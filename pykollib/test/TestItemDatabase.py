from pykollib.database import ItemDatabase

import unittest


class Main(unittest.TestCase):
    def runTest(self):
        ItemDatabase.init()
