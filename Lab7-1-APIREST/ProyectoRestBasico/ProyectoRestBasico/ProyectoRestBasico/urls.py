"""
URL configuration for ProyectoRestBasico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apiRestDemo.views import employeeview, employeeviewBD
from serialApp.views import student_list, student_detail
from cbvApp.views import StudentList, StudentDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', employeeview),
    path('employeesBD/', employeeviewBD),
    path('apistudents/', student_list),
    path('apistudents/<int:pk>/', student_detail),
     # api rest por clases
    path('apistudentsclase/', StudentList.as_view()),
    path('apistudentsclase/<int:pk>/', StudentDetail.as_view()),
]
