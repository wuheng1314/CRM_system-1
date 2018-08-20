from django.conf.urls import url, include

from crm import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^index/$', views.index),
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
