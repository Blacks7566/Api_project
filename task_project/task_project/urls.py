from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router = DefaultRouter()
router.register('imageApi',views.ImageView,basename='images')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
