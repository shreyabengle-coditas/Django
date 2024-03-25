from django.urls import path
from . import views 

urlpatterns=[
    path('adminLogin/',views.admin_login ),
    path('adminControl/', views.admin_control),
    path('var1/',views.admin_var1),
    path('math1/',views.admin_math1),
]

