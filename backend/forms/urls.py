from django.urls import path
from . import views

urlpatterns = [
    path('get_forms/', views.forms_list, name='Form_List'),
    path('get_form_fields/', views.get_form_fields, name='FORM_FIELDS'),
]