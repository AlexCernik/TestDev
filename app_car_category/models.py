from django.db import models

class CarCategory(models.Model):
    name = models.CharField(max_length=70, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo?', help_text='Indica si la categoría esta activa o no.')
    
    class Meta:
        verbose_name = 'Categoría'
    
    def __str__(self):
        return self.name