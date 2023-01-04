from rest_framework import serializers
from api.models import ImagesPro


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesPro
        fields = '__all__'
        read_only_fields = ['thumbnial','medium','large','grayscale']