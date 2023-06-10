from django.urls import path
from .views import CarList, CarDetail

urlpatterns = [
    path('cars/', CarList.as_view()),
    path('car/<int:pk>/', CarDetail.as_view()),
]