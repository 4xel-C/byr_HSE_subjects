import unittest
from unittest.mock import patch
from menu import select_quarter, select_generation_method


class Test(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_select_quarter(self, mock_input):
        self.assertEqual(select_quarter(), 1)

    @patch("builtins.input", side_effect=["5"])
    def test_select_quarter_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            select_quarter()

    @patch("builtins.input", side_effect=["abc", "7", "2  "])
    def test_select_quarter_invalid_then_valid(self, mock_input):
        self.assertEqual(select_quarter(), 2)

    @patch("builtins.input", side_effect=["1"])
    def test_select_generation_method(self, mock_input):
        self.assertEqual(select_generation_method(1), "auto function")

    @patch("builtins.input", side_effect=["2"])
    def test_select_generation_method_manual(self, mock_input):
        self.assertEqual(select_generation_method(1), "manual function")

    @patch("builtins.input", side_effect=["sdqfkjh", "76", "3  "])
    def test_select_generation_method_invalid_then_valid(self, mock_input):
        self.assertEqual(select_generation_method(1), "back")

    @patch("builtins.input", side_effect=["4"])
    def test_select_generation_method_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            select_generation_method(1)


# run the tests
if __name__ == "__main__":
    unittest.main()
