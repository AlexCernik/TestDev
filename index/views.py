from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from app_car_category.models import CarCategory
from app_car_category.serializers import CarCategorySerializer
from app_car_model.models import Car
from app_car_model.serializers import CarSerializer

class Index(APIView):

    def get(self, request):
        category_queryset = CarCategory.objects.filter(active=True, Car__active=True).annotate(car_count=Count('Car')).filter(car_count__gt=0)
        category_serializer = CarCategorySerializer(category_queryset, many=True)

        car_queryset = Car.objects.filter(category__in=category_queryset, active=True)
        car_serializer = CarSerializer(car_queryset, many=True, context={'request': request})

        return Response({
            'categories': category_serializer.data,
            'cars': car_serializer.data
        })