from django.contrib import admin
from .models import Forms, FieldTypes, FormFields, WorkFlow, WorkFlowStates, StateTransition
from .models import FormInstance, FormFieldData

from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode

BASE_URL = 'http://127.0.0.1:8000'

@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_instance_count')

    def view_instance_count(self, obj):
        count = len(FormInstance.objects.filter(form = obj))
        url = (
            reverse('admin:forms_forminstance_changelist')
            + "?"
            + f'form={obj.id}'
        )
        return format_html('<a href="{}">{} Instance</a>', url, count)

    view_instance_count.short_description = 'instances'


@admin.register(FieldTypes)
class FieldTypesAdmin(admin.ModelAdmin):
    pass


@admin.register(FormFields)
class FormFieldsAdmin(admin.ModelAdmin):
    list_display = (
        'view_field_id',
        'view_related_form', 
        'view_background',
        'view_fieldname',
        'view_fieldtype',
    )

    def view_field_id(self, obj):
        return obj.id
    view_field_id.short_description = 'FIELD ID'

    def view_related_form(self, obj):
        url = (
            reverse('admin:forms_forms_changelist')
            + "?"
            + f'pk={obj.form.id}'
        )
        return format_html('<a href="{}">{}</a>', url, obj.form)
    view_related_form.short_description = 'RELATED FORM'

    def view_background(self, obj):
        return obj.background
    view_background.short_description = 'BACKGROUND'

    def view_fieldname(self, obj):
        return obj.fieldName
    view_fieldname.short_description = 'FIELD NAME'

    def view_fieldtype(self, obj):
        return obj.fieldType
    view_fieldtype.short_description = 'FIELD TYPE'


@admin.register(FormInstance)
class FormInstanceAdmin(admin.ModelAdmin):
    list_display = ('view_instance_id', 'form_name', 'userEmail', 'view_current_state', 'view_time', 'view_related_data_fields')

    def view_instance_id(self, obj):
        return obj.id
    view_instance_id.short_description = 'INSTANCE ID'

    def form_name(self, obj):
        return obj.form
    form_name.short_description = 'FORM'

    def view_current_state(self, obj):
        return obj.currentState
    view_current_state.short_description = 'CURRENT STATE'

    def view_time(self, obj):
        return obj.time
    view_time.short_description = 'LAST CHANGED'
    
    def view_related_data_fields(self, obj):
        count = len(FormFieldData.objects.filter(formInst = obj))
        url = (
            reverse('admin:forms_formfielddata_changelist')
            + "?"
            + f'formInst={obj.id}'
        )
        return format_html('<a href="{}">{} Field</a>', url, count)
    view_related_data_fields.short_description = 'RELATED DATA FIELDS'


@admin.register(FormFieldData)
class FormFieldDataAdmin(admin.ModelAdmin):
    # list_display = ()
    pass
    

@admin.register(WorkFlow)
class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ('name', 'view_related_form', 'view_related_states')

    def view_related_form(self, obj):
        url = (
            reverse('admin:forms_forms_changelist')
            + "?"
            + f'pk={obj.form.id}'
        )
        return format_html('<a href="{}">{}</a>', url, obj.form)
    view_related_form.short_description = 'RELATED FORM'

    def view_related_states(self, obj):
        count = len(WorkFlowStates.objects.filter(workflow=obj))
        url = (
            reverse('admin:forms_workflowstates_changelist')
            + "?"
            + f'workflow={obj.id}'
        )
        return format_html('<a href="{}">{} State</a>', url, count)
    view_related_states.short_description = 'RELATED STATES'

@admin.register(WorkFlowStates)
class WorkFlowStatesAdmin(admin.ModelAdmin):
    list_display = ('state', 'view_workflow')

    def view_workflow(self, obj):
        url = (
            reverse('admin:forms_workflow_changelist')
            + "?"
            + f'form={obj.workflow.form.id}'
        )
        return format_html('<a href="{}">{}</a>', url, obj.workflow)
    view_workflow.short_description = 'RELATED WORKFLOW'

@admin.register(StateTransition)
class StateTransitionAdmin(admin.ModelAdmin):
    list_display = ('fromState', 'toState')