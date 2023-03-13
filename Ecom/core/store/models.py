from django.db import models
from django.contrib.auth.models import User # nhập mô hình người dùng mặc định của django
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import OneToOneField
from django.utils import translation

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self): # trả về chuỗi tên khách hàng
        return str(self.name)
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    detail = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True, blank =True)

    def __str__(self): # trả về chuỗi tên sản phẩm
        return self.name 

    def imageURL(self): # nếu url ảnh trống hay (ảnh sản phẩm không có) sẽ trả về ảnh nope no
        try:
            url = self.image.url
        except:
            url = ''
        return url
class Order (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False )

    def __str__(self):  #trả về id đơn đặt hàng
        return str(self.id) 

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
                shipping = True
        return shipping


    @property
    def get_cart_total(self):   # phương thức trả về tổng tiền các sản phẩm trong giỏ hàng
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):   # phương thức trả về tổng đơn hàng trong giỏ hàng
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)   
    zipcode = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)   

    def __str__(self): # trả về địa chỉ đặt hàng
        return str(self.address)
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    @property
    def get_total(self):    # phương thức trả về tổng giá sản phẩm từng sản phẩm
        total = self.product.price * self.quantity
        return total
    def __str__(self): #trả về sản phẩm trong giỏ hàng
        return str(self.product)