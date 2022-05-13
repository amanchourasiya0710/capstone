from django.contrib import admin
from .models import Forms, FieldTypes, FormFields, WorkFlow, WorkFlowStates, StateTransition

# Register your models here.
admin.site.register(Forms)
admin.site.register(FieldTypes)
admin.site.register(FormFields)
admin.site.register(WorkFlow)
admin.site.register(WorkFlowStates)
admin.site.register(StateTransition)