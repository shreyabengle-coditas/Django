from django.urls import path
from Patients import views as p
urlpatterns=[
    path('',p.homepage),

]