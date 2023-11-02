from django.test import TestCase
from .models import TypeOfDepartmentModel, DepartmentModel, RoomDepartmentModel


# Create your tests here.
class TestDepartment(TestCase):

    typeOfDepartment = ["Cận lâm sàng", "Hệ nội","Hệ ngoại","Cấp cứu","Khoa khám bệnh","Chất lượng cao"]
    deparment = [
        {"department_name":"Trung tâm Tim mạch","department_code":"tttm"},
        {"department_name":"Trung tâm Đột quỵ","department_code":"ttdq"},
        {"department_name":"Trung tâm Y, dược cổ truyền - Phục hồi chức năng","department_code":"ttydct-phcn"},
        {"department_name":"Trung tâm Thận - Lọc máu","department_code":"ttt-lm"},
        {"department_name":"Trung tâm Ung bướu","department_code":"ttub"},
        {"department_name":"Trung tâm Huyết học - Truyền máu","department_code":"tthh-tm"},
        {"department_name":"Trung tâm Xét nghiệm","department_code":"ttxn"},
        {"department_name":"Trung tâm Khám chữa bệnh chất lượng cao","department_code":"ttkcbclc"},
    ]


    def checkDepartmentdepartment_code_dup(self):
        for i in range(len(self.deparment)-1):
            for j in range(i+1,len(self.deparment)):
                if self.deparment[i]['department_code']==self.deparment[j]['department_code']:
                    return False
        return True
    
    # insert to departmentModel
    if checkDepartmentdepartment_code_dup:
        for i in deparment:
            try:
                obj = DepartmentModel(**i)
                obj.save()
            except:
                continue
    
    # insert to TypeOfDepartmentModel
    distinctType = [x for x in set(typeOfDepartment)]
    for i in distinctType:
        try:
            TypeOfDepartmentModel.objects.create(type_name=i)
        except:
            continue