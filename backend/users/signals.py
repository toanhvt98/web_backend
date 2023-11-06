from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import RoleModel,UserAccount,RoomDepartmentRoleUserModel

@receiver(pre_save,sender=RoleModel)
def upper_role_code(sender,instance,**kwargs):
    instance.role_code = instance.role_code.upper()

@receiver(post_save,sender=UserAccount)
def create_RoomDepartmentRoleUserModel_for_UserAccount(sender,instance,**kwargs):
    RoomDepartmentRoleUserModel.objects.create(user_id=instance,roomDepartment_id=None,role_id=None,canViewDashboard=False,canCreateTask=False)
    