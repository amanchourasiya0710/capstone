from django.contrib import admin
from .models import Forms, FieldTypes, FormFields

# Register your models here.
admin.site.register(Forms)
admin.site.register(FieldTypes)
admin.site.register(FormFields)