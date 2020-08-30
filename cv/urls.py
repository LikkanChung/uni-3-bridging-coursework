from django.urls import path
from . import views

app_name = "cv"

urlpatterns = [
    path('', views.cv, name='cv'),
    path('add/contact', views.cv_add_contact, name="cv_add_contact"),
    path('edit/contact/<int:pk>', views.cv_edit_contact, name="cv_edit_contact"),
    path('add/education', views.cv_add_education, name="cv_add_education"),
    path('edit/education/<int:pk>', views.cv_edit_education, name="cv_edit_education"),
    path('add/experience', views.cv_add_experience, name="cv_add_experience"),
    path('edit/experience/<int:pk>', views.cv_edit_experience, name="cv_edit_experience"),
    path('add/volunteering', views.cv_add_volunteering, name="cv_add_volunteering"),
    path('edit/volunteering/<int:pk>', views.cv_edit_volunteering, name="cv_edit_volunteering"),

]
