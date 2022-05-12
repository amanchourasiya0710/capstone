from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Forms 
from .serializers import FormsSerializer

@api_view(('GET', 'POST'))
def forms_list(request):
    "List all form types present in the database."
    
    forms = Forms.objects.all()
    serializer = FormsSerializer(forms, many=True)
    print("serializer -->> :: ", serializer)
    return Response(serializer.data)
