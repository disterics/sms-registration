import os
from google.appengine.ext import webapp
from sms_message import IncomingSMSMessage
from google.appengine.ext.webapp import template
from models import *

class MainPage(webapp.RequestHandler):
	"""
	This is a debugging page that allows me to test how the code handles messages.
	"""
	def get(self):
		template_values = {}
		path = os.path.join(os.path.dirname(__file__), 'templates/registration.html')
		self.response.out.write(template.render(path, template_values))

class Register(webapp.RequestHandler):
	"""
        Handles the form submission
	"""
	debug = False
	def get(self):
		'Pass on get requests to the post handler.'
		self.post()

	def post(self):
		'Handle the post request.'
		msg = IncomingSMSMessage(self.request.get('phone'), 
							self.request.get('body'))
		msg.confirm()
		event = msg.save()
		if msg:
			template_values = {'event': event}
			path = os.path.join(os.path.dirname(__file__), 'templates/notification.html')
			self.response.out.write(template.render(path, template_values))

class Event(webapp.RequestHandler):
	"""
	This is a debugging page that allows me to test how the code creates events.
	"""
	def get(self):
		template_values = {}
		path = os.path.join(os.path.dirname(__file__), 'templates/event.html')
		self.response.out.write(template.render(path, template_values))

class ListVisitors(webapp.RequestHandler):
	"""
	This is a debugging page that allows me to test how the code creates events.
	"""
	def get(self):
		visitors = db.GqlQuery("SELECT * FROM RegisteredVisitor ORDER BY phone DESC LIMIT 10")
		template_values = {'visitors': visitors}

		path = os.path.join(os.path.dirname(__file__), 'templates/visitor_list.html')
		self.response.out.write(template.render(path, template_values))