from django.contrib import admin
from .models import Forms, FieldTypes, FormFields, WorkFlow, WorkFlowStates, StateTransition
from .models import FormInstance, FormFieldData

# Register your models here.
admin.site.register(Forms)
admin.site.register(FieldTypes)
admin.site.register(FormFields)
admin.site.register(FormInstance)
admin.site.register(FormFieldData)
admin.site.register(WorkFlow)
admin.site.register(WorkFlowStates)
admin.site.register(StateTransition)