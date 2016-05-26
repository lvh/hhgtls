import certifi
import socket
import ssl


# Find OpenSSL version
print(ssl.OPENSSL_VERSION)


# First, this is what you do if you have a good, recent Python.
def if_your_python_is_good():
    # If on Linux:
    context = ssl.create_default_context()
    # Otherwise:
    context = ssl.create_default_context(cafile=certifi.where())

    # If using any other stdlib module than socket, you will probably not need
    # to do this. Instead, you'll be able to pass the context object itself to
    # the module. This works for e.g. asyncio.
    sock = socket.create_connection(('http2bin.org', 443))
    sock = context.wrap_socket(sock, server_hostname='http2bin.org')

    # GO GO GO


# For older Pythons:
def if_your_python_is_bad():
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv2 | ssl.OP_NO_COMPRESSION
    context.verify_mode = ssl.CERT_REQUIRED

    # If on Linux:
    context.load_default_certs()
    # else:
    context.load_verify_locations(cafile=certifi.where())

    sock = socket.create_connection(('http2bin.org', 443))
    sock = context.wrap_socket(sock, server_hostname='http2bin.org')

    # GO GO GO


# Advantages:
# - Built in to the standard library.
# - For newer Pythons, good configuration isn't too hard.
# - Works with other standard library modules, like asyncio.
#
# Disadvantages:
# - The OpenSSL Python is linked against might suck, and replacing it is hard.
#   This is very true on OS X, which is linked against 0.9.8zh, but also true
#   on many other platforms.
# - There is much less flexibility in this API: certain things you might want
#   to do are simply impossible.
# - On Python < 2.7.9 this module is actively terrible and should be avoided as
#   much as possible.
