from twisted.web import server, resource, static
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.server import Site
import sqlite3
import JSON

#global var for database
global DATABASE = 'users.db'


#Populate messages to chat box div
class get_Chat(Resource):
        def render_POST(self, request):
		a = request.args
		db = sqlite3.connect(DATABASE )
		data = db.cursor()
		table = data.execute('''select * from DATABASE ''')
		db.close()
		#convert data to JSON format here
		print table
		return table
 
#retrieve message from submit form; store to db
class get_Message(Resource):

        def render_POST(self, request):
                a = request.args
                b = a['message']
                print b               
                db = sqlite3.connect('user.db')
                data = db.cursor()
                data.execute('''INSERT INTO test(message) VALUES(?)''',(b))
                db.commit()
                db.close()
             
                return ''

#Needs more work
class verify_User(Resource):
	
	def render_POST(self, request):
		a = request.args
		db = sqlite3.connect('users.db')
		data = db.cursor()
		#add verification command
		db.commit()
		db.close()

#Needs more work
class delete_User(Resource):

	def render_POST(self, request):
		a = request.args
		db = sqlite3.connect('users.db')
		data = db.cursor()
		#add delete command
		db.commit()
		print 'User delted'
		db.close()		

#Needs error handling and success return response
class add_User(Resource):

	def render_POST(self, request):
		a = request.args
		db = sqlite3.connect('users.db')
		data = db.cursor()
		username = a['useraccount'][0]
		password = a['password'][0]
		#displayname = #populate
		data.execute('''INSERT INTO users(username, password)
			VALUES(?,?)''',(username, password))
		db.commit()
		print a
		print 'User submitted'
		db.close()
		request.redirect("http://student.cs.plattsburgh.edu:8081/chat")
		request.finish()
		return server.NOT_DONE_YET		 

#Test function - currently not in use
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
        #Pinning the pages    
	root = resource.Resource()
	root.putChild('', File("/home/cbowi001/files/chatv1/index.html"))
	root.putChild('add', add_User())
	root.putChild('chat', File("/home/cbowi001/files/chatv1/NEWchatPageV1.html"))
	root.putChild('grab', get_Message())
	root.putChild('grabMessage.js', File("/home/cbowi001/files/chatv1/grabMessage.js"))
	root.putChild('ajax.js', File('/home/cbowi001/files/chatv1/ajax.js'))
	root.putChild('login.css', static.File('/home/cbowi001/files/chatv1/login.css'))
	root.putChild('NEWchatPageV1.css', static.File('/home/cbowi001/files/chatv1/NEWchatPageV1.css'))
	root.putChild('populate', get_Chat())
	
	#Running the server
	factory = Site(root)
	reactor.listenTCP(8081, factory)
	reactor.run()

main()


