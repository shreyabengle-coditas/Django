from django.urls import path
from Patients import views as p
urlpatterns=[
    path('',p.homepage),
    path('appointment/', p.schedule_appointment),
    path('history/', p.medical_history),
    path('notifications/', p.notifications),
]