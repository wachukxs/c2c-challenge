from tastypie.resources import ModelResource
from api.models import Item, Interest, Buyer, Seller
from tastypie.authorization import Authorization

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