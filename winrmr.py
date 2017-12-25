#!/usr/bin/env python3
# coding: utf-8 -*-

import winrm


def exec(payload):
    resp = {'stdin': None, 'stdout': None, 'stderr': None}

    address = payload.get('address')
    command = payload.get('command')
    username = payload.get('username')
    password = payload.get('password')

    if None in [address, command, username, password]:
        raise Exception('Missing arguments')

    command = command.split(' ')

    winrm_conn = winrm.Session(address, auth=(username, password))
    winrm_resp = winrm_conn.run_cmd(command[0], command[1:])

    resp['stdout'] = winrm_resp.std_out
    resp['stderr'] = winrm_resp.std_err

    return resp
