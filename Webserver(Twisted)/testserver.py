from twisted.web import server, resource, static
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
import sqlite3


class get_Message(Resource):

    def render_POST(self, request):
        a = request.args
        b = a['message']
        print b
        db = sqlite3.connect('user.db')
        data = db.cursor()
        data.execute('''INSERT INTO test(message) VALUES(?)''', (b))
        db.commit()
        db.close()

        return ''


class verify_User(Resource):

    def render_POST(self, request):
        a = request.args
        db = sqlite3.connect('users.db')
        data = db.cursor()
        # add verification command
        db.commit()
        db.close()


class delete_User(Resource):

    def render_POST(self, request):
        a = request.args
        db = sqlite3.connect('users.db')
        data = db.cursor()
        # add delete command
        db.commit()
        print 'User delted'
        db.close()


class add_User(Resource):

    def render_POST(self, request):
        a = request.args
        db = sqlite3.connect('users.db')
        data = db.cursor()
        username = a['useraccount'][0]
        password = a['password'][0]
        # displayname = #populate
        data.execute('''INSERT INTO users(username, password)
			VALUES(?,?)''', (username, password))
        db.commit()
        print a
        print 'User submitted'
        db.close()
        request.redirect("http://student.cs.plattsburgh.edu:8081/chat")
        request.finish()
        return server.NOT_DONE_YET


class Test(Resource):

    def render_POST(self, request):
        a = request.args
        #b = a['useraccount'][0]
        #c = a['password'][0]
        print a
        request.redirect("http://student.cs.plattsburgh.edu:8081/zed")
        request.finish()
        return server.NOT_DONE_YET


def main():
    # Need to static.FIle css pages and learn to serve /index firsts
    # Pinning the pages

    root = resource.Resource()
    root.putChild('', File("/home/cbowi001/files/chatv1/index.html"))
    root.putChild('add', add_User())
    root.putChild(
        'chat',
        File("/home/cbowi001/files/chatv1/NEWchatPageV1.html"))
    root.putChild('grab', get_Message())
    root.putChild(
        'grabMessage.js',
        File("/home/cbowi001/files/chatv1/grabMessage.js"))
    root.putChild(
        'login.css',
        static.File('/home/cbowi001/files/chatv1/login.css'))
    root.putChild(
        'NEWchatPageV1.css',
        static.File('/home/cbowi001/files/chatv1/NEWchatPageV1.css'))

    # Running the server
    factory = Site(root)
    reactor.listenTCP(8081, factory)
    reactor.run()

main()
