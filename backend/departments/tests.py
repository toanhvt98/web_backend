from django.test import TestCase
from .models import TypeOfDepartmentModel, DepartmentModel, RoomDepartmentModel


# Create your tests here.
class TestDepartment(TestCase):
    typeOfDepartment = ["noi", "ngoai", "clc", "cap cuu"]
    departments = {
        "noi": {"ten": "Khoa ung bướu", "isCenterDepartment": False, "code": "kub"},
        "ngoai": {"ten": "Khoa ngoại soi", "isCenterDepartment": False, "code": "kns"},
        "clc": {
            "ten": "Trung tâm khám chữ bệnh chất lượng cao",
            "isCenterDepartment": True,
            "code": "ttclc",
            "room": [
                {"ten": "khoa kham benh1", "code": "kkb1"},
                {"ten": "khoa kham benh2", "code": "kkb2"},
                {"ten": "khoa kham benh3", "code": "kkb3"},
            ],
        },
        "cap cuu": {"ten": "Khoa cấp cứu", "isCenterDepartment": False, "code": "kcc"},
    }

    for i in typeOfDepartment:
        type = TypeOfDepartmentModel.objects.create(type_name=i)
        for j in departments:
            try:
                DepartmentModel.objects.create(
                    typeOfDepartment_id=type,
                    department_name=departments[j]["ten"],
                    department_code=departments[j]["code"],
                    isCenterDepartment=departments[j]["isCenterDepartment"],
                )
            except:
                pass

    for i in departments:
        if departments[i]["isCenterDepartment"]:
            department = DepartmentModel.objects.get(
                department_code=departments[i]["code"]
            )
            try:
                if len(departments[i]["room"]) > 0:
                    for j in departments[i]["room"]:
                        RoomDepartmentModel.objects.create(
                            department_id=department,
                            roomDepartment_code=j["code"],
                            roomDepartment_name=j["ten"],
                        )
            except:
                pass
