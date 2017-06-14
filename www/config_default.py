#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Primo Lin'

configs = {
    'debug': True,
    'db': {
        'host': '10.1.20.130',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'test'
    },
    'session': {
        'secret': 'Awesome'
    }
}
