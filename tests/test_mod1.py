import os
import unittest

from mod1 import primary


class TestMod1(unittest.TestCase):
    def test_one(self):
        output = primary.first_one(5)
        self.assertTrue(output > 0)

    def test_two(self):
        output = primary.second_one()
        self.assertEqual(output, [2])


if __name__ == "__main__":
    unittest.main()
