#!/usr/bin/env python3
# coding: utf-8 -*-

import base64
from io import StringIO
import boto3
import paramiko
import winrm

ssm = boto3.client('ssm')


def ssh_exec(event):
    resp = {'stdin': None, 'stdout': None, 'stderr': None}

    address = event.get('address')
    command = event.get('command')
    username = event.get('username')
    private_key_name = event.get('private-key')

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

    stdin, stdout, stderr = ssh.exec_command(command)

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


def winrm_exec(event):
    resp = {'stdin': None, 'stdout': None, 'stderr': None}

    address = event.get('address')
    command = event.get('command')
    username = event.get('username')
    password = event.get('password')

    if None in [address, command, username, password]:
        raise Exception('Missing arguments')

    command = command.split(' ')

    winrm_conn = winrm.Session(address, auth=(username, password))
    winrm_resp = winrm_conn.run_cmd(command[0], command[1:])

    resp['stdout'] = winrm_resp.std_out
    resp['stderr'] = winrm_resp.std_err

    return resp


def lambda_handler(event, context):
    mode = event.get('mode')

    if mode is None:
        return
    elif mode == 'ssh':
        return ssh_exec(event)
    elif mode == 'winrm':
        return winrm_exec(event)
