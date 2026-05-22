thriftpy-wrap
=============

A thin wrap around thriftpy2 to help you create console based server applications.
It also extends thriftpy2 in order to make possible to run the server against
already opened sockets.


.. code-block:: python

    import thriftpy2
    import thriftpywrap

    spec = thriftpy2.load('dsl.thrift')


    class Handler(object)
        """ Remote procedures """
    
    if __name__ == '__main__':
        app = thriftpywrap.ConsoleApp(spec.Service, Handler)
        app()


Executing this script will result is something like:

.. code-block:: bash

    $ python ping_server.py
    usage: ping_server.py [-h] [--port PORT]
                      [--address-family {AF_APPLETALK,AF_DECnet,AF_INET,AF_INET6,AF_IPX,AF_ROUTE,AF_SNA,AF_UNIX,AF_UNSPEC}]
                      (--host HOST | --unix-socket UNIX_SOCKET | --fd FD)
                      [--loglevel LOGLEVEL]
                      [arguments [arguments ...]]
    ping_server.py: error: one of the arguments --host --unix-socket --fd is required
