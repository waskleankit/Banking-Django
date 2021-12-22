from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def index(request):
    message = " <h4>Hello world. this is CustomerApp.</h4>"
    message = message + "<br><a href='all_customer/'> All Customer</a>"
    message = message + "<br><a href='add_customer/'> Add Customer</a>"
    return HttpResponse(message)

def add_customer(request):
    return render(request, 'CustomerApp/add_customer.html')
    # content = "<input type='text' placeholder='customer name' />"
    # content = content + "<br><input type='button' value='Submit' />"
    # return HttpResponse(content)

def all_customer(request):
    latest_customer_list = Customer.objects.all()
    context = {'latest_customer_list': latest_customer_list,}
    return render(request, 'CustomerApp/customer_list.html',context)

from django.shortcuts import get_object_or_404
def customer_detail(request,customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer,}
    return render(request, 'CustomerApp/customer_details.html',context)

# fuction to recieve and process add_customer from data
from django.utils import timezone
def add(request):
    name = request.POST['name']
    gender = request.POST['gender']
    balance = request.POST['balance']
    acc_type = request.POST['acc_type']
    acc_no = request.POST['acc_no']

    message = ""
    try:
        customer = Customer(name=name,gender=gender,balance=balance,account_no=acc_no,account_type=acc_type,pub_date=timezone.now())
        customer.save();
        message = "Customer data saved!!!"
    except:
        message = "Customer data save failed ,try again."

    context = {'message':message}
    return render(request, 'CustomerApp/add_customer.html',context)

def customer_delete(request,customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    message = ""
    try:
        customer.delete();
        message = "Customer Deleted!!!"
    except:
        message = "Customer deletion failed ,try again."
    message = message + "<br><br><a href='../../all_customer/'>Back</>"

    return HttpResponse(message)
# rest-framework
# django -rest-framework
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializers

@csrf_exempt
def customer_json_list(request):
    """ List all code snippets,or create a new snippet"""
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializers(customers,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def customer_json_detail(request,pk):
    """ Retrive ,update or delete a code customer"""
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = CustomerSerializers(customer)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializers(customer,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    if request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)
