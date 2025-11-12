import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("hugo carcamo")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(200)
        self.assertEqual(self.account.get_balance(), 200)

    def test_withdraw(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 300)

    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

    def test_sequence_of_transactions(self):
        self.account.deposit(1000)
        self.account.withdraw(250)
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 1050)


if __name__ == "__main__":
    unittest.main()
