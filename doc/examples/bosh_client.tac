"""
An example BOSH client.

"""

from twisted.application import service
from twisted.words.protocols.jabber.jid import JID
from wokkel import bosh

# Configuration parameters

LOG_TRAFFIC = True

# Set up the Twisted application

application = service.Application("BOSH Client")

client = bosh.XMPPClient(JID("tofu@localhost"), "secret", url="http://localhost:5280/bosh")
client.logTraffic = LOG_TRAFFIC
client.setServiceParent(application)

