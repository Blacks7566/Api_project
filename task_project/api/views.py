from rest_framework.viewsets import ModelViewSet
from account.models import User
from api.serializers import ImagesSerializer
from api.models import ImagesPro
from django.db.models.signals import post_save
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class ImageView(ModelViewSet):
    queryset = ImagesPro.objects.all()
    serializer_class = ImagesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
