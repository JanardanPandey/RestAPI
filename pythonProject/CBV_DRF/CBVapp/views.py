import io

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .serializers import StudentSerializers
from .models import Student
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
 def get(self,request, *args,**kwargs):
  json_data = request.body
  stream = io.BytesIO(json_data)
  pythondata = JSONParser().parse(stream)
  id = pythondata.get('id', None)
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer=StudentSerializers(stu)
   json_data = JSONRenderer().render(serializer.data)
   return HttpResponse(json_data, content_type='application/json')
  stu = Student.objects.all()
  serializers=StudentSerializers(stu, many=True)
  json_data= JSONRenderer().render(serializers.data)
  return HttpResponse(json_data, content_type='application/json')
 
 def post(self,request,*args,**kwargs):
  jsondata = request.body
  stream = io.BytesIO(jsondata)
  pythondata = JSONParser().parse(stream)
  serializers = StudentSerializers(data=pythondata)
  if serializers.is_valid():
   serializers.save()
   res = {'msg':'data created'}
   return JsonResponse(res,content_type='application/json')
  res = serializers.errors
  return JsonResponse(res, content_type='application/json')

 def put(self,request,*args,**kwargs):
  jsondata = request.body
  stream = io.BytesIO(jsondata)
  pythondata = JSONParser().parse(stream)
  id = pythondata.get('id')
  stu = Student.objects.get(id=id)
  serializer = StudentSerializers(stu, pythondata, partial=True)
  if serializer.is_valid():
   serializer.save()
   res = {'msg':'data updated'}
   return JsonResponse(res, content_type='application/json')
  res = {'msg':serializer.errors}
  return JsonResponse(res,content_type='application/json')

 def delete(self,request,*args,**kwargs):
  data = request.body
  stream = io.BytesIO(data)
  pythondata = JSONParser().parse(stream)
  id = pythondata.get('id')
  stu = Student.objects.get(id=id)
  stu.delete()
  stud = Student.objects.all()
  serilizer = StudentSerializers(stud,many=True)
  jsonstud = JSONRenderer().render(serilizer.data)
  return HttpResponse(jsonstud, content_type='application/json')