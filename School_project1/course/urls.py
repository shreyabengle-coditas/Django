from django.urls import path
from course import views as c

urlpatterns=[
    path('',c.home_page),
    path('python/',c.learn_python),
    path('django/', c.learn_django),
    path('var/', c.learn_var),
    path('math/', c.learn_math),

]