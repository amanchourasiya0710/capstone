from rest_framework import serializers
from .models import Forms, FormFields

class FormsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Forms
       fields = ('name',)

class FormFieldsSerializer(serializers.ModelSerializer):
   class Meta:
       model = FormFields
       fields = ('form', 'background', 'fieldName', 'fieldType', 'fieldLocation',)