from rest_framework import serializers
from .models import Forms, FormFields, WorkFlowStates

class FormsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Forms
       fields = ('name',)

class FormFieldsSerializer(serializers.ModelSerializer):
   class Meta:
       model = FormFields
       fields = ('form', 'background', 'fieldName', 'fieldType', 'fieldLocation',)

class WorkFlowStatesSerializer(serializers.ModelSerializer):
   class Meta:
       model = WorkFlowStates
       fields = ('workflow', 'state',)