"""
URL configuration for Hospital_Management_System project.

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
from django.urls import path , include
from Patients import views as p
from Doctors import views as d
from Administration import views as a

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('appointment/', p.schedule_appointment),
    # path('history/', p.medical_history),
    # path('notifications/', p.notifications),
    
    path('',include('Patients.urls')),


    # path('viewAppointment/', d.view_appointment),
    # path('viewRecords/', d.access_records),
    # path('prescription/', d.prescription),
    path('',include('Doctors.urls')),
    
    # path('management/', a.management),
    # path('reports/', a.reports),
    path('',include('Administration.urls')),



]
