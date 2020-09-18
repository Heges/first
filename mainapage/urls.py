from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPaigeView.as_view(), name='mainpaige'),
]