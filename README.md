# Aplicación challenge Test_Dev.

Aplicación que permite listar categorías, automóviles y obtener la ficha de los automóviles.

</br>
- <b>Instalar las dependencias.</b>

```
pip install -r requirements.txt
```
</br>
- <b>Hacer las migraciones.</b>

```
python manage.py makemigrations
python manage.py migrate
```
</br>
- <b>Crear un super usuario.</b>

```
python manage.py createsuperuser
```
</br>
- <b>Iniciar el servidor.</b>

```
python manage.py runserver
```
</br>
- <b>Se pueden cargar algunos datos iniciales con el siguiente comando (OPCIONAL).</b>
Este carga algunas categorías y automóviles.

```
python INSERT_INITIAL_DATA.py
```

# Endpoints

| URL (GET) | Descripción |
| --- | --- |
| /api/v1/index/ | Trae las categorías y los automóviles. </br> (Únicaménte categorías que tengan automóviles asociados). |
| /api/v1/cars/ | Listado de todos los automóviles. |
| /api/v1/cars/?by_category_id=ID | Filtrar automóviles por categorías. |
| /api/v1/cars/?by_price=param | Parámetro (price) ordena de menor a mayor precio. </br> Parámetro (-price) ordena de mayor a menor precio. |
| /api/v1/cars/?by_year=param | Parámetro (year) ordena los más viejos primero. </br> Parámetro (-year) ordena los más nuevos primero. |
| /api/v1/car/ID_AUTO/ | Obtener la ficha de un automóvil. |

</br>

Se puede utilizar una combinación entre el filtrado por categoría y por orden, por ejemplo

    /api/v1/cars/?by_category_id=ID&by_year=-year
    o
    /api/v1/cars/?by_category_id=ID&by_price=price
