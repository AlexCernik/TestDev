from django.db import models
from datetime import date
from app_car_category.models import CarCategory
from utils.upload_image import upload_image

class Car(models.Model):
    current_year = date.today().year + 1
    YEARS = ((i, i) for i in reversed(range(1920, current_year)))

    category = models.ForeignKey(CarCategory, on_delete=models.PROTECT, related_name='Car', verbose_name='Categoría')
    thumbnail = models.ImageField(upload_to=upload_image, verbose_name='Imagen miniatura', help_text='Se recomienda cargar una imagen miniatura de la original.')
    name = models.CharField(max_length=40, verbose_name='Nombre')
    year = models.PositiveSmallIntegerField(verbose_name='Año', choices=YEARS, help_text='Año de fabricación.')
    version = models.CharField(max_length=10, verbose_name='versión', help_text='Nombre de la versión.')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')
    active = models.BooleanField(default=True, verbose_name='Activo?', help_text='Indica si este automóvil sera visible al público.')

    class Meta:
        verbose_name = 'Automóvil'
        verbose_name_plural = 'Automoviles'
    
    def __str__(self):
        return self.name