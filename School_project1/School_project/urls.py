"""
URL configuration for School_project project.

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
from django.urls import path,include

# from course import views as c
# from admin import views as a
from fees import views as f
# from fees.views import *

# from admin import views as ad
# import course


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dj/', c.learn_django),
    # path('python/', c.learn_python),
    # path('var/', c.learn_var),
    # path('math/', c.learn_math),
    path('', include('course.urls')),


   
    # path('adminLogin/', a.admin_login),
    # path('adminControl/',a.admin_control),
    # path('var1/', a.admin_var1),
    # path('math1/', a.admin_math1),
    path('', include('admin.urls')),


    
    
    # path('feePaid', f.fee_paid),
    # path('feeDue', f.fee_due),
    # path('feeRem', f.fee_remaning),
    # path('feeAmt', f.fee_amt),
    path('', include('fees.urls')),
   
]
