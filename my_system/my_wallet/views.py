from django.shortcuts import render, redirect
from datetime import datetime

from django.contrib.auth.models import User
from .models import Operation, Investor

# Create your views here.
def home(request):
  return render(request, 'my_wallet/home.html')

#TODO: The user need to be connected
def new_operation_form(request):
  return render(request, 'my_wallet/new_operation.html')

def new_operation_view(request):
  if request.method != 'POST':
    print('The method isnt POST')

    return redirect('home')

  if not request.user.is_authenticated:
    print('User isnt authenticated')

    return redirect('home')

  share_name = request.POST['share_name']
  number_shares = request.POST['number_shares']
  unit_share_price = request.POST['unit_share_price']
  tax = request.POST['tax']
  type_operation = request.POST['type_operation']

  date = datetime.now()

  user = request.user
  investor = Investor.objects.get(user=user)

  operation = Operation(
    share_name = share_name,
    number_shares = number_shares,
    unit_share_price = unit_share_price,
    tax = tax,
    operation_type = type_operation,
    date = date,
    investor = investor
  )

  operation.save()

  return redirect('home')

def list_same_share_operations_form(request):
  pass