__author__ = 'chadhurley'
import os
import sys

TESTDIR = os.path.dirname(os.path.realpath(__file__))
ROOTDIR = os.path.dirname(TESTDIR)
sys.path.insert(0, ROOTDIR)

from unittest import main, TestCase
from client import Omnivore

from config import api_key


def get_omnivore_client():
    client = Omnivore()
    return client

get_omivore_client = get_omnivore_client()

class OmnivoreClientTestBase(TestCase):
    def setUp(self):
        pass

    @property
    def client(self):
        return get_omivore_client