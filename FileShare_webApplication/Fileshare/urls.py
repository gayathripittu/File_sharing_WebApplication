from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('upload', views.upload, name='upload'),
    path('fileview', views.fileview, name='fileview'),
    path('result', views.result, name='result'),
    path('uploaddetails', views.uploaddetails, name='uploaddetails'),
    path('file_upload', views.file_upload, name='file_upload'),
    path('logout', views.logout, name='logout'),
]