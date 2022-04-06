from django.urls import path, include

from .views import OrderReportView


urlpatterns = [
    path('orders/', OrderReportView.as_view(), name = 'orders-report'),
]