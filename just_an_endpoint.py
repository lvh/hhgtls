from twisted.internet import task, endpoints, defer, protocol
@task.react
@defer.inlineCallbacks
def main(reactor):
    endpoint = endpoints.clientFromString(reactor,
                                          "tls:chat.freenode.net:6697")
    done = defer.Deferred()
    class Printer(protocol.Protocol):
        def dataReceived(self, data):
            print(repr(data))
        def connectionLost(self, reason):
            done.callback(reason)
    yield endpoint.connect(protocol.Factory.forProtocol(Printer))
    yield done
