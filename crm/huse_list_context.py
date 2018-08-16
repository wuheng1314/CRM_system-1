#coding=utf-8
from crm.models import HouseInfo


def GetHousE_list(request):
    house_list=HouseInfo.objects.all()
    return {'house_list':house_list}
#获取查询的信息

def GetLook_table(request):
    #获取所查列表信息
    queryType =HouseInfo.objects.values("")
