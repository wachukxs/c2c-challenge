from tastypie.resources import ModelResource
from api.models import Item, Interest, Buyer, Seller
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'items'
        authorization = Authorization()

class InterestResource(ModelResource):
    class Meta:
        queryset = Interest.objects.all()
        resource_name = 'interests'
        authorization = Authorization()
        allowed_methods = ['get']

class BuyerResource(ModelResource):
    class Meta:
        queryset = Buyer.objects.all()
        resource_name = 'buyers'
        authorization = Authorization()

class SellerResource(ModelResource):
    class Meta:
        queryset = Seller.objects.all()
        resource_name = 'sellers'
        authorization = Authorization()
        excludes = ['password', 'created_at']
        filtering = {
            "slug": ('exact', 'startswith',),
            "email": ALL,
        }