from django.core import serializers
from jsonpickle import json

from crm.models import *


def noticeList(request):
    list1 = NoticeInfo.objects.all().order_by('-notice_time')
    return {
        'noticeList':list1
    }
def deptList(request):
    list1 = DepartmentInfo.objects.all().order_by('-department_id')
    return {
        'deptList': list1
    }
def roleList(request):
    list1 = UserRole.objects.all().order_by('role_power')
    list2 = CustomerInfo.objects.all()
    return {
        'roleList':list1,'customerList':list2
    }
def userList(request):
    list1 = UserInfo.objects.all()
    list1 = serializers.serialize('json',list1)
    return {
        'userList':list1
    }
def userNameList(request):
    list1 = UserInfo.objects.all()
    list2 = []
    for i in list1:
        list2.append(i.user_name)
    list2 = json.dumps(list2)
    # list2= serializers.serialize('json',list2)
    return {
        'userNameList':list2
    }
def customerList(request):
    list1 = CustomerInfo.objects.all()
    return {
        'customerList':list1
    }