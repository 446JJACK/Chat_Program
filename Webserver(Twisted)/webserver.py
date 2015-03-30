from twisted.web import server, resource
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
    

def main():
    root = Resource()
    root.putChild("foo", File("/home/chris/Documents/login.html"))
    root.putChild("bar", File("/home/chris/Documents/index.html"))
    root.putChild("zed", File("/home/chris/Documents/htmlchatroom.html"))
    factory = Site(root)
    reactor.listenTCP(8080, factory)
    reactor.run()


main()
