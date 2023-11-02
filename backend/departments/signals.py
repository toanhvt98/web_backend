# actions.py

from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=DepartmentModel)
def create_room_department_for_department(sender, instance, **kwargs):
    if not instance.isCenterDepartment:
        RoomDepartmentModel.objects.create(
            department_id=instance,
            roomDepartment_code=instance.department_code,
            roomDepartment_name=instance.department_name,
        )
