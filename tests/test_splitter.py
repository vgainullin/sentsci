import unittest
import nltk
from sentsci import splitter


class TestSentSci(unittest.TestCase):

    def test_split(self):
        text = "Japan is a country. Hello world."
        result = splitter.split(text)
        print(result)
        self.assertEqual(len(result), 2)
        text = "Japan is a country (Fig.1E). Hello world."
        result = splitter.split(text)
        self.assertEqual(len(result), 2)

    def test_nb_split(self):
        text = "Japan is a country. Hello world."
        result = splitter.nb_split(text)
        self.assertEqual(len(result), 2)
        text = "Japan is a country (Fig.1E). Hello world."
        result = splitter.nb_split(text)
        #self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()
