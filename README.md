# Aplicación challenge Test_Dev.

Aplicación que permite listar categorías, automóviles y la ficha de los automóviles.

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

El principal que trae las categorías y también los automóviles, (Trae únicaménte las categorías que tengan automóviles asociados).

```
/api/v1/index/
```

</br></br>

<b>Listado de todos los automóviles.</b>

```
/api/v1/cars/
```

</br></br>

<b>Filtrar automóviles por categorías.</b>

```
/api/v1/cars/?by_category_id=ID
```

</br></br>

<b>Listado de automóviles según precio.</b>

    Parámetro (price) ordena de menor a mayor precio.
    Parámetro (-price) ordena de mayor a menor precio.

ejemplo

```
/api/v1/cars/?by_price=price
```

</br></br>

<b>Listado de automóviles según antigüedad.</b>

    Parámetro (year) ordena los más viejos primero.
    Parámetro (-year) ordena los más nuevos primero.

ejemplo

```
/api/v1/cars/?by_year=-year
```

</br>

Se puede utilizar una combinación entre el filtrado por categoría y por orden, por ejemplo

    /api/v1/cars/?by_category_id=ID&by_year=-year
    /api/v1/cars/?by_category_id=ID&by_price=price

</br></br>

<b>Obtener la ficha de un automóvil.</b>

```
/api/v1/car/ID_AUTO/
```