from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('saved/<str:em>/<str:val>', views.saved, name='saved'),
    path('pas/<str:em>/<str:val>', views.pas, name='pas'),
    path('del/<str:em>/<str:val>/<str:ste>', views.dela, name='dela'),
    path('logu/<str:val>', views.logu, name='logu')
]
