from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from account.views import UserApi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router1 = DefaultRouter()

router.register('imageApi',views.ImageView,basename='images')
router1.register('userApi',UserApi,basename='user')


urlpatterns = [
    path('',include(router.urls)),
    path('userApi/',include(router1.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),

]
