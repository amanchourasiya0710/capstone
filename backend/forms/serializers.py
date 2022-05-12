from rest_framework import serializers
from .models import Forms, FormFields

class FormsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Forms
       fields = ('name')
    
# class FormFields(models.Model):
#     form = models.ForeignKey(Forms, on_delete=models.CASCADE, related_name = 'formFields')
#     background = models.CharField(max_length=256, default='',blank=True)
#     fieldName = models.CharField(max_length=256)
#     fieldType = models.ForeignKey(FieldTypes, on_delete=models.CASCADE)
#     fieldLocation=models.IntegerField(default=0)
#     class Meta:
#         verbose_name_plural = 'FormFields'
#     def __str__(self):
#         return '{} {}'.format(self.background, self.fieldName)

class FormFieldsSerializer(serializers.ModelSerializer):
   class Meta:
       model = FormFields
       fields = ('name')