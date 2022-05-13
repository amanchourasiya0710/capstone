from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core import serializers

from .models import Forms, FormFields, WorkFlow, WorkFlowStates
from .serializers import FormsSerializer, FormFieldsSerializer, WorkFlowStatesSerializer

@api_view(['GET'])
def forms_list(request):
    "List all form types present in the database."
    if request.method == 'GET':
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms, many=True)
        print("serializer -->> :: ", serializer)
        return Response(serializer.data)
    
@api_view(['POST'])
def get_form_fields(request):
    "Get all fields corresponding to a particular form"
    if request.method == 'POST':
        form_serializer = FormsSerializer(data=request.data)

        if form_serializer.is_valid():
            formName = form_serializer.data['name'] 
            formObject = Forms.objects.get(name=formName)
            print("form Object: ", formObject)

            # formfields = FormFields.objects.all().filter(form=formObject)
            formfields = FormFields.objects.filter(form=formObject)

            result = []
            for obj in formfields:
                d = {
                    "background": obj.background,
                    "fieldName": obj.fieldName,
                    "fieldType": obj.fieldType.typeName,
                    "fieldLocation": obj.fieldLocation
                }
                result.append(d)
            # formfields_serializer = FormFieldsSerializer(formfields, many=True)
            # print("old>>>>>>>>>>>>>>>>>>>>>>", formfields_serializer.data)
            # result_serializer = serializers.serialize('json', result, fields=('background', 'fieldName', 'fieldType', 'fieldLocation',))
            # print("new>>>>>>>>>>>>>>>>>>>>>>", result_serializer.data)
            return Response(result, status=status.HTTP_201_CREATED)
            # return Response(formfields_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_form_states(request):
    "Give the name of the form and get all the states corresponsinding to that form"
    if request.method == 'POST':
        form_serializer = FormsSerializer(data=request.data)

        if form_serializer.is_valid():
            # get the formObject from the formName
            formName = form_serializer.data['name'] 
            formObject = Forms.objects.get(name=formName)
            print("form Object: ", formObject)

            # get the WorkflowObject from the formObject
            workflowObject = WorkFlow.objects.get(form = formObject)

            # get all states from this WorkflowObject.
            states = WorkFlowStates.objects.all().filter(workflow = workflowObject)
            print("states: ", states)
            states_serializer = WorkFlowStatesSerializer(states, many=True)
            return Response(states_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_form_instance(request):
    "Give (formName, userName, currentState) and your new form instance will get created."
    pass

@api_view(['POST'])
def save_form_instance(request):
    "Give ()"
    pass