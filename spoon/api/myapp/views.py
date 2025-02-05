from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyModelSerializer
from .models import MyModel

@api_view(['GET'])
def my_model_view(request):
    try:
        instance = MyModel.objects.latest('current_datetime')  # Use the correct field name
    except MyModel.DoesNotExist:
        return Response({"error": "No data found"}, status=404)
    
    serializer = MyModelSerializer(instance)
    data = serializer.data

    current_time = timezone.now().replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["current_datetime"] = current_time
    
    return Response(data, status=200)