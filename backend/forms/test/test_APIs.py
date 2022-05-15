from django.test import TestCase, Client
# from rest_framework.test import TestCase, Client
from rest_framework import status
from forms.models import *

import json

class TestAPIs(TestCase):  
     
    def setUp(self):
        self.client = Client()

        # Entries for 'test_get_forms'
        Forms.objects.create(name="LEAVE FORM")
        Forms.objects.create(name="REIMBURSEMENT FORM")

        # Entries for 'test_get_form_fields'
        FieldTypes.objects.create(typeName='STRING')
        FormFields.objects.create(
            form=Forms.objects.first(), 
            background='',
            fieldName='Name',
            fieldType=FieldTypes.objects.first(),
            fieldLocation=0
        )
        FormFields.objects.create(
            form=Forms.objects.first(), 
            background='',
            fieldName='Department',
            fieldType=FieldTypes.objects.first(),
            fieldLocation=0
        )

        # Entries for 'test_get_form_states'
        WorkFlow.objects.create(
            name = "LEAVE FORM WORKFLOW",
            form = Forms.objects.first() 
        )
        WorkFlowStates.objects.create(
            workflow = WorkFlow.objects.first(),
            state = "TODO"
        )
        WorkFlowStates.objects.create(
            workflow = WorkFlow.objects.first(),
            state = "INPROGRESS"
        )
        WorkFlowStates.objects.create(
            workflow = WorkFlow.objects.first(),
            state = "CLOSED"
        )

        # Entries for 'test_save_form_instance'
        FormInstance.objects.create(
            form = Forms.objects.first(),
            userEmail="admin@gmail.com",
            currentState=WorkFlowStates.objects.first()
        )

        self.form_inst_id = FormInstance.objects.first().id

    def test_get_forms(self):
        response = self.client.get('/forms/get_forms/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), [{'name': 'LEAVE FORM'}, {'name': 'REIMBURSEMENT FORM'}])

    def test_get_form_fields(self):
        response = self.client.post('/forms/get_form_fields/', {"name": "LEAVE FORM"})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(), 
            [
                {'form_field_id': 1, 'background': '', 'fieldName': 'Name', 'fieldType': 'STRING', 'fieldLocation': 0},
                {'form_field_id': 2, 'background': '', 'fieldName': 'Department', 'fieldType': 'STRING', 'fieldLocation': 0},
            ]
        )

    def test_get_form_states(self):
        response = self.client.post('/forms/get_form_states/', {"name": "LEAVE FORM"})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), [{'workflow': 1, 'state': 'TODO', 'workflowstates_pk': 1}, {'workflow': 1, 'state': 'INPROGRESS', 'workflowstates_pk': 2}, {'workflow': 1, 'state': 'CLOSED', 'workflowstates_pk': 3}])

    def test_create_form_instance(self):
        response = self.client.post('/forms/create_form_instance/', {"form": "LEAVE FORM", "userEmail": "admin@gmail.com"})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json(), [{'form_instance_id': 2}])
    
    def test_save_form_instance(self):
        req = [
                {"fieldId": 1, "formInst": self.form_inst_id, "value": "Anant"},
                {"fieldId": 2, "formInst": self.form_inst_id, "value": "Computer Science"}
            ]

        response = self.client.post(
            '/forms/save_form_instance/', 
            req,
            content_type='application/json'
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(),[{'fieldId': 1, 'formInst': 1, 'value': 'Anant'}, {'fieldId': 2, 'formInst': 1, 'value': 'Computer Science'}])