from django.test import TestCase, Client
# from rest_framework.test import TestCase, Client
from rest_framework import status
from forms.models import *


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

    def test_get_forms(self):
        response = self.client.get('/forms/get_forms/')
        self.assertEquals(response.json(), [{'name': 'LEAVE FORM'}, {'name': 'REIMBURSEMENT FORM'}])
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_form_fields(self):
        response = self.client.post('/forms/get_form_fields/', {"name": "LEAVE FORM"})
        print(response.json())
        self.assertEquals(1, 1)
