from twisted.internet import defer, task, ssl
from twisted.web import client, iweb
from zope.interface import implementer
import sys, treq
@task.react
@defer.inlineCallbacks
def main(reactor):
    with open(sys.argv[1]) as f: root = ssl.Certificate.loadPEM(f.read())
    @implementer(iweb.IPolicyForHTTPS)
    class OneTrust(object):
        def creatorForNetloc(self, host, port):
            return ssl.optionsForClientTLS(host.decode("ascii"), root)
    treqish = treq.client.HTTPClient(client.Agent(reactor, OneTrust()))
    response = yield treqish.get('https://example.com/')
    print("got code: {}".format(response.code))
    body = yield treq.content(response)
    print("got {} bytes".format(len(body)))
