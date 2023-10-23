from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The username field must be set")
        username = self.normalize_email(username)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password, **extra_fields)


class Departments(models.Model):
    department_name = models.CharField(max_length=200, unique=True, null=False)

    class Meta:
        db_table = "Department"


class Rooms(models.Model):
    room_name = models.CharField(max_length=200, unique=False, null=False)
    department_id = models.ForeignKey(
        Departments, on_delete=models.CASCADE, db_column="department_id"
    )

    class Meta:
        db_table = "Rooms"


class Roles(models.Model):
    role_name = models.CharField(max_length=200, unique=True, null=False)

    class Meta:
        db_table = "Roles"


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    department_id = models.ForeignKey(
        Departments, on_delete=models.CASCADE, db_column="department_id"
    )
    role_id = models.ForeignKey(
        Roles, on_delete=models.SET_NULL, null=True, db_column="role_id"
    )
    objects = UserManager()
    USERNAME_FIELD = "username"

    class Meta:
        db_table = "Users"

    def get_full_name(self):
        # Define how to get the full name of the user (e.g., "John Doe")
        return f"{self.first_name}  {self.last_name}".strip()

    def get_short_name(self):
        # Define how to get the short name of the user (e.g., "John")
        return self.last_name.strip()

    def __str__(self):
        return self.username.strip()
