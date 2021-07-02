import io

from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import StudentSerializers
from django.http import JsonResponse, HttpResponse
from .models import Student

@method_decorator(csrf_exempt, name = 'dispatch')
class StudentAPI(View):
    def post(self,request,*args,**kwargs):
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        serializers = StudentSerializers(data = pythondata)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data created'}
            return JsonResponse(res, content_type='application/json')
        res = serializers.error
        return JsonResponse(res, content_type='application/json')

    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


    def put(self,request , *args , **kwargs):
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializers(stu , pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data udpated'}
            return JsonResponse(res, content_type='application/json')
        res = serializer.error()
        return JsonResponse(res, content_type='application/json')


    def delete(self,request, *args, **kwargs):
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id= id)
        stu.delete()

        res={"msg":" data deleted"}
        return JsonResponse(res, content_type='application/json')