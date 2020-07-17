from django.db import models

# Create your models here.

class Seller(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    state_of_residence = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Buyer(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return '%s living at %s' % (self.name, self.location)

class Item(models.Model): # deletable.
    price = models.CharField(max_length=50)
    description = models.TextField()
    name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200) # 'sold' or 'for-sale'.
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s sold at %s' % (self.name, self.price)

class Interest(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # when the buyer got intrested.

    def __str__(self):
        return '%s is intrested in %s' % (self.buyer, self.created_at)