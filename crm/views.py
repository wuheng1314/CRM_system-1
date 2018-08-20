# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from crm.models import UserInfo,HouseType,HouseInfo


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
