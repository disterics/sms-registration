import urllib
from google.appengine.api import urlfetch

class SMSGateway(object):
    'Represents and SMS gateway'
    
    def send(self, source, dest, msg):
        raise NotImplementedError


class ClickatellGateway(SMSGateway):
    'Clickatell implementation of the SMS Gateway'
    API_URL = "http://api.clickatell.com/http/sendmsg"
    DEBUG = False

    def __init__(self):
        'Init the authentication tokens'
        self.m_user = '???'
        self.m_api_id = '????'
        self.m_req_feat = '48'
        self.m_passwd = '?????'
    
    def send(self, source, dest, msg):
        'Clickatell specific send'
        #todo check length of message

        form_fields = {
            "user" : self.m_user,
            "password" : self.m_passwd,
            "api_id" : self.m_api_id,
            "from" : source,
            "req_feat" : self.m_req_feat,
            "to": dest,
            "text": msg,
            }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url=self.API_URL,
                                payload=form_data,
                                method=urlfetch.POST,
                                headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if self.DEBUG and result.status_code == 200:
            self.response.out.write(result.content)
