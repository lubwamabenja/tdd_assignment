import unittest
from register import User_Accounts

class TestUserAccount(unittest.TestCase):
    def setUp(self):
        self.account = User_Accounts()
        self.email = "lubwama73@gmail.com"
        self.password = "Lubwama1!"
        self.username = "Benja"
        self.name = "Lubwama"
        self.age = 100

        self.existing_account = dict(
            username = self.username,            
            email = self.email,
            age = self.age,
            password = self.password
        )

    def test_isntantiation(self):
        self.assertIsInstance(self.account, User_Accounts)

    def test_email_validity(self):
        self.assertTrue(self.account.verify_email(self.email))

    def test_password_validity(self):
        self.assertTrue(self.account.verify_password(self.password))
        self.assertFalse(self.account.verify_password("IsaacBenja"))

    def test_username_validity(self):
        self.assertTrue(self.account.verify_username(self.username, self.name))

    def test_age_validity(self):
        self.assertTrue(self.account.verify_age(self.age))
        self.assertFalse(self.account.verify_age(0))

    def test_user_can_register(self):
        self.assertEqual(len(self.account.users), 0)
        self.account.register_user(self.name, **self.existing_account)
        self.assertEqual(len(self.account.users), 1)

    def test_duplicate_users(self):
        self.account.register_user(self.name, **self.existing_account)
        self.assertFalse(self.account.register_user(self.name, **self.existing_account))

    def test_user_can_login(self):
        self.account.register_user(self.name, **self.existing_account)
        self.assertTrue(self.account.login(self.username, self.password))
        self.assertFalse(self.account.login("lubwama", "benja"))
