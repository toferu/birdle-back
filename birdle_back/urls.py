from django.urls import path
from . import views

urlpatterns = [
    path('api/birdle/', views.BirdList.as_view(), name='bird_list'),
    path('api/birdle/<int:pk>', views.BirdDetail.as_view(), name='bird_detail'),
]