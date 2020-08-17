from django.urls import path
from . import views

app_name = "cv"

urlpatterns = [
    path('', views.cv, name='cv'),
]
