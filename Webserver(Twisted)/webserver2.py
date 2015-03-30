from twisted.web import server, resource
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
from pprint import pprint

class Simple(Resource):
	def render_POST(self, request):  
		request.redirect("http://student.cs.plattsburgh.edu:8081/zed")
		request.finish()
		return server.NOT_DONE_YET 

def main():
	root = Resource()
	root.putChild("foo", File("/home/cbowi001/files/webserverchatroom/login.html"))
	root.putChild("bar", File("/home/cbowi001/files/webserverchatroom/index.html"))
	root.putChild("zed", File("/home/cbowi001/files/webserverchatroom/htmlchatroom.html"))
	root.putChild("pst", Simple())
	factory = Site(root)
	reactor.listenTCP(8081, factory)
	reactor.run()

main()
