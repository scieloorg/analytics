import unittest
import socket
import tempfile
import os

import thriftpy2
from thriftpywrap import (get_description, make_server, )

spec = thriftpy2.load(os.path.join(os.path.dirname(__file__), "spec.thrift"))


class Dispatcher(object):
    def ping(self):
        return True


class GetDescriptionTests(unittest.TestCase):
    def test_from_class(self):
        class Foo(object):
            __description__ = """Foobar"""

        self.assertEqual(get_description(Foo), 'Foobar')

    def test_from_instance(self):
        class Foo(object):
            __description__ = """Foobar"""

        self.assertEqual(get_description(Foo()), 'Foobar')

    def test_missing(self):
        class Foo(object):
            pass

        self.assertEqual(get_description(Foo(), default='Foo'), 'Foo')

    def test_from_class_missing(self):
        class Foo(object):
            pass

        self.assertEqual(get_description(Foo, default='Foo'), 'Foo')


class MakeServerTests(unittest.TestCase):
    def test_unix_domain_socket(self):
        """Does not create/bind/listen the socket
        """
        from thriftpy2.server import TThreadedServer
        temp_dir = tempfile.mkdtemp()
        sock_path = os.path.join(temp_dir, 'test_sock.sock')

        server = make_server(spec, Dispatcher(), unix_socket=sock_path)
        self.assertIsInstance(server, TThreadedServer)

    def test_host_port(self):
        """Does not create/bind/listen the socket
        """
        from thriftpy2.server import TThreadedServer
        server = make_server(spec, Dispatcher(), host='0.0.0.0', port=0)
        self.assertIsInstance(server, TThreadedServer)

    def test_fd(self):
        from thriftpy2.server import TThreadedServer
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', 0))

            server = make_server(spec, Dispatcher(), fd=sock.fileno())
            self.assertIsInstance(server, TThreadedServer)

            server.trans.listen()
            self.assertEqual(server.trans.handle.getsockname(),
                             sock.getsockname())
        finally:
            server.trans.close()
            sock.close()
