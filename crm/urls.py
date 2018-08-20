from django.conf.urls import url, include

from crm import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^index/$', views.index),
    url(r'^houselist/$', views.HouseList.as_view()),
    url(r'^HouseQueryServlet/$', views.HouseQueryServlet.as_view()),
    url(r'^HouseDeleteServlet/(?P<b>\d.*)/$',views.DeleteServlet_view),
    url(r'^HouseUpdateServlet/$',views.UpdateServlet.as_view()),

    url(r'^(.*?)/$', views.others),
]
