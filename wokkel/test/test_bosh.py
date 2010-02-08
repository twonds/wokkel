# Copyright (c) 2009 Christopher Zorn (tofu@thetofu.com)
# See LICENSE for details.

"""
Tests for L{wokkel.bosh}.
"""

from twisted.internet import defer
from twisted.trial import unittest


class BOSHClient(unittest.TestCase):
    """
    Tests for BOSH client connections
    """
