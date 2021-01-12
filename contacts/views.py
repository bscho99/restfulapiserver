from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.


@csrf_exempt
def contacts(request):
    if request.method == 'GET':
        query_set = Contact.objects.all()
        serializer = ContactSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        query_set = Contact.objects.all()
        query_set.delete()
        return HttpResponse(status=200)


@csrf_exempt
def contact(request, pk):
    obj = Contact.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ContactSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serializer = ContactSerializer(obj)
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def get(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        name = data['name']
        obj = Contact.objects.get(name=name)
        serializer = ContactSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
