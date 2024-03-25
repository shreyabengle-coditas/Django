from django.urls import path
from Administration import views as a

urlpatterns=[
    path('management/', a.management),
    path('reports/', a.reports),
]