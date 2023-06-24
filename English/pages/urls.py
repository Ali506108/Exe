from django.urls import path
from .views import exe

urlpatterns = [
    path("", exe, name="exe"),
]
