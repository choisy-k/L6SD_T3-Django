from django.contrib import admin
from .models import ShopNote, Item

# Register your models here.
#superuser: adminoci, oci@gmail.com, @dminOci123
admin.site.register(ShopNote)
admin.site.register(Item)