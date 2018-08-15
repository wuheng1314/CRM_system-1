# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
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