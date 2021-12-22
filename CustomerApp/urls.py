from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_customer/',views.add_customer),
    path('all_customer/',views.all_customer),
    path('<int:customer_id>/',views.customer_detail,name='customer_detail'),
    path('add/',views.add),
    path('<int:customer_id>/customer_delete/',views.customer_delete,name='customer_delete'),

    path('customer_api/customers/',views.customer_json_list),
    path('customer_api/customers/<int:pk>/', views.customer_json_detail),
]