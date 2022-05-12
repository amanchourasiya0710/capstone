from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Forms, FormFields
from .serializers import FormsSerializer, FormFieldsSerializer

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

            formfields = FormFields.objects.all().filter(form=formObject)
            print("formfields: ", formfields)
            formfields_serializer = FormFieldsSerializer(formfields, many=True)
            return Response(formfields_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
