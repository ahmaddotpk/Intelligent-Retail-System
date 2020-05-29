"""irsserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

from .views import UserViewSet, StoreViewSet, EmployeeViewSet, CustomerViewSet, SalepointViewSet, ItemCategoryViewSet, ItemViewSet, ItemBatchViewSet, SaleViewSet, OrderViewSet, ForecastDataViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('stores', StoreViewSet)
router.register('employees', EmployeeViewSet)
router.register('customers', CustomerViewSet)
router.register('salepoints', SalepointViewSet)
router.register('itemcategories', ItemCategoryViewSet)
router.register('items', ItemViewSet)
router.register('itembatches', ItemBatchViewSet)
router.register('sales', SaleViewSet)
router.register('orders', OrderViewSet)
router.register('predict', ForecastDataViewSet, basename='predict')


urlpatterns = [
    path('', include(router.urls)),
    
]
