from google.appengine.ext import webapp
from sms_message import IncomingSMSMessage

class MainPage(webapp.RequestHandler):
	"""
	This is a debugging page that allows me to test how the code handles messages.
	"""
	def get(self):
		self.response.out.write("""
      <html>
        <body>
          <form action="/register" method="post">
            <div>
              <label for="entry_0">Phone Number </label>
              <label for="entry_0">Phone number text came from </label>
              <input id="entry_0" type="text" value="" name="phone"/>
            </div>
            <br />
            <div>
              <label for="entry_1">Body of SMS </label>
              <label for="entry_1">body of sms </label>
              <textarea id="entry_1" cols="75" rows="8" name="body"> 
              </textarea>
            </div>
            <br />
            <div>
              <input type="submit" value="Submit"/>
            </div>
          </form>
        </body>
      </html>""")


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
		msg.save()

