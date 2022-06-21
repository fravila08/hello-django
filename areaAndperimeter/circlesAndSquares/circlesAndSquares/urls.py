"""circlesAndSquares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from urllib import response
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def squeryRectangle(shape, calc, height=0, width=0):
    if calc== 'area':
        area=height*width
        area2=HttpResponse(area)
        return area2
    if calc== 'perimeter':
        perimeter=(height+width)*2
        perimeter2=HttpResponse(perimeter)
        return perimeter2
    
def squeryCircle(shape,calc, radius=0):
    response=HttpResponse('<h1>Hello</h1>')
    if radius== 0:
        response.status_code= 409
        return response
    if calc== 'area':
        area=(radius*radius)*3.14
        area2=HttpResponse(area)
        return area2
    if calc== 'perimeter':
        perimeter= 2*(radius*3.14)
        perimeter2=HttpResponse(perimeter)
        return perimeter2
    
            
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/<str:calc>/<int:height>/<int:width>/', squeryRectangle),
    path('circle/<str:calc>/<int:radius>/', squeryCircle)
]
