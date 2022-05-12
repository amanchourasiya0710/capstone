from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.forms_list, name='Form_List'),
]
