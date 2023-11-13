from django.urls import path
from .views import bbs_api, BbDetailAPIView, comments_api

app_name = 'api'

urlpatterns = [
    path('bbs/', bbs_api),
    path('bbs/<int:pk>', BbDetailAPIView.as_view()),
    path('bbs/<int:pk>/comments', comments_api),
]
