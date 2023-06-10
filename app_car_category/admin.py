from django.contrib import admin
from .models import CarCategory

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_editable = ('active',)