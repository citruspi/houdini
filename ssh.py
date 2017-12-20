#!/usr/bin/env python3
# coding: utf-8 -*-

import base64
from io import StringIO
import boto3
import paramiko

ssm = boto3.client('ssm')


def exec(payload):
    resp = {'stdin': None, 'stdout': None, 'stderr': None}

    address = payload.get('address')
    command = payload.get('command')
    username = payload.get('username')
    private_key_name = payload.get('private-key')

    if None in [address, command, username, private_key_name]:
        raise Exception('Missing arguments')

    try:
        private_key_encoded = ssm.get_parameter(
            Name=f'ssh-private-key-{private_key_name}',
            WithDecryption=True
        )['Parameter']['Value']
    except Exception as ex:
        raise Exception('Failed to load private key from AWS SSM Parameter Store')

    private_key = paramiko.rsakey.RSAKey.from_private_key(
        StringIO(base64.b64decode(private_key_encoded).decode('utf-8'))
    )

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(address, username=username, pkey=private_key)

    stdin, stdout, stderr = ssh.exec_command('uptime')

    try:
        resp['stdin'] = stdin.read().decode('utf-8')
    except Exception:
        pass

    try:
        resp['stdout'] = stdout.read().decode('utf-8')
    except Exception:
        pass

    try:
        resp['stderr'] = stderr.read().decode('utf-8')
    except Exception:
        pass

    ssh.close()

    return resp
