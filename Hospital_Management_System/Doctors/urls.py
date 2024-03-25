from django.urls import path
from Doctors import views as d
urlpatterns=[
     path('viewAppointment/', d.view_appointment),
    path('viewRecords/', d.access_records),
    path('prescription/', d.prescription),
]