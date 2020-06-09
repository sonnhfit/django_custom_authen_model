from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# quản lý tài khoản


# tài khoản
class TaiKhoan(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    link_anh_dai_dien = models.CharField(max_length=200)
    ngay_sinh = models.DateField()
    ngay_tao = models.DateField()


class HangSanXuat(models.Model):
    ten_hang = models.CharField(max_length=255)


class HangHoa(models.Model):
    ten_hang = models.CharField(max_length=255)
    gia_tien = models.IntegerField(default=0)
    hang = models.ForeignKey(HangSanXuat, on_delete=models.SET_NULL, null=True, blank=True)


class User(AbstractUser):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
