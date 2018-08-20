# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from crm.models import UserInfo, HouseType, CustomerSource


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


