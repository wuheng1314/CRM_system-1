# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jsonpickle
from django.core import serializers
from django.urls import reverse

from crm.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from crm.models import UserInfo


def login(request):

    return render(request,'login.html')

def index(request):
    
    return render(request,'main.html')


def others(request,addr):
    return render(request,addr)


class Login(View):

    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        userNum = request.POST.get('userNum')
        userPw = request.POST.get('userPw')
        if not UserInfo.objects.filter(user_num=userNum,user_pw=userPw):
            return render(request, 'login.html',{'flag': 1 })
        return render(request, 'main.html')


def main(request,addr):
    return render(request, 'main.html',{'addr':addr})


def noticeDel(request,num):
    num = int(num)
    NoticeInfo.objects.filter(notice_id = num).delete()
    return render(request,'notice_list.html')


def noticeAdd(request):
    user = request.POST.get('user','')
    user = UserInfo.objects.filter(user_name = user)[0]
    if not user:
        return  HttpResponseRedirect('/crm/notice_add.html/')
    notice_item = request.POST.get('notice_item')
    notice_content = request.POST.get('notice_content')
    notice_time = request.POST.get('notice_time')
    notice_endtime = request.POST.get('notice_endtime')
    NoticeInfo.objects.create(user=user,notice_content=notice_content,notice_endtime=notice_endtime,notice_time=notice_time,notice_item=notice_item)
    return HttpResponseRedirect('/crm/notice_list.html')

def getUser(request):
    user = request.GET.get('user')
    result = UserInfo.objects.filter(user_name=user)
    # result=jsonpickle.dumps(result)
    # result=serializers.serialize('json',result)
    print result
    result = None if len(result) == 0 else 1
    return JsonResponse({'result':result})


def noticeQuery(request):
    flag = int(request.POST.get('queryType',''))
    word = request.POST.get('noticeInput','')
    if flag == 1 :
        noticeList=NoticeInfo.objects.filter(notice_item__contains=word)
    elif flag == 2:
        noticeList = NoticeInfo.objects.filter(notice_content__contains=word)
    else:
        noticeList = []
    print noticeList
    return render(request,'notice_list.html',{'noticeList':noticeList})


def departmentAdd(request):
    department_name = request.POST.get("departmentName",'')
    department_desc = request.POST.get("departmentDesc",'')
    list1 = ['',None]
    flag = {}
    if department_desc in list1 or department_name in list1:
        flag['项目不能为空'] = -1
        return render(request, 'dept_add.html', {'flag': flag})
    try:
        dep = DepartmentInfo.objects.get(department_name=department_name.encode(encoding='UTF-8'))
        flag['已存在此部门'] = 1
        return render(request, 'dept_add.html', {'flag': flag})
    except:
        dep = DepartmentInfo.objects.create(department_name=department_name,department_desc=department_desc,is_used = 1)
        flag['添加成功']= 2
        return render(request,'dept_add.html',{'flag':flag})


def departmentDel(request):
    department_id = request.GET.get('id')
    try:
        userList = UserInfo.objects.filter(department_id = department_id)
        departmentList = DepartmentInfo.objects.filter(department_id=department_id)
        for i in departmentList:
            i.userinfo_set.clear()
        DepartmentInfo.objects.filter(department_id=int(department_id)).delete()
    except Exception as e:
        return HttpResponse(e)
    return render(request,'dept_add.html')


def get_userNum(request):
    num = request.GET.get('num')
    l1 = UserInfo.objects.filter(user_num=num)
    num1 = True if len(l1) == 0 else False
    return JsonResponse({'res':num1})


def userAdd(request):
    fieldsDict = request.POST
    fieldsDict = fieldsDict.items()
    dict1 = {}
    try:
        for i,j in fieldsDict:
            if i == 'department':
                j = DepartmentInfo.objects.get(department_id = j)
            if i == 'role':
                j = UserRole.objects.get(role_id= j)
            if i not in ['csrfmiddlewaretoken']:
                dict1[i] = j
        UserInfo.objects.create(is_used = 1,**dict1)
        return render(request,'emp_add.html',{'flag3': 1})
    except:
        return render(request, 'emp_add.html', {'flag3': 0})


def roleAdd(request):
    powerDict = {'太阳':-5,'月亮':0,'一星':1,'两星':2,'三星':3,}
    roleNameList = [role.role_name for role in UserRole.objects.all()]
    roleName = request.POST.get('roleName')
    if roleName in ['',None]:
        return render(request, 'role_add.html', {'flag': -1})
    if roleName in roleNameList:
        return render(request, 'role_add.html', {'flag': 0})
    rolePower = request.POST.get('rolePower')
    try:
        UserRole.objects.create(role_name = roleName,role_power = rolePower,is_used = 1)
        return render(request,'role_add.html',{'flag':1})
    except:
        return HttpResponse('出现问题')


def userRoleDel(request):
    num = request.GET.get('num')
    try:
        UserRole.objects.filter(role_id=num).delete()
    except:
        return render(request, 'role_add.html',{'flag':-2})
    return render(request,'role_add.html')