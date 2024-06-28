from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'secret_password',
            "first_name": "test",
            "last_name": "test",
            "role": "user"
        }

    def test_user_creation(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        # Add more assertions if needed for other fields

    def test_user_email_unique(self):
        User.objects.create_user(**self.user_data)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.user_data)

    def test_user_without_username(self):
        del self.user_data['username']
        with self.assertRaises(ValueError):
            User.objects.create_user(**self.user_data)