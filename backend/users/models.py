from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from departments.models import RoomDepartmentModel


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


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "username"

    class Meta:
        db_table = "Users"


class RoleModel(models.Model):
    role_name = models.CharField(unique=True, max_length=50)
    role_code = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = "Roles"
        constraints = [
            models.UniqueConstraint(fields=['role_name'], name='unique_role_name'),
            models.UniqueConstraint(fields=['role_code'], name='unique_role_code'),
        ]

class RoomDepartmentRoleUserModel(models.Model):
    user_id = models.OneToOneField(
        UserAccount,
        on_delete=models.CASCADE,
        related_name="user_id",
        db_column="user_id",
        verbose_name="Id của table Users",
    )
    roomDepartment_id = models.ForeignKey(
        RoomDepartmentModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name="roomDepartment_id",
        db_column="roomDepartment_id",
        verbose_name="Id của table RoomDepartments",
    )
    role_id = models.ForeignKey(
        RoleModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name="role_id",
        db_column="role_id",
        verbose_name="Id của table Roles",
    )
    canViewDashboard = models.BooleanField(default=False)
    canCreateTask = models.BooleanField(default=False)

    class Meta:
        db_table = "RoomDepartmentRoleUser"
        indexes = [
            models.Index(
                fields=[
                    "roomDepartment_id",
                    "role_id",
                    "canViewDashboard",
                    "canCreateTask",
                ]
            ),
        ]
