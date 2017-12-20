#!/usr/bin/env python3
# coding: utf-8 -*-

import ssh


def lambda_handler(event, context):
    mode = event.get('mode')

    if mode is None:
        return
    elif mode == 'ssh':
        return ssh.exec(event)
