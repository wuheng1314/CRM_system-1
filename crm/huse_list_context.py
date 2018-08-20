#coding=utf-8
from crm.models import *

#安子
def GetHousE_list(request):
    house_list=HouseInfo.objects.all()
    return {'house_list':house_list}

#获取用户信息传送给houselist_add.html页面用于添加用户信息
def GetUserInfo(request):
    user_list=UserInfo.objects.all()
    return {'user_list':user_list}
#获取房屋类型送给houselist_add.html页面用于添加房屋类型
def GetHouseType(request):
    house_type_list=HouseType.objects.all()
    return {'house_type_list':house_type_list}

