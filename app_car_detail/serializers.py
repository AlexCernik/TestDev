from rest_framework import serializers

class CarDetailBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)