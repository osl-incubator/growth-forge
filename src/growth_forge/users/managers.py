# type: ignore
from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager

if TYPE_CHECKING:
    from growth_forge.users.models import User


class UserManager(DjangoUserManager['User']):
    """Custom manager for the User model."""

    def _create_user(
        self,
        email: str,
        password: str,
        **extra_fields,
    ) -> User:
        """
        Create and save a user with the given email and password.
        """
        if not email:
            msg = 'The given email must be set'
            raise ValueError(msg)
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email: str,
        password: str | None = None,
        **extra_fields,
    ):  # type: ignore[override]
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password)

    def create_superuser(
        self,
        email: str,
        password: str | None = None,
        **extra_fields,
    ):  # type: ignore[override]
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            msg = 'Superuser must have is_staff=True.'
            raise ValueError(msg)
        if extra_fields.get('is_superuser') is not True:
            msg = 'Superuser must have is_superuser=True.'
            raise ValueError(msg)

        return self._create_user(email, password, **extra_fields)
