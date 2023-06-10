from django.contrib import admin
from .models import CarDetail, SmallFeatures, BigFeatures
from app_car_model.models import Car

class SmallFeaturesAdmin(admin.StackedInline):
    model = SmallFeatures
    extra = 1

class BigFeaturesAdmin(admin.StackedInline):
    model = BigFeatures
    extra = 1

@admin.register(CarDetail)
class CarDetailAdmin(admin.ModelAdmin):
    fields = (
        'car',
        'image',
        'title',
        'description'
    )
    inlines = (SmallFeaturesAdmin, BigFeaturesAdmin)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CarDetailAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['car'].queryset = Car.objects.filter(CarDetail__isnull=True)
        return form