from twisted.internet import task, defer

import treq

@task.react
@defer.inlineCallbacks
def main(reactor):
    response = yield treq.get('https://example.com/')
    print("got code: {}".format(response.code))

    body = yield treq.content(response)
    print("got {} bytes".format(len(body)))
