from django.db import models

# Create your models here.
class product(models.Model):
    types= [
        ('Chair', 'Chair'),
        ('Table', 'Table'),
        ('others','others'),
    ]

    productaname = models.CharField(max_length=255,null=False,default="NA")
    producttype = models.CharField(max_length=255,choices= types)
    productqty = models.IntegerField()
    productprice = models.IntegerField(null=False,default="NA")
    productdesc = models.TextField()
    producttopping =models.CharField(max_length=255,default="NA")
    product_logo_url = models.ImageField(upload_to="ProductImages/",default="ProductImages/product.png")
