from django.test import TestCase
import random
from django.contrib.auth.password_validation import validate_password
# Create your tests here.
from .models import *


class TestUsers(TestCase):
    role  = [
        {'role_name':"Giám đốc Bệnh viện",'role_code':'gdbv'},
        {'role_name':"Giám đốc Trung tâm",'role_code':'gdtt'},
        {'role_name':"Nhân viên",'role_code':'nv'},
]
    for i in role:
        try:
            RoleModel(**i).save()
        except:
            pass
    try:
        a = UserAccount(username='toanh',first_name="to",last_name="anh")
        a.set_password("toanh")
        a.save()
    except:
        pass