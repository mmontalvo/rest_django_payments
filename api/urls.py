from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'payments', views.PaymentViewSet)
router.register(r'bank_transfer', views.BankTransferViewSet)

urlpatterns = [
    path('', include(router.urls))
]