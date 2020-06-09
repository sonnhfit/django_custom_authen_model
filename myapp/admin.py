from django.contrib import admin

# Register your models here.
from .models import User, HangSanXuat, HangHoa, BaiViet

admin.site.register(User)
admin.site.register(HangSanXuat)
admin.site.register(HangHoa)
admin.site.register(BaiViet)
