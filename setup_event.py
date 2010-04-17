#import from sys
import hashlib
import urllib

#import from appengine
from google.appengine.api import urlfetch

# import from local
from sms_gateway import ClickatellGateway
from models import RegisteredVisitor

class Event(object):
	"""
	Represents an sms message
	"""
	ORIGIN = '233261685159'

	def __init__(self):
		'Constructor'
		self.m_code = None
		self.m_name = None
		self.m_date = None
		self.m_description = None

	def set_code(self, code):
		'Accessor for body'
		self.m_code = code

	def set_name(self, name):
		'Accessor for phone number'
		self.m_name = name

	def set_date(self, body):
		'Accessor for body'
		self.m_body = body

	def set_description(self, description):
		'Accessor for phone number'
		self.m_description = description

	def confirm(self):
		'Confirm receipt of the message. No default implementation.'
		raise NotImplementedError

	def save(self):
		'Save to the datastore'
		user = RegisteredVisitor()
		user.phone = self.m_phone
		user.body = self.m_body
		user.hash = self.get_hash()
		return user.put()

class IncomingSMSMessage(SMSMessage):
	"""
	Respresents an incoming sms message
	"""
	def __init__(self, phone, body):
		''
		self.set_phone(phone)
		self.set_body(body)

	def confirm(self):
		'Use clickatell to confirm the message'
		confirm_msg = "We are excited you are coming to Maker Faire Africa 2010, Aug 6-7. Your confirmation # is %s" % (self.get_confirmation_number())
		sms_gateway = ClickatellGateway()
		sms_gateway.send(self.ORIGIN, self.m_phone, confirm_msg)

	def save(self):
		'Override so that we can also write to google docs'
		SMSMessage.save(self)
		self.googleDocIt()

	def get_confirmation_number(self):
		'Return a digit number taken from the hash'
		hash = self.get_hash()
		subhash = ''
		if len(hash) > 11:
			subhash = hash[3:10]
		else:
			subhash = hash
		return subhash

	def googleDocIt(self):
		'Save to google docs so that we can share with other mfa organizers'
		form_fields = {
			"formkey": "dHg3d0FuMTdJcVZCa1NDakRIQTBuVmc6MA..",
			"entry.0.single": self.m_phone,
			"entry.1.single": self.m_body,
			"entry.2.single": self.get_confirmation_number(),
			}
		form_data = urllib.urlencode(form_fields)
		url = "http://spreadsheets.google.com/formResponse"
		result = urlfetch.fetch(url=url,
					payload=form_data,
					method=urlfetch.POST,
					headers={'Content-Type': 'application/x-www-form-urlencoded'})

