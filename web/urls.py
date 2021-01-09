from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('', views.lgin,name="login"),
    path('signup', views.signup,name="signup"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('learn', views.learn,name="learn"),
    path('cp', views.cp,name="cp"),
    path('editor', views.editor,name="editor"),
    path('logout', views.lgout,name="logout"),
]