# coding=utf-8

from django.conf.urls import url, include

from crm import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^index/$', views.index),
    # 小贾
    url(r'^dem/$', views.dem_index),

    url(r'^dem1/$',views.dem1_index),
    url(r'^dem2/(?P<pk>\d+)/$',views.dem2_index),
    url(r'^dev/$',views.Dev.as_view()),
    # 客户关怀添加
    url(r'^care_add/$',views.Care.as_view()),

    url(r'^dev1/$',views.dev1_index),
    url(r'^dev2/(?P<pk>\d+)/$',views.dev2_index),


    url(r'^(.*?)/$', views.others),
    # url(r'^dem/$', views.dem_index),

    #安雪男
    url(r'^houselist/$', views.HouseList.as_view()),
    url(r'^HouseQueryServlet/$', views.HouseQueryServlet.as_view()),
    url(r'^HouseDeleteServlet/(?P<b>\d.*)/$',views.DeleteServlet_view),
    url(r'^HouseUpdateServlet/$',views.UpdateServlet.as_view()),
     #陈子鹏
    url(r'^index/getuser/$', views.getUser),
    url(r'^index/noticeDel/(\d*)/$', views.noticeDel),
    url(r'^index/noticeAdd/$', views.noticeAdd),
    url(r'^index/noticeQuery/$', views.noticeQuery),
    url(r'^index/get_userNum/$', views.get_userNum),
    url(r'^index/userAdd/$', views.userAdd),
    url(r'^index/roleAdd/$', views.roleAdd),
    url(r'^index/userRoleDel/$', views.userRoleDel),
    url(r'^index/departmentAdd/$', views.departmentAdd ,name= 'departmentAdd'),
    url(r'^index/departmentDel/$', views.departmentDel,name= 'departmentDel'),
    url(r'^(.*?)/$', views.others),
    ]

