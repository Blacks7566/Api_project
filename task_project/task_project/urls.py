from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api import views
from account.views import UserApi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router1 = DefaultRouter()

router.register('imageApi',views.ImageView,basename='images')
router1.register('userApi',UserApi,basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
