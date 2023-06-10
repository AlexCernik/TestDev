from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, Count
from .models import Car
from .serializers import CarSerializer
from app_car_detail.serializers import CarDetailBaseSerializer
from app_car_category.models import CarCategory

class CarList(APIView):
    """
        Obtenemos una lista de todos los autos.
        Filtrado por categoría únicamente si esta está activa y tiene automóviles cargados.
    """
    def get(self, request):
        by_category_id = request.query_params.get('by_category_id')
        by_price = request.query_params.get('by_price')
        by_year = request.query_params.get('by_year')

        _filter = Q(category__active=True)

        if by_category_id:
            try:
                category_queryset = CarCategory.objects \
                .annotate(car_count=Count("Car")) \
                .get(pk=by_category_id, active=True, car_count__gt=0)
                _filter = Q(category=category_queryset)
            except:
                if not by_category_id.isnumeric():
                    return Response(
                        {'detail': 'El ID de la categoría debe ser un número entero.'},
                        status=status.HTTP_404_NOT_FOUND
                    )
                elif by_category_id:
                    return Response(
                        {'detail': 'La categoría no existe o todavía no tiene automóviles cargados.'},
                        status=status.HTTP_404_NOT_FOUND
                    )

        queryset = Car.objects.filter(
            _filter,
            active=True
        )

        if by_price:
            if by_price == '-price' or by_price == 'price':
                queryset = queryset.order_by(by_price)
            else:
                return Response(
                    {'detail': 'El parámetro price debe ser -price o price.'},
                    status=status.HTTP_404_NOT_FOUND
                )

        elif by_year:
            if by_year == '-year' or by_year == 'year':
                queryset = queryset.order_by(by_year)
            else:
                return Response(
                    {'detail': 'El parámetro year debe ser -year o year.'},
                    status=status.HTTP_404_NOT_FOUND
                )

        serializer = CarSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CarDetail(APIView):

    def get(self, request, pk):
        try:
            instance = Car.objects.get(pk=pk, category__active=True, active=True)
        except:
            return Response(
                {'detail': 'No se encontró un automóvil con ese ID.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        try:
            car_detail = instance.CarDetail
        except:
            return Response(
                {'detail': 'No se pudo cargar la ficha del modelo, vuelva a intentarlo más tarde.'},
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            serializer_car_detail = CarDetailBaseSerializer(car_detail, context={'request': request})
            serializer_small_features = CarDetailBaseSerializer(instance.CarDetail.SmallFeatures.all(), many=True, context={'request': request})
            serializer_big_features = CarDetailBaseSerializer(instance.CarDetail.BigFeatures.all(), many=True, context={'request': request})

            return Response({
                'car': {
                    'name': instance.name,
                    'version': instance.version
                },
                'car_detail': serializer_car_detail.data,
                'small_features': serializer_small_features.data,
                'big_features': serializer_big_features.data
            })