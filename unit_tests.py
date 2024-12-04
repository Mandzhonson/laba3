import unittest
from main import match_snils,find_snils_in_file,find_snils_on_site


class test_snils_functions(unittest.TestCase):

    def test_valid_match_snils(self):
        self.assertTrue(match_snils("123-233-111 00"))
        self.assertTrue(match_snils("123-567-541 55"))
        self.assertTrue(match_snils("999-999-999 99"))
        self.assertTrue(match_snils("000-000-000 00"))
        self.assertTrue(match_snils("222-222-222 22"))
    def test_invalid_match_snils(self):
        self.assertFalse(match_snils("12345678910"))
        self.assertFalse(match_snils("MISHAMANZHOS"))
        self.assertFalse(match_snils(""))
        self.assertFalse(match_snils("999-999-9992 00"))
        self.assertFalse(match_snils("999-9992-999 00"))
        self.assertFalse(match_snils("9992-999-999 00"))
        self.assertFalse(match_snils("9992-9992-9992 00"))

if __name__=="__main__":
    unittest.main()