from django.contrib import admin
from app1.models import product,Offer
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','img_url')

class productoffer(admin.ModelAdmin):
    list_display = ('code','discription','discount')

    
admin.site.register(Offer,productoffer)
admin.site.register(product,productAdmin)
