from django.urls import path
from . import views
from django.conf.urls import  url,include
from .views import DataViewSet,ClientViewSet
from rest_framework.routers import  DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token #


router=DefaultRouter()
router.register("client",ClientViewSet,basename="client")
router.register("client-data",DataViewSet,basename="client-data")



urlpatterns = [
    url("api/",include(router.urls)),
    path("",views.index,name="index"),
    path("tables/",views.tables,name="tables"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

]