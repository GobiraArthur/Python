from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurante_app.urls'),name='restaurante'),
    path('api/', include('api_app.urls')),    
]
