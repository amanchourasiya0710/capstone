from concurrent.futures import process
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core import serializers

from .models import FormInstance, Forms, FormFields, WorkFlow, WorkFlowStates
from .serializers import FormsSerializer, FormFieldsSerializer, WorkFlowStatesSerializer, FormInstanceSerializer, FormFieldDataSerializer

from accounts.models import UserAccount

@api_view(['POST'])
def get_username(request):
    "Give (useremail) and get (firstname, lastname)"
    if request.method == 'POST':
        res = {
            "fullname": ""
        }
        try:
            _user = UserAccount.objects.get(email = request.data['useremail'])
            res['fullname'] = _user.first_name + " " + _user.last_name
            return Response(res, status=status.HTTP_200_OK)
        except:
            res['fullname'] = "INVALID"
            return Response(res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_forms(request):
    "List all form types present in the database."
    if request.method == 'GET':
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms, many=True)
        # print("serializer -->> :: ", serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def get_form_fields(request):
    "Get all fields corresponding to a particular form"
    if request.method == 'POST':
        form_serializer = FormsSerializer(data=request.data)

        if form_serializer.is_valid():
            formName = form_serializer.data['name'] 
            formObject = Forms.objects.get(name=formName)
            # print("form Object: ", formObject)

            # formfields = FormFields.objects.all().filter(form=formObject)
            formfields = FormFields.objects.filter(form=formObject)

            result = []
            for obj in formfields:
                d = {
                    "form_field_id": obj.id,
                    "background": obj.background,
                    "fieldName": obj.fieldName,
                    "fieldType": obj.fieldType.typeName,
                    "fieldLocation": obj.fieldLocation
                }
                result.append(d)
            return Response(result, status=status.HTTP_200_OK)
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
            # print("form Object: ", formObject)

            # get the WorkflowObject from the formObject
            workflowObject = WorkFlow.objects.get(form = formObject)

            # get all states from this WorkflowObject.
            states = WorkFlowStates.objects.all().filter(workflow = workflowObject)
            # print("states: ", states)
            # states_serializer = WorkFlowStatesSerializer(states, many=True)

            result = []
            for obj in states:
                # print("obj workflow id: ", obj.workflow.id)
                # print("obj id: ", obj.id)
                d = {
                    "workflow": obj.workflow.id,
                    "state" : obj.state,
                    "workflowstates_pk": obj.id
                }
                result.append(d)
            return Response(result, status=status.HTTP_200_OK)
            # return Response(states_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_form_instance(request):
    "Give (form, userEmail) and your new form instance will get created."
    if request.method == 'POST':

        form_obj = Forms.objects.get(name=request.data['form'])
        workflow_obj = WorkFlow.objects.get(form=form_obj)
        all_obj = WorkFlowStates.objects.filter(workflow=workflow_obj)
        min_id = 10**9
        for obj in all_obj:
            min_id = min(min_id, obj.id)

        processed_data = request.data.copy()
        processed_data["form"] = form_obj.id
        processed_data["currentState"] = min_id

        serializer = FormInstanceSerializer(data=processed_data)
        if serializer.is_valid():
            obj = serializer.save()
            result = [{
                "form_instance_id": obj.id
            }]
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_form_instance(request):
    "Give form in form of (fieldId, formInst, value) and your form will be saved"
    if request.method == 'POST':
        processed_request = request.data['data']
        serializer = FormFieldDataSerializer(data=processed_request, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
