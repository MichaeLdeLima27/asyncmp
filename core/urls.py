from django.urls import path
from .views import contador_view

urlpatterns = [
    path("contador/", contador_view),
]
