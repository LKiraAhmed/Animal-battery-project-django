from django.db import models
from django.contrib.auth.models import User
import json

from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True , blank=True)
    business_name = models.TextField(max_length=30, null=True , blank=True)
    about = models.TextField(null=True , blank=True)
    address = models.TextField(null=True,blank=True)
    phone = models.TextField(max_length=11,null=True , blank=True)
    business_phone = models.TextField(max_length=11 , null=True , blank=True)
    def __str__(self):
        return self.user.username
    
class Product(models.Model):
    x = [
        ('Food','Food') , ('Clothes','Clothes'),
        ('accessories','accessories') , ('Medicine','Medicine'),
        ('Toys','Food') , ('Cages','Cages') , ('none','none')
    ]
    pet = [
        ('Cat','Cat') , ('Dog','Dog'),
        ('Bird','Bird') , ('Fish','Fish')
    ]
    user=models.ForeignKey(User , null=True, blank=True,on_delete=models.CASCADE)
    product_name = models.TextField(max_length=50)
    product_shot_des = models.TextField(max_length=100)
    product_description = models.TextField(max_length=2000)
    product_price = models.FloatField()
    product_discount_price = models.FloatField(null=True , blank=True)
    product_img = models.FileField(null=False, blank=False)
    product_sell_price = models.FloatField()
    product_stock = models.IntegerField()
    product_type = models.TextField(choices=pet)
    product_Catecory = models.TextField(choices = x)
    discount = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
      return self.product_name

        
        
class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    product_img = models.FileField(null=False, blank=False)

    def __str__(self):
        return self.product.product_name
    

class Order(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.product_stock == 0 or i.product.product_stock == '0':
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.product_price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)


class DoctorVent(models.Model):
    user = models.OneToOneField( User , on_delete=models.CASCADE)
    email = models.EmailField(null=True , blank=True)
    phone = models.TextField(max_length=11,null=True , blank=True)
    vent_phone = models.TextField(max_length=11 , null=True , blank=True)
    address = models.TextField(blank=True , null=True)
    profile_pic = models.ImageField()
    about = models.TextField(null=True , blank=True)
    
    def __str__(self):
        return self.user.username
    
class Vent_Photo(models.Model):
    class Meta:
        verbose_name = 'Vent_Photo'
        verbose_name_plural = 'Vent_Photos'
    
    DoctorVent = models.ForeignKey(
        DoctorVent, on_delete=models.CASCADE, null=True, blank=True)
    vent_img = models.FileField(null=False, blank=False)



class search(models.Model):
    text=models.CharField(max_length=200)
    def __str__(self):
        return self.text
    

class Dogs(models.Model):
  accessories = models.CharField(max_length=50)

class AccessoriesDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='accessories_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=50)
  price = models.CharField(max_length=50)

class BedsDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='beds_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class FoodDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='food_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class FleaTicksDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='flea_ticks_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class GroomingDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='grooming_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class PharmacyVitaminsDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='pharmacy_vitamins_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class ToysDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='toys_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class TreatsBiscuitsDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='treats_biscuits_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class WetFoodDogs(models.Model):
  dog = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='wet_food_dogs')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)
#done dogs Sidebar 

class cats(models.Model):
  accessories = models.CharField(max_length=100)

class AccessoriesCats(models.Model):
  cats = models.ForeignKey(cats, on_delete=models.CASCADE, related_name='accessories_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)  

class BedsCats(models.Model):
    cats=models.ForeignKey(cats,on_delete=models.CASCADE,related_name='beds_cats')
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)  

class FoodCats(models.Model):
    cats=models.ForeignKey(cats,on_delete=models.CASCADE,related_name='food_cats')
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)  

class FleaTicksCats(models.Model):
  cats = models.ForeignKey(cats, on_delete=models.CASCADE, related_name='flea_ticks_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class Groomingcats(models.Model):
  cats = models.ForeignKey(cats, on_delete=models.CASCADE, related_name='grooming_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)
 
class PharmacyVitaminsCats(models.Model):
  cats = models.ForeignKey(Dogs, on_delete=models.CASCADE, related_name='pharmacy_vitamins_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class Toyscats(models.Model):
  cats = models.ForeignKey(cats, on_delete=models.CASCADE, related_name='toys_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class TreatsBiscuitsCats(models.Model):
  cats = models.ForeignKey(cats, on_delete=models.CASCADE, related_name='treats_biscuits_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)

class WetFoodCats(models.Model):
  cats = models.ForeignKey(cats, on_delete=models.CASCADE, related_name='wet_food_cats')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)
#done cats Sidebar

class fish(models.Model):
    accessories = models.CharField(max_length=100)

class AccessoriesFish(models.Model):
  fish = models.ForeignKey(fish, on_delete=models.CASCADE, related_name='accessories_fish')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)  

class FoodFish(models.Model):
    fish=models.ForeignKey(fish,on_delete=models.CASCADE,related_name='food_fish')
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)  
# done fish Sidebar

class Brid(models.Model):
    accessories = models.CharField(max_length=100)

class AccessoriesBrid(models.Model):
  Brid = models.ForeignKey(Brid, on_delete=models.CASCADE, related_name='accessories_Brid')
  img = models.ImageField()
  title = models.CharField(max_length=200)
  price = models.CharField(max_length=200)  

class FoodBrid(models.Model):
    Brid=models.ForeignKey(fish,on_delete=models.CASCADE,related_name='food_Brid')
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)  
# done Brid Sidebar
    