from django.contrib import admin
from .models import Person, Product, Order

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Order)
