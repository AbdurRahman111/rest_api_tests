from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import staff_info, staff_salary
from .serializers import staff_info_serializers, staff_salary_serializers, staff_ratings_serializers
from django.contrib.auth import authenticate, login, logout




@csrf_exempt
def show_multiple_results_from_database(request):
    all_staffs = staff_info.objects.all()
    var_staff_info_serializers = staff_info_serializers(all_staffs, many=True)
    json_data = JSONRenderer().render(var_staff_info_serializers.data)

    all_staffs = staff_info.objects.all()
    var_staff_info_serializers = staff_info_serializers(all_staffs, many=True)
    json_data = JSONRenderer().render(var_staff_info_serializers.data)

    all_staffs = staff_info.objects.all()
    var_staff_info_serializers = staff_info_serializers(all_staffs, many=True)
    json_data = JSONRenderer().render(var_staff_info_serializers.data)








@csrf_exempt
def one_salary(request):
    id = request.POST.get('id')
    getSalary= staff_salary.objects.filter(id=id)
    if getSalary:
        getSalary= staff_salary.objects.get(id=id)

        serializer_var = staff_salary_serializers(getSalary, many=False)

        json_data = JSONRenderer().render(serializer_var.data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        mag = {'massage': 'Staff is not exist !'}
        json_data = JSONRenderer().render(mag)
        return HttpResponse(json_data, content_type='application/json')





@csrf_exempt
def staff_info_see(request):

    # mag = {'massage': 'Data is Deleted'}
    # json_data = JSONRenderer().render(mag)
    # return HttpResponse(json_data, content_type='application/json')
    id = request.POST.get('id')
    print(id)
    getStaff= staff_info.objects.get(id=id)
    serializer_var = staff_info_serializers(getStaff, many=False)

    json_data = JSONRenderer().render(serializer_var.data)
    return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def see_all_staffs(request):

    getStaff= staff_info.objects.all()
    serializer_var = staff_info_serializers(getStaff, many=True)

    json_data = JSONRenderer().render(serializer_var.data)
    return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def staff_create(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    name = request.POST.get('name')
    roll = request.POST.get('roll')
    address = request.POST.get('address')
    adsd = request.POST.get('adsd')
    print(username, password, name, roll, address, adsd)

    user = authenticate(username=username, password=password)
    if user is not None:
        var_staff_info = staff_info(name=name, roll=roll, address=address, adsd=adsd)
        var_staff_info.save()
        mag = {'massage': 'Staff is created !'}
        json_data = JSONRenderer().render(mag)
        return HttpResponse(json_data, content_type='application/json')
    else:
        mag = {'massage': 'Error: You are not authorized !'}
        json_data = JSONRenderer().render(mag)
        return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def staff_update(request):

    updated_staff_id = request.POST.get('updated_staff_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    name = request.POST.get('name')
    roll = request.POST.get('roll')
    address = request.POST.get('address')
    adsd = request.POST.get('adsd')
    print(username, password, name, roll, address, adsd)

    user = authenticate(username=username, password=password)
    if user is not None:
        var_staff_info = staff_info.objects.filter(id=updated_staff_id)
        if var_staff_info:
            getvar_staff_info = staff_info.objects.get(id=updated_staff_id)
            getvar_staff_info.name=name
            getvar_staff_info.roll=roll
            getvar_staff_info.address=address
            getvar_staff_info.adsd=adsd
            getvar_staff_info.save()
            mag = {'massage': 'Staff is updated !'}
            json_data = JSONRenderer().render(mag)
            return HttpResponse(json_data, content_type='application/json')
        else:
            mag = {'massage': 'Staff is not exist !'}
            json_data = JSONRenderer().render(mag)
            return HttpResponse(json_data, content_type='application/json')


    else:
        mag = {'massage': 'Error: You are not authorized !'}
        json_data = JSONRenderer().render(mag)
        return HttpResponse(json_data, content_type='application/json')
