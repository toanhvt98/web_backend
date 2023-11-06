# actions.py

from .models import *
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver


@receiver(post_save, sender=DepartmentModel)
def create_room_department_for_department(sender, instance, **kwargs):
    RoomDepartmentModel.objects.create(
        department_id=instance,
        roomDepartment_code=instance.department_code,
        roomDepartment_name=instance.department_name,
    )
@receiver(pre_save, sender=DepartmentModel)
def upper_department_code(sender, instance, **kwargs):
    instance.department_code = instance.department_code.upper()
    
@receiver(pre_save, sender=RoomDepartmentModel)
def upper_department_code(sender, instance, **kwargs):
    instance.roomDepartment_code = instance.roomDepartment_code.upper()
