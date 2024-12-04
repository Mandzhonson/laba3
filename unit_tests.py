import unittest
import os
from main import match_snils, find_snils_in_file, find_snils_on_site


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

    def test_find_in_file(self):
        # проверка работы регулярного выражения в файле
        test_filename = "check_snils.txt"
        with open(test_filename, "w", encoding="utf-8") as file:
            file.write("123-456-789 01\n")
            file.write("000-000-000 00\n")
            file.write("9992-9992-9992 00\n")
            file.write("666-666-666 36\n")
        search_snils = find_snils_in_file(test_filename)
        self.assertEqual(
            search_snils, ["123-456-789 01", "000-000-000 00", "666-666-666 36"])
        os.remove(test_filename)

    def test_find_on_site(self):
        # проверим работу функции поиска снилса из сайта
        arr = find_snils_on_site()[:5] # возьмем первые 5 снилсов из сайта(мы заранее знаем,что они верны)
        self.assertEqual(arr, ["176-925-428 13", "196-624-640 09",
                         "169-130-191 62", "150-685-127 58", "160-090-318 20"])


if __name__ == "__main__":
    unittest.main()
