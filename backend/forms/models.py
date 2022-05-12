from django.db import models

# Create your models here.
class Forms(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Forms'

    def __str__(self):
        return self.name

class FieldTypes(models.Model):
    typeName = models.CharField(max_length = 30)

    class Meta:
        verbose_name_plural = 'FieldTypes'

    def __str__(self):
        return self.typeName

class FormFields(models.Model):
    form = models.ForeignKey(Forms, on_delete=models.CASCADE, related_name = 'formFields')
    background = models.CharField(max_length=256, default='',blank=True)
    fieldName = models.CharField(max_length=256)
    fieldType = models.ForeignKey(FieldTypes, on_delete=models.CASCADE)
    fieldLocation=models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'FormFields'
    def __str__(self):
        return '{} {}'.format(self.background, self.fieldName)