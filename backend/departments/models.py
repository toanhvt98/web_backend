from django.db import models

# Create your models here.


class TypeOfDepartmentModel(models.Model): # Model này thể hiện loại khoa
    type_name = models.CharField(unique=True, max_length=200)

    class Meta:
        db_table = "TypeOfDepartment"


class DepartmentModel(models.Model): # Model này thể hiện các trung tâm
    department_name = models.CharField(unique=True, max_length=200)
    department_code = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = "Department"


class RoomDepartmentModel(models.Model): # Model này thể hiện khoa đó có phải nằm trong trung tâm không và loại khoa của nó là gì
    typeOfDepartment_id = models.ForeignKey(
        TypeOfDepartmentModel,
        on_delete=models.CASCADE,
        related_name="typeOfDepartment_id",
    )
    department_id = models.ForeignKey(
        DepartmentModel, on_delete=models.SET_NULL,null=True,default=True, related_name="department_id"
    )
    roomDepartment_code = models.CharField(unique=True, max_length=50)
    roomDepartment_name = models.CharField(unique=True, max_length=200)

    class Meta:
        db_table = "RoomDepartment"
