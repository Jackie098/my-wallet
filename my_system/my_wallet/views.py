from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.contrib.auth.models import User
from .models import Operation, Investor

# Create your views here.
def home(request):

  #calculos

  #contexto

  return render(request, 'my_wallet/home.html')

@login_required
def new_operation_form(request):
  return render(request, 'my_wallet/new_operation.html')

@login_required
def new_operation_view(request):
  if request.method != 'POST':
    print('The method isnt POST')

    return redirect('home')

  share_name = request.POST['share_name']
  number_shares = float(request.POST['number_shares'])
  unit_share_price = float(request.POST['unit_share_price'])
  brokerage_cost = float(request.POST['brokerage_cost'])
  type_operation = request.POST['type_operation']

  date = datetime.now()

  user = request.user
  investor = Investor.objects.get(user=user)

  # Business Rule
  e = 0.00003125
  l = 0.000275

  trading_value = number_shares * unit_share_price

  emoluments = trading_value * e
  settlement_cost = trading_value * l
  tax = emoluments + settlement_cost + brokerage_cost

  if type_operation == 'PS':
    amount = trading_value + tax
  else:
    amount = trading_value - tax

  operation = Operation(
    share_name = share_name,
    trading_value = trading_value,
    number_shares = number_shares,
    unit_share_price = unit_share_price,
    tax = tax,
    amount = amount,
    operation_type = type_operation,
    date = date,
    investor = investor
  )

  operation.save()

  return redirect('home')

@login_required
def list_same_share_operations_form(request):
  pass