from django.urls import path
from . import views

urlpatterns = [
    path('get_forms/', views.get_forms, name='FORM_LIST'),
    path('get_username/', views.get_username, name='GET_USERNAME'),
    path('get_form_fields/', views.get_form_fields, name='FORM_FIELDS'),
    path('get_form_states/', views.get_form_states, name='FORM_STATES'),
    path('create_form_instance/', views.create_form_instance, name='FORM_INSTANCE'),
    path('save_form_instance/', views.save_form_instance, name='SAVE_FORM_INSTANCE'),
]
