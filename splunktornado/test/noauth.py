from tornado.testing import LogTrapTestCase, AsyncHTTPTestCase
from tornado.web import RequestHandler, _O, authenticated, Application

import logging
import re

class SimpleRequestHandler(RequestHandler):
    def initialize(self, login_url):
        pass

class SimpleTest(AsyncHTTPTestCase, LogTrapTestCase):
    pass