import unittest
from vcode import vcode, ALPHABET


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(ALPHABET,
                         vcode('a', ALPHABET))

    def test_b(self):
        self.assertEqual('bcdefghijklmnopqrstuvwxyza',
                         vcode('b', ALPHABET))

    def test_n(self):
        self.assertEqual('nopqrstuvwxyzabcdefghijklm',
                         vcode('n', ALPHABET))

    def test_ab(self):
        self.assertEqual('accee',
                         vcode('ab', 'abcde'))

    def test_caps(self):
        self.assertEqual('aA',
                         vcode('aa', 'aA'))

    def test_from_book(self):
        mymessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
        mykey = 'ASIMOV'
        mysecret = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf."""
        self.assertEqual(mysecret,
                         vcode(mykey, mymessage))


if __name__ == '__main__':
    unittest.main()
