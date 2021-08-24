import unittest
from mod2.core import and_another_one


class TestSecondary(unittest.TestCase):

    def test_and_another_one(self):
        self.assertEqual("DJ Khaled!", and_another_one())

