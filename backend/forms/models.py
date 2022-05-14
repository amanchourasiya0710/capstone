from django.db import models
from accounts.models import Department, Roles, UserAccount

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
    
class WorkFlow(models.Model):
    name = models.CharField(max_length=256)
    form = models.ForeignKey(Forms, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'WorkFlow'
    def __str__(self):
        return f'{self.name}'

class WorkFlowStates(models.Model):
    workflow = models.ForeignKey(WorkFlow, on_delete=models.CASCADE, related_name='states')
    state = models.CharField(max_length=256)
    class Meta:
        verbose_name_plural = 'WorkFlowStates'
    def __str__(self):
        return f'{self.state}'

class StateTransition(models.Model):
    fromState = models.ForeignKey(WorkFlowStates, on_delete=models.CASCADE, related_name='fromState')
    toState = models.ForeignKey(WorkFlowStates, on_delete=models.CASCADE, related_name='toState')
    class Meta:
        verbose_name_plural = 'StateTransition'
    def __str__(self):
        return f'{self.fromState} -> {self.toState}'

class TransitionRoles(models.Model):
    transtion = models.ForeignKey(StateTransition, on_delete=models.CASCADE, related_name='allowedRoles')
    rolesAllowed = models.ForeignKey(Roles, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'TransitionRoles'
    def __str__(self):
        return f'Transition:{self.transtion} Allowed to:{self.rolesAllowed}'

class FormInstance(models.Model):
    form = models.ForeignKey(Forms, on_delete=models.CASCADE, related_name='formInstances')
    userEmail = models.EmailField(max_length=250)
    # user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='requests')
    time = models.DateTimeField(auto_now_add=True)
    currentState = models.ForeignKey(WorkFlowStates, on_delete=models.CASCADE, related_name='activeforms')
    class Meta:
        verbose_name_plural = 'FormInstances'
    def __str__(self):
        return f'{self.form} Instance: {self.id}'

class FormFieldData(models.Model):
    fieldId = models.ForeignKey(FormFields, on_delete=models.CASCADE, related_name='fieldData')
    formInst = models.ForeignKey(FormInstance, on_delete=models.CASCADE, related_name='formData')
    value = models.CharField(max_length=1000)
    class Meta:
        verbose_name_plural = 'FormFieldData'
    def __str__(self):
        return f'{self.formInst} Data: {self.fieldId}'


# class WorkflowData(models.Model):
#     formInst = models.ForeignKey(FormInstance, on_delete=models.CASCADE, related_name='workflowdata')
#     transitions = models.ForeignKey(StateTransition, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)