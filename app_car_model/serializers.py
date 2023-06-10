from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    name = serializers.CharField(read_only=True)
    year = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
