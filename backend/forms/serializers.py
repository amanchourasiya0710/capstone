from rest_framework import serializers
from .models import Forms, FormFields, WorkFlowStates, FormInstance, FormFieldData

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

class FormInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormInstance
        fields = ('form', 'userEmail', 'currentState',)

class FormFieldDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFieldData
        fields = ('fieldId', 'formInst', 'value')