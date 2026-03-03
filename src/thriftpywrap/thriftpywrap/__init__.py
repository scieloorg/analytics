#coding: utf-8
from __future__ import absolute_import

import logging
import argparse
import socket
import sys

from thriftpy2.protocol import TBinaryProtocolFactory
from thriftpy2.server import TThreadedServer
from thriftpy2.thrift import TProcessor
from thriftpy2.transport import (TBufferedTransportFactory, TServerSocket, )

__all__ = ['ConsoleApp']

_ADDRESS_FAMILY = [af for af in dir(socket) if af.startswith('AF_')]
_DEFAULT_DESCRIPTION = 'Thrift-based RPC server.'
_PROTO_FACTORY = TBinaryProtocolFactory
_TRANS_FACTORY = TBufferedTransportFactory

logger = logging.getLogger(__name__)


def get_description(handler, default=None):
    default_description = default or _DEFAULT_DESCRIPTION
    return handler.__description__ if hasattr(
        handler, '__description__') else default_description


def ConsoleApp(spec, handler,
               proto_factory=_PROTO_FACTORY(),
               trans_factory=_TRANS_FACTORY()):
    def app():
        parser = argparse.ArgumentParser(description=get_description(handler))
        parser.add_argument('--port', type=int, default=8080)
        parser.add_argument('--address-family',
                            type=str,
                            default='AF_INET',
                            choices=sorted(_ADDRESS_FAMILY))
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--host')
        group.add_argument('--unix-socket')
        group.add_argument('--fd', type=int)
        parser.add_argument(
            'arguments',
            default=[],
            nargs='*',
            help="Optional arguments you may need for your app")

        parser.add_argument('--loglevel', default='info', help="log level")
        args = parser.parse_args()

        logging.basicConfig(level=getattr(logging, args.loglevel.upper()))

        address_family = getattr(socket, args.address_family)

        logger.debug('Protocol factory: %s', proto_factory)
        logger.debug('Transport factory: %s', trans_factory)

        server = make_server(spec, handler(*args.arguments),
                             fd=args.fd,
                             host=args.host,
                             port=args.port,
                             unix_socket=args.unix_socket,
                             address_family=address_family,
                             proto_factory=proto_factory,
                             trans_factory=trans_factory)
        try:
            server.serve()
        except KeyboardInterrupt:
            sys.exit(1)
        finally:
            server.trans.close()
            logger.debug('Closing transport %s', server.trans)

    return app


def make_server(service, handler,
                fd=None,
                host=None,
                port=None,
                unix_socket=None,
                address_family=socket.AF_INET,
                proto_factory=None,
                trans_factory=None):
    processor = TProcessor(service, handler)
    if unix_socket is not None:
        logger.info('Setting up server bound to %s', unix_socket)
        server_socket = TServerSocket(unix_socket=unix_socket,
                                      socket_family=address_family)
    elif fd is not None:
        logger.info('Setting up server bound to socket fd %s', fd)
        server_socket = TFDServerSocket(fd=fd, socket_family=address_family)
    elif host is not None and port is not None:
        logger.info('Setting up server bound to %s:%s', host, str(port))
        server_socket = TServerSocket(host=host,
                                      port=port,
                                      socket_family=address_family)
    else:
        raise ValueError('Insufficient params')

    server = TThreadedServer(processor, server_socket,
                             iprot_factory=proto_factory,
                             itrans_factory=trans_factory)
    return server


class TFDServerSocket(TServerSocket):
    def __init__(self, fd=None, **kwargs):
        self._fd = fd
        super(TFDServerSocket, self).__init__(**kwargs)

    def _init_sock(self):
        if self._fd is None:
            super(TFDServerSocket, self)._init_sock()
            self.handle = self.sock
            return

        self.sock = socket.fromfd(self._fd, self.socket_family, socket.SOCK_STREAM)
        self.handle = self.sock
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            try:
                self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except OSError:
                pass
        self.sock.settimeout(None)

    def listen(self):
        if self._fd is None:
            super(TFDServerSocket, self).listen()
            logger.debug('Started listening socket %s', repr(self.sock))
            logger.info('Started listening %s', self.sock.getsockname())
            return

        self._init_sock()
        self.sock.listen(self.backlog)
        logger.debug('Started listening socket %s', repr(self.sock))
        logger.info('Started listening %s', self.sock.getsockname())
