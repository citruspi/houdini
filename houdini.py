#!/usr/bin/env python3
# coding: utf-8 -*-

import ssh
import winrmr


def lambda_handler(event, context):
    mode = event.get('mode')

    if mode is None:
        return
    elif mode == 'ssh':
        return ssh.exec(event)
    elif mode == 'winrm':
        return winrmr.exec(event)
