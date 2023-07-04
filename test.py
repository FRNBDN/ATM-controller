import unittest
from run import (
    validate_card_nr,
    verify_pin,
    fetch_accounts_data,
    deposit,
    withdraw,
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

    def test_fetch_accounts_data_valid(self):
        card_number = "3456789034567890"
        expected_accounts = [
            {"Name": "Checking", "Balance": 1500},
            {"Name": "Savings", "Balance": 20000},
        ]
        expected_owner = "Michael Brown"
        result = fetch_accounts_data(card_number)
        self.assertEqual(result[0], expected_accounts)
        self.assertEqual(result[1], expected_owner)

    def test_deposit_valid_amount(self):
        account = {"Name": "Checking", "Balance": 1500}
        value_deposited = 100
        deposit(account, value_deposited)
        self.assertEqual(account["Balance"], 1600)

    def test_deposit_invalid_amount(self):
        account = {"Name": "Checking", "Balance": 1500}
        value_deposited = -100
        self.assertRaises(ValueError, deposit, account, value_deposited)
        self.assertEqual(account["Balance"], 1500)

    def test_withdraw_valid_amount(self):
        account = {"Name": "Checking", "Balance": 1500}
        value_withdrawn = 200
        withdraw(account, value_withdrawn)
        self.assertEqual(account["Balance"], 1300)

    def test_withdraw_invalid_amount(self):
        account = {"Name": "Checking", "Balance": 1500}
        value_withdrawn = -100
        self.assertRaises(ValueError, withdraw, account, value_withdrawn)
        self.assertEqual(account["Balance"], 1500)

    def test_withdraw_insufficient_funds(self):
        account = {"Name": "Checking", "Balance": 1500}
        value_withdrawn = 2000
        self.assertRaises(ValueError, withdraw, account, value_withdrawn)
        self.assertEqual(account["Balance"], 1500)


if __name__ == "__main__":
    unittest.main()
