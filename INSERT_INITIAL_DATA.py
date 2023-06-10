import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDev.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from app_car_category.models import CarCategory
from app_car_model.models import Car
from app_car_detail.models import CarDetail, SmallFeatures, BigFeatures

CarCategory.objects.bulk_create([
    CarCategory(name='Autos'),
    CarCategory(name='Pickups'),
])

Car.objects.bulk_create([
    Car(
        category_id=1,
        thumbnail='/images/etios.png',
        name='Etios',
        year=2019,
        version='XLS',
        price=815900
    ),
    Car(
        category_id=2,
        thumbnail='/images/hilux.png',
        name='Hilux',
        year=2020,
        version='DX/SR',
        price=1500000
    )
])

CarDetail.objects.create(
    car_id=2,
    image='/images/hilux_ficha.png',
    title='Preparada para cualquier desafío',
    description='Texto lorem ipsum dolor sit amet orem ipsum dolor sit amet. lorem ipsum dolor sit amet orem ipsum dolor sit amet lorem ipsum dolor sit amet orem ipsum dolor sit amet.',
)

SmallFeatures.objects.bulk_create([
    SmallFeatures(
        car_detail_id=1,
        image='/images/motor.png',
        title='Nuevos Motores Toyota',
        description='Dos alternativas diesel con turbo de geometría variable, 1GD (2.8 L) y 2GD (2.4 L).'
    ),
    SmallFeatures(
        car_detail_id=1,
        image='/images/suspension.png',
        title='Suspensión mejorada',
        description='Mayor confort de marcha, estabilidad y capacidad Off Road.'
    ),
    SmallFeatures(
        car_detail_id=1,
        image='/images/transmision.png',
        title='Transmisión automática',
        description='Posibilidad de elección de caja automática de  manejo.'
    )
])

BigFeatures.objects.bulk_create([
    BigFeatures(
        car_detail_id=1,
        image='/images/chasis.png',
        title='Título de 20 px',
        description='Texto lorem ipsum dolor sit amet orem ipsum dolor sit amet. lorem ipsum dolor sit amet orem ipsum dolor sit amet lorem ipsum dolor sit amet orem ipsum dolor sit amet.'
    )
])