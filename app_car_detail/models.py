from django.db import models
from app_car_model.models import Car
from utils.upload_image import upload_image

class BaseCarModel(models.Model):
    image = models.ImageField(upload_to=upload_image, verbose_name='Imagen')
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.CharField(max_length=220, verbose_name='Descripción')
    
    class Meta:
        abstract = True

class CarDetail(BaseCarModel):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='CarDetail', verbose_name='Automóvil')

    class Meta:
        verbose_name = 'Ficha del Automóvil'
        verbose_name_plural = 'Fichas del los Automoviles'
    
    def __str__(self):
        return f'{self.car.name} {self.car.version}'
    
class SmallFeatures(BaseCarModel):
    car_detail = models.ForeignKey(CarDetail, on_delete=models.CASCADE, related_name='SmallFeatures', verbose_name='Ficha')

    class Meta:
        verbose_name = 'Detalle corto'
        verbose_name_plural = 'Detalles cortos'
    
    def __str__(self):
        return self.title
    
class BigFeatures(BaseCarModel):
    car_detail = models.ForeignKey(CarDetail, on_delete=models.CASCADE, related_name='BigFeatures', verbose_name='Ficha')
    description = models.TextField(max_length=1000, verbose_name='Descripción')


    class Meta:
        verbose_name = 'Detalle amplio'
        verbose_name_plural = 'Detalles amplios'
    
    def __str__(self):
        return self.title