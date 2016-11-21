# coding: utf-8
import os
import thriftpy
import json
import logging

from thriftpy.rpc import make_client
from xylose.scielodocument import Article, Journal

LIMIT = 1000

logger = logging.getLogger(__name__)

accessstats_thrift = thriftpy.load(
    os.path.join(os.path.dirname(__file__))+'/accessstats.thrift')

publicationstats_thrift = thriftpy.load(
    os.path.join(os.path.dirname(__file__))+'/publicationstats.thrift')


class ServerError(Exception):
    def __init__(self, message=None):
        self.message = message or 'thirftclient: ServerError'

    def __str__(self):
        return repr(self.message)


class PublicationStats(object):

    def __init__(self, address, port):
        """
        Cliente thrift para o Publication Stats.
        """
        self._address = address
        self._port = port

    @property
    def client(self):

        client = make_client(
            publicationstats_thrift.PublicationStats,
            self._address,
            int(self._port)
        )
        return client

    def document(self, code, collection):

        return self.client.document(code, collection)


class AccessStats(object):

    def __init__(self, address, port):
        """
        Cliente thrift para o Access Stats.
        """
        self._address = address
        self._port = port

    @property
    def client(self):

        client = make_client(
            accessstats_thrift.AccessStats,
            self._address,
            int(self._port)
        )
        return client

    def document(self, code, collection):

        return self.client.document(code, collection)
