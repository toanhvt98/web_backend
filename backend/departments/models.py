from django.db import models

# Create your models here.

class TypeOfDepartmentModel(models.Model):
    type_name = models.CharField(unique=True,max_length=200)

    class Meta:
        db_table = "TypeOfDepartment"

class DepartmentModel(models.Model):
    typeOfDepartment_id = models.ForeignKey(TypeOfDepartmentModel,on_delete=models.CASCADE,related_name="typeOfDepartment_id")
    department_name = models.CharField(unique=True,max_length=200)
    isCenterDepartment = models.BooleanField(default=True)

    class Meta:
        db_table = "Department"

class RoomDepartmentModel(models.Model):
    department_id = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,related_name="department_id")
    roomDepartment_name = models.CharField(unique=True,max_length=200)

    def save(self, *args, **kwargs):
        if self.department_id.isCenterDepartment:
            self.roomDepartment_name = self.department_id.department_name
        super(RoomDepartmentModel, self).save(*args, **kwargs)
    class Meta:
        db_table = "RoomDepartment"