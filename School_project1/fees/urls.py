from django.urls import path
from fees import views as f

urlpatterns=[
    path('feePaid', f.fee_paid),
    path('feeDue', f.fee_due),
    path('feeRem', f.fee_remaning),
    path('feeAmt', f.fee_amt),

]