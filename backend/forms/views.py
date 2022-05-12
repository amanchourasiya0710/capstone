from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Forms 
from .serializers import FormsSerializer


@api_view(['GET'])
def forms_list(request):
    "List all form types present in the database."
    
    if request.method == 'GET':
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms, many=True)
        print("serializer -->> :: ", serializer)
        return Response(serializer.data)
