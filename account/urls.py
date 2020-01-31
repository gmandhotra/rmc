from django.urls import path,include
from .views import *


urlpatterns = [

    path(r'register/', UserViewSet.as_view()),
    path(r'login/', UserViewSet.as_view()),


]