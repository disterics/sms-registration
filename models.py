from google.appengine.ext import db

class RegisteredVisitor(db.Model):
    """
    Represents a text message from a user who is registering for MFA
    """
    phone = db.PhoneNumberProperty()
    body = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    hash = db.StringProperty()

class Event(db.Model):
    """
    Create an event for users to register
    """
    code = db.StringProperty()
    name = db.StringProperty()
    date = db.DateTimeProperty()
    description = db.TextProperty()