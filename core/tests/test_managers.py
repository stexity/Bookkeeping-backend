from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager


class ManagersTests(TestCase):

    def test_create_user_with_valid_data_successfully(self):
        """Test thet create user with valid credentials successfully"""
        data = {
            'email': 'test@finance.com',
            'password': 'test@1233',
            'name': 'Test'
        }
        user = get_user_model().objects.create_user(**data)

        self.assertEquals(user.email, data['email'])
        self.assertTrue(user.check_password(data['password']))

    def test_new_user_email_normalized(self):
        """Test to check the email of new user is normalized"""
        data = {
            'email': 'test@FINANCE.COM',
            'password': 'test@1233',
            'name': 'Test'
        }
        user = get_user_model().objects.create_user(**data)

        self.assertEqual(
            user.email, BaseUserManager.normalize_email(data['email'])
        )

    def test_create_superuser_with_valid_data_successfully(self):
        """Test that create superuser with valid data successfully"""
        super_user = get_user_model().objects.create_superuser(
            email='admin@FINANCE.COM',
            password=None
        )

        self.assertTrue(super_user.is_staff)
