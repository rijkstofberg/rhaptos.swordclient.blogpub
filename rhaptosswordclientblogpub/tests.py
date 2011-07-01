import unittest
from pyramid.config import Configurator
from pyramid import testing

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_it(self):
        from rhaptosswordclientblogpub.views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'rhaptos.swordclient.blogpub')
