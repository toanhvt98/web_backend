from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import RoleModel

@receiver(pre_save,sender=RoleModel)
def upper_role_code(sender,instance,**kwargs):
    instance.role_code = instance.role_code.upper()