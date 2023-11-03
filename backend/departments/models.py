from django.db import models

# Create your models here.


class TypeOfDepartmentModel(models.Model):  # Model này thể hiện loại khoa
    type_name = models.CharField(unique=True, max_length=200)

    class Meta:
        db_table = "TypesOfDepartment"
        indexes = [
            models.Index(fields=["type_name"]),
        ]
        constraints = [
            models.UniqueConstraint(fields=['type_name'], name='unique_type_name'),

        ]

class DepartmentModel(models.Model):  # Model này thể hiện các trung tâm
    department_name = models.CharField(unique=True, max_length=200)
    department_code = models.CharField(unique=True, max_length=50)
    isCenterDepartment = models.BooleanField(default=False)
    typeOfDepartment_id = models.ForeignKey(
        TypeOfDepartmentModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name="typeOfDepartment_id",
        db_column="typeOfDepartment_id",
        verbose_name="Id của table TypesOfDepartment",
    )

    class Meta:
        db_table = "Departments"
        indexes = [
            models.Index(fields=["typeOfDepartment_id", "department_code"]),
        ]

        constraints = [
            models.UniqueConstraint(fields=['department_name'], name='unique_department_name'),
            models.UniqueConstraint(fields=['department_code'], name='unique_department_code'),
        ]

class RoomDepartmentModel(
    models.Model
):  # Model này thể hiện khoa đó có phải nằm trong trung tâm không và loại khoa của nó là gì
    department_id = models.ForeignKey(
        DepartmentModel,
        on_delete=models.CASCADE,
        related_name="department_id",
        db_column="department_id",
        verbose_name="Id của table Departments",
    )
    roomDepartment_code = models.CharField(unique=True, max_length=50, null=True)
    roomDepartment_name = models.CharField(unique=True, max_length=200)

    class Meta:
        db_table = "RoomDepartments"

        indexes = [
            models.Index(fields=["department_id", "roomDepartment_code"]),
        ]
        constraints = [
            models.UniqueConstraint(fields=['roomDepartment_name'], name='unique_roomDepartment_name'),
            models.UniqueConstraint(fields=['roomDepartment_code'], name='unique_roomDepartment_code'),
        ]