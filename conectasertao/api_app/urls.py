from django.urls import path
from api_app import views

urlpatterns = [
    path('categoria/', views.categoria,),
    path('categoria', views.categoria_id),
]
