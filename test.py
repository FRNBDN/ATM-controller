import unittest
from run import (
    validate_card_nr,
    verify_pin,
)


class TestATMController(unittest.TestCase):
    def test_validate_card_nr_valid(self):
        card_number = "3456789034567890"
        result = validate_card_nr(card_number)
        self.assertEqual(result, card_number)

    def test_validate_card_nr_invalid(self):
        card_number = "3456123434567890"
        result = validate_card_nr(card_number)
        self.assertIsNone(result)

    def test_verify_pin_valid(self):
        card_number = "3456789034567890"
        pin = "9876"
        result = verify_pin(card_number, pin)
        self.assertTrue(result)

    def test_verify_pin_invalid(self):
        card_number = "3456789034567890"
        pin = "1234"
        result = verify_pin(card_number, pin)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
