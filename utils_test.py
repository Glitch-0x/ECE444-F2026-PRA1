import unittest
from utils import utils

class TestUtils(unittest.TestCase):

    # --- Tests for reversed() ---
    
    def test_reversed_integer(self):
        """tests 'reversed' with Integern."""
        self.assertEqual(utils.reversed(1234), 4321)
        self.assertEqual(utils.reversed(-567), -765)
        self.assertEqual(utils.reversed(1000), 1)

    def test_reversed_string(self):
        """tests 'reversed' with Strings (should cause TypeError)."""
        with self.assertRaises(TypeError):
            utils.reversed("1234")

    def test_reversed_float(self):
        """Testet 'reversed' with floats (should cause TypeErrorauslösen)."""
        with self.assertRaises(TypeError):
            utils.reversed(12.34)

    # --- Tests for formatter() ---

    def test_formatter_integer(self):
        """tests 'formatter' with Integern."""
        # 10 in binary is '0b1010', in octal '0o12'
        self.assertEqual(utils.formatter(10), ('0b1010', '0o12'))
        self.assertEqual(utils.formatter(0), ('0b0', '0o0'))

    def test_formatter_string(self):
        """tests 'formatter' with Strings (should cause TypeError)."""
        with self.assertRaises(TypeError):
            utils.formatter("10")

    def test_formatter_float(self):
        """tests 'formatter' with Floats (should cause TypeError)."""
        with self.assertRaises(TypeError):
            utils.formatter(10.5)

if __name__ == '__main__':
    unittest.main()