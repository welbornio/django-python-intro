import logging
import os
import datetime
import wsgiref.handlers
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import webapp

class LogSenderHandler(InboundMailHandler):
	def receive(self, mail_message):
		logging.info("Received a message from: " + mail_message.sender)
		message = mail.EmailMessage(sender=mail_message.sender, subject=mail_message.subject, to="welborn.ethan@gmail.com")
		maintype = mail_message.original.get_content_maintype()

		body_string = ""
		payload = mail_message.original.get_payload(0)
		if isinstance(payload, list):
			for m in payload:
				body_string += str(m)
		else:
			body_string = str(payload)

		message.body = body_string

		logging.info("Sending message to welborn.ethan@gmail.com")
		message.send()
		


application = webapp.WSGIApplication([
    ('.*', LogSenderHandler),
], debug=True)


def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()