from django.test import TestCase
from .models import TypeOfDepartmentModel, DepartmentModel, RoomDepartmentModel
import random


# Create your tests here.
class TestDepartment(TestCase):
    typeOfDepartment = [
        "Cận lâm sàng",
        "Hệ nội",
        "Hệ ngoại",
        "Cấp cứu",
        "Khoa khám bệnh",
        "Chất lượng cao",
    ]
    deparment = [
        {
            "department_name": "Trung tâm Tim mạch",
            "department_code": "TTTM",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Đột quỵ",
            "department_code": "TTDQ",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Y, dược cổ truyền - Phục hồi chức năng",
            "department_code": "TTYDCT-PHCN",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Thận - Lọc máu",
            "department_code": "TTT-LM",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Ung bướu",
            "department_code": "TTUB",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Huyết học - Truyền máu",
            "department_code": "TTHH-TM",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Xét nghiệm",
            "department_code": "TTXN",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Trung tâm Khám chữa bệnh chất lượng cao",
            "department_code": "TTKCB-CLC",
            "isCenterDepartment": True,
        },
        {
            "department_name": "Khoa cap cuu",
            "department_code": "kcc",
            "isCenterDepartment": False,
        },
    ]
    role = {
        1
    }
    def checkDepartmentdepartment_code_dup(self):
        for i in range(len(self.deparment) - 1):
            for j in range(i + 1, len(self.deparment)):
                if (
                    self.deparment[i]["department_code"]
                    == self.deparment[j]["department_code"]
                ):
                    return False
        return True

    # insert to TypeOfDepartmentModel
    distinctType = [x for x in set(typeOfDepartment)]
    for i in distinctType:
        try:
            TypeOfDepartmentModel.objects.create(type_name=i)
        except:
            continue

    # insert to departmentModel

    for i in deparment:
        try:
            obj = DepartmentModel(
                **i,
                typeOfDepartment_id=TypeOfDepartmentModel.objects.get(
                    type_name=random.choice(
                        [
                            "Cận lâm sàng",
                            "Hệ nội",
                            "Hệ ngoại",
                        ]
                    )
                )
            )
            obj.save()
        except:
            continue
