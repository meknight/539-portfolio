#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# all pages in single handler
class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'Work'}))
    def about(self):
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    	self.response.write(template.render({'title': 'About'}))
    def fun(self):
        template = JINJA_ENVIRONMENT.get_template('templates/fun.html')
    	self.response.write(template.render({'title': 'Fun'}))
    def contact(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title': 'Contact'}))


# login page with separate handler
# class LoginHandler(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('templates/login.html')
#     	self.response.write(template.render({'title': 'Login'}))
#     def post(self):
#     	in_username = self.request.get('name')
#     	in_password = self.request.get('pw')

#     	username = 'Colleen'
#     	password = 'pass'

#     	if in_username == username and in_password == password:
#     		template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
#     		self.response.write(template.render({'title': 'Welcome'}))
#     		logging.info(in_username)
#     		logging.info(in_password)
#     	else:
#     		template = JINJA_ENVIRONMENT.get_template('templates/login.html')
#     		self.response.write(template.render({'title': 'Login', 'incorrect': 'Bad credentials. Try again.'}))
#     		logging.info('Incorrect username: %s', in_username)
#     		logging.info('Incorrect password: %s', in_password)


    	

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    webapp2.Route('/about.html', handler=IndexHandler, handler_method='about'),
    webapp2.Route('/fun.html', handler=IndexHandler, handler_method='fun'),
    webapp2.Route('/contact.html', handler=IndexHandler, handler_method='contact'),
    # ('/login.html', LoginHandler)
], debug=True)
