# Copyright (c) 2009 Christopher Zorn (tofu@thetofu.com)
# See LICENSE for details.

"""
Tests for L{wokkel.bosh}.
"""

from twisted.internet import defer, reactor
from twisted.trial import unittest
from twisted.web import server as webserver, resource, static

from wokkel import bosh

class TestResource(resource.Resource):
    """
    Resource to mimic BOSH connection manager.
    """

    isLeaf = False

    def request_GET(self, request):
        """
        Return simple string.
        """
        return "BOSH"

    def request_POST(self, request):
        
        return "POST"


    

class BOSHClient(unittest.TestCase):
    """
    Tests for BOSH client connections
    """


    def setUp(self):
        """
        Basic http server to handle requests.
        """

        self.root     = static.File("./html") # make _trial_temp/html the root html directory
        self.resource = TestResource()
        self.root.putChild('bosh', self.resource)

        self.site  = webserver.Site(self.root)
        
        self.p =  reactor.listenTCP(0, self.site, interface="127.0.0.1")
        self.port = self.p.getHost().port
                
        # set up proxy        
        self.proxy = bosh.Proxy(self.getURL())
        self.sid   = None
        self.keys  = bosh.Keys()

        
    def getURL(self, path = "bosh"):
        return "http://127.0.0.1:%d/%s" % (self.port, path)
        
    
        
    def testClientCreator(self):

        return True
    

    def tearDown(self):
        def cbStopListening(result=None):
            
            self.root = None
            self.site = None
            #self.proxy.factory.stopFactory()
            
            self._cleanPending()
            self._cleanSelectables()

        #if hasattr(self.proxy.factory,'client'):
        #    self.proxy.factory.client.transport.stopConnecting()
        
        d = defer.maybeDeferred(self.p.stopListening)
        d.addCallback(cbStopListening)

        return d

    def _cleanPending(self):
        pending = reactor.getDelayedCalls()
        if pending:
            for p in pending:
                if p.active():
                    p.cancel()

    def _cleanSelectables(self):
        removedSelectables = reactor.removeAll()
