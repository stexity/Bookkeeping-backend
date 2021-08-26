from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """To create user with email instead of username"""
        if not email:
            raise ValueError("Invalid Email!!!")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        To Override the create_superuser method
        to create super user with email instead of username
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_verified = True
        user.is_active = True
        user.save()

        return user
