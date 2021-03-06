"""c2c_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from tastypie.api import Api
from django.conf.urls import url, include
from django.contrib import admin
from api.resources import ItemResource, SellerResource, InterestResource, BuyerResource

v1_api = Api(api_name='v1')
v1_api.register(SellerResource())
v1_api.register(InterestResource())
v1_api.register(ItemResource())
v1_api.register(BuyerResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(v1_api.urls)),
]
