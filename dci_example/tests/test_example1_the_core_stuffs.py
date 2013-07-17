from unittest import TestCase
from example1_the_core_stuffs import Account

class TestAccount(TestCase):
    def test_withdraw_70_from_100(self):
        account = Account(100)
        account.withdraw(70)
        self.assertEqual(account.balance, 30)

