from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('price', views.PriceView.as_view(), name='price'),
    path('videos', views.VideoListView.as_view(), name='videos'),
    path('video/<int:pk>/', views.VideoView.as_view(), name='video')
]
