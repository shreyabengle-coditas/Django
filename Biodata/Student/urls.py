from django.urls import path
from Student import views as s
urlpatterns=[
    path('',s.display),
    path('NextPage/', s.new_page)

]