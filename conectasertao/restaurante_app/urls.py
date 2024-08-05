from django.urls import path
from restaurante_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('newuser/', views.newuser, name='newuser'),
    path('deluser/<id>', views.deluser, name='deluser'),
    path('editperfil/', views.editperfil, name='editperfil'),
]
