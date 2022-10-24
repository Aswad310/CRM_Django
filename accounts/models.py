from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length= 200, null=True)
    email = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=10, default=1, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    # show name "Aswad" instead of Customer object(1)
    def __str__(self): 
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    # show Tag name instead of Tag object(1)
    def __str__(self): 
        return self.name
    
class Product(models.Model):
    CATEGORY = (
                    ('Indoor', 'Indoor'),
                    ('Out Door', 'Out Door'),
                )    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True) 
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    tag =  models.ManyToManyField(Tag) # many-to-many relationship
    status = models.CharField(max_length=10, default=1, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    # show Product name instead of Product object(1)
    def __str__(self): 
        return self.name
    
class Order(models.Model):
    STATUS = (
                ('Pending', 'Pending'),
                ('Out of delivery', 'Out of delivery'),
                ('Delivered', 'Delivered'),
            )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) #one-to-many
    product =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) #one-to-many
    order_status = models.CharField(max_length=200, null=True, choices=STATUS)
    status = models.CharField(max_length=10, default=1, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)