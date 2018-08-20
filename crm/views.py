# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
import jsonpickle
from django.core import serializers
from django.urls import reverse

from crm.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View



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

#贾漂亮
# 添加房屋类型
def dem_index(request):
        t = request.GET.get('houseTypeName','')
        if t:
            try:
                housename=HouseType.objects.get(type_name=t,)
                return HttpResponse('已存在')
            except HouseType.DoesNotExist:
                housename=HouseType.objects.create(type_name=t,is_used=1)
                return HttpResponseRedirect('/crm/dem1/')
        return HttpResponse('数据不能为空')


def dem1_index(request):
    housenamelist=HouseType.objects.filter()
    return render(request,'house_type_list.html',{'housenamelist':housenamelist})

# 删除房屋类型
def dem2_index(request,pk):
    t=HouseType.objects.filter(type_id=pk)
    t.delete()
    return HttpResponseRedirect('/crm/dem1/')

# 添加客户来源
class Dev(View):
    def get(self,request):
        return render(request,'customer_source_list.html')
    def post(self,request):
        s=request.POST.get('SourceName')
        if s:
            try:
                CustomerSource.objects.get(source_name=s)
                return HttpResponse('已存在')
            except CustomerSource.DoesNotExist:
                CustomerSource.objects.create(source_name=s,is_used=1)
                return HttpResponseRedirect('/crm/dev1')
        return HttpResponse('数据不能为空')

# 删除客户来源
def dev1_index(request):
    sourcenamelist=CustomerSource.objects.filter()
    return render(request,'customer_source_list.html',{'sourcenamelist':sourcenamelist})
def dev2_index(request,pk):
    t=CustomerSource.objects.filter( source_id =pk)
    print t
    t.delete()
    return HttpResponseRedirect('/crm/dev1/')


class Care(View):
    def  get(self,request):

        return render(request,'customer_care_list.html')
    def post(self,request):
        s = request.POST.get('')
        if s:
            try:
                CustomerSource.objects.get(source_name=s)
                return HttpResponse('已存在')
            except CustomerSource.DoesNotExist:
                CustomerSource.objects.create(source_name=s, is_used=1)
                return HttpResponseRedirect('/crm/dev1')
        return HttpResponse('数据不能为空')

#安不丑

#房屋信息的添加安
class HouseList(View):
    def get(self,request):
        return render(request,'houselist_add.html',)
    def post(self,request):
        #接收请求参数
        abc=request.POST
        username=request.POST.get('username',)
        username=UserInfo.objects.get(user_id=username)

        house_type=request.POST.get('type',)
        house_type=HouseType.objects.get(type_id=house_type)

        houseaddr=request.POST.get('houseaddr',)

        house_price=request.POST.get('house_price','')

        house_en=request.POST.get('house_en','')

        if  house_price and house_en and houseaddr:
            HouseInfo.objects.create( user=username,type=house_type,house_address=houseaddr,house_price=house_price,house_ambient=house_en)
            abc="添加成功，加油！请继续添加"
            return render(request,'houselist_add.html',{'abc':abc})
        efg='添加失败，数据不能为空,请重新添加'
        return render(request,'houselist_add.html',{'efg':efg})

#房屋信息的查询 可以模糊查询安
class HouseQueryServlet(View):
    def get(self,request):
       return render(request,'house_list.html')
    def post(self,request):
        #获取查询的方式的值
        queryType=request.POST.get('queryType')
        queryType=int(queryType)
        # #获取用户输入的字段
        houseInput=request.POST.get('houseInput','')
        #如果值等于1则根据房屋类型进行查询
        if queryType==1:
             if houseInput:
                 houselist= [i.houseinfo_set.all() for i in HouseType.objects.filter(type_name__contains=houseInput)]
                 return render(request,'house_list.html',{'house_list':houselist[0]})
             else:
                 return render(request,'house_list.html')
        elif queryType==2:
            if houseInput:
                houselist=HouseInfo.objects.filter(house_price__range=(int(houseInput)-100,int(houseInput)+100)).all()
                for house in houselist:
                    print  house.house_id
                return render(request, 'house_list.html', {'house_list': houselist})
            else:
                return render(request, 'house_list.html')

#房屋信息的删除，关键字传参安
def DeleteServlet_view(request,b):
    HouseInfo.objects.filter(house_id=b).delete()

    return render(request,'house_list.html')

#修改页面安
class UpdateServlet(View):
    def get(self,request):
       c = int(request.GET.get('num'))
       print c
       houseinfo=HouseInfo.objects.filter(house_id=c)
       return render(request,"houselist_adm.html",{'houseinfo':houseinfo[0]})
    def  post(self,request):
        re = request.POST
        houset = HouseInfo.objects.filter(house_id=int(request.POST.get('id'))).update(type=re['type'], user=re['username'], house_address=re['houseaddr'], house_price=re['house_price'],house_ambient=re['house_en'])
        print houset
        return render(request, "house_list.html")
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

