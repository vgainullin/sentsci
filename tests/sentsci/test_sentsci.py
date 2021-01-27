import unittest
from sentsci.sentsci import split, nb_split


class TestSentSci(unittest.TestCase):

    def test_split(self):
        text = "This is sentence number one. This is the second sentence."
        result = split(text)
        self.assertEqual(len(result), 2)


    def test_nb_split(self):
        text = "This is sentence number one. This is the second sentence."
        result = nb_split(text)
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()
