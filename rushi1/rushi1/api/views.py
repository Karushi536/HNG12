from django.shortcuts import render
from .serializers import MyModelSerializer
from .models import MyModel
from django.utils.timezone import now
from django.http import JsonResponse

# Create your views here.
def MyModelview(request):
    if request.method == 'GET':
        instance = MyModel.objects.first()
        serializer = MyModelSerializer(instance)
        data = serializer.data
        data["current_datetime"] = now().isoformat()
        return JsonResponse(serializer.data, safe=False, status=200)
