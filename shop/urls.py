
from django.urls import path
from .views import index, purchase_form, checkout, process_payment

urlpatterns = [
    path('', index, name='index'),
    path('purchase-form/<int:product_id>/', purchase_form, name='purchase_form'),
    path('checkout/<int:purchase_id>/', checkout, name='checkout'),
    path('process-payment/<int:purchase_id>/', process_payment, name='process_payment'),
]
