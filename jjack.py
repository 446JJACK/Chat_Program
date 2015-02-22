from twisted.web import http

class MyRequestHandler(http.Request):
    pages = {
        '/': '<h1>Home</h1>Home page',
        '/index.html': '<h1>Test</h1>Test page',
        }

    def process(self):
        if self.pages.has_key(self.path):
            self.write(self.pages[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such page.")
        self.finish()

class MyHttp(http.HTTPChannel):
    requestFactory = MyRequestHandler

class MyHttpFactory(http.HTTPFactory):
    protocol = MyHttp

if __name__ == "_ _main_ _":
    from twisted.internet import reactor
    reactor.listenTCP(8080, MyHttpFactory())
    reactor.run()