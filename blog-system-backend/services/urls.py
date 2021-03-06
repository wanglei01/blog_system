from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^getBlogDirList', views.getBlogDirList),
    url(r'^getMenuList', views.getMenuList),
    url(r'^saveBlog', views.saveBlog),
    url(r'^getBlogList', views.getBlogList),
    url(r'^getBlogDetail', views.getBlogDetail),
    url(r'^addMenu', views.addMenu),
    url(r'^editMenu', views.editMenu),

]