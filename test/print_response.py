#!/bin/env python

import logging

import context

from vndb_thigh_highs import VNDB, Config
from vndb_thigh_highs.socket import Socket
from vndb_thigh_highs.models import *

class PrintSocket(Socket):
    def communicate(self, message):
        response = super().communicate(message)
        escaped_response = response.replace('\\', '\\\\')
        print("Received '%s'" % escaped_response)
        return response

def main():
    vndb = create_client()
    vndb.get_release(Release.id == 350)

def create_client():
    config = Config()
    socket = PrintSocket(config.logger)
    return VNDB(config=config, socket=socket)

if __name__ == '__main__':
    main()
