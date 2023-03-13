from django.db.models.signals import post_save  # tín hiệu gửi bởi hệ thống mô hình, được gửi cuối save()
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer

# chứa thông tin các tài khoản
@receiver(post_save,sender = User)
# tạo thông tin người dùng
def create_customer(sender, instance, created,**kwargs): # **kwargrs truyền 1 số lượng đối số bị thay đổi
    if created:
        Customer.objects.create(user = instance)
# lưu thông tin người dùng
@receiver(post_save,sender = User)
def save_customer(sender, instance,**kwargs):
    instance.customer.save()
