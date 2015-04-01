from twisted.web import server, resource, static
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
import sqlite3

class verify_User(Resource):
	
	def render_POST(Resource):
		a = request.args
		db = sqlite3.connect('users.db')
		data = db.cursor()
		#add verification command
		db.commit()
		db.close()

class delete_User(Resource):

	def render_POST(self, request):
		a = request.args
		db = sqlite3.connect('users.db')
		data = db.cursor()
		#add delete command
		db.commit()
		print 'User delted'
		db.close()		

class add_User(Resource):

	def render_POST(self, request):
		a = request.args
		db = sqlite3.connect('users.db')
		data = db.cursor()
		#username = #populate
		#password = #populate
		#displayname = #populate
		data.execute('''INSERT INTO users(username INTEGER PRIMARY KEY, password, displayname)
			VALUES(?,?,?)''',(username, password, displayname))
		db.commit()
		print 'User submitted'
		db.close()		 

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
	#Need to static.FIle css pages and learn to serve /index firsts
        #Pinning the pages 
	root = Resource()
	root.putChild("login", File("/home/cbowi001/files/webserverchatroom/newchathtmls/index.html")) #shorten file path
	root.putChild("chatroom", File("/home/cbowi001/files/webserverchatroom/newchathtmls/NEWchatPageV1.html")) #shorten file path
	#root.putChild("styles.css", static.File("/home/cbowi001/files/webserverchatroom/newchathtmls/login.css"))
	#root.putChild("zed", File("/home/cbowi001/files/webserverchatroom/htmlchatroom.html"))

	
	#Running the server
	factory = Site(root)
	reactor.listenTCP(8081, factory)
	reactor.run()

main()
