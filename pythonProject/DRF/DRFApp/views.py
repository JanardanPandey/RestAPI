import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

# Create your views here.
@csrf_exempt
def postdata(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'Data Created'}
            #res = JSONRenderer().render(msg)
            #return HttpResponse(res, content_type='application/json')
            return JsonResponse(msg, safe = False)
        res = JSONRenderer().render(serializer.errors)
        return HttpResponse(res, content_type='application/json')

    if request.method == 'PUT':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        pytondata = JSONParser().parse(stream)
        id = pytondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializers(stu, data=pytondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated'}
            msg = JSONRenderer().render(res)
            return HttpResponse(msg, content_type='application/json')
        msg = JSONRenderer().render(serializer.errors)
        return HttpResponse(msg, content_type='application/json')

    if request.method == 'GET':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = StudentSerializers(stu)
            jsondata = JSONRenderer().render(serializers.data)
            return HttpResponse(jsondata, content_type='appliction/json')

        stu = Student.objects.all()
        serializers = StudentSerializers(stu, many=True)
        jsondata = JSONRenderer().render(serializers.data)
        return HttpResponse(jsondata, content_type='appliction/json')

    if request.method== 'DELETE':
        json_data= request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        #res = {'msg':'data deleted'}
        #json_res = JSONRenderer().render(res)
        stud = Student.objects.all()
        serializers = StudentSerializers(stud, many=True)
        json_stud = JSONRenderer().render(serializers.data)
        return HttpResponse(json_stud, content_type='application/json')
