from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=25)
    customerid=models.CharField(max_length=25)
    customerphone=models.CharField(max_length=25)
    customerplace=models.CharField(max_length=25)

class Reg_seller(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Reg_user(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    address = models.CharField(max_length=600)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Reg_tutor(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    address = models.CharField(max_length=600)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)


class craft_selling(models.Model):
 
    owner_name=models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description  = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity=models.IntegerField()
    image = models.FileField(upload_to='crafts/')
    craft_material  = models.CharField(max_length=200)
    size  = models.CharField(max_length=200)


class accessories_selling(models.Model):
 
    owner_name=models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description  = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity=models.IntegerField()
    image = models.FileField(upload_to='accessories/')
    accessory_type = models.CharField(max_length=200)
    size  = models.CharField(max_length=200)


class Cart(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    username=models.CharField(max_length=100)
    totalamount=models.IntegerField()
    # size=models.IntegerField()

class Craftcart(models.Model):

    item_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    username=models.CharField(max_length=100)
    totalamount=models.IntegerField()

class pay(models.Model):
    username=models.CharField(max_length=30)
    # cardno=models.IntegerField()
    # card=models.IntegerField()
    phoneno=models.CharField(max_length=30)
    proname=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
class Video(models.Model):
    username=models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    video_link = models.URLField()
    video_file = models.FileField(upload_to='videos/')  # Add this line

    def __str__(self):
        return self.title
  