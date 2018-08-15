from django.conf.urls import url, include

from crm import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^index/$', views.index),
    url(r'^(.*\..*)/$', views.others),
]
