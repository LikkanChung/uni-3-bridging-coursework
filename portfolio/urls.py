from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('projects/<int:pk>', views.project_detail, name='project_detail'),
]
