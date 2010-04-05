# The entry point to the webapp
# API import 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#local imports
from handlers import MainPage, Register

application = webapp.WSGIApplication(
  [('/', MainPage), 
   ('/register', Register)],
  debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
    main()
