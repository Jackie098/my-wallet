from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Sum
from datetime import datetime

from django.contrib.auth.models import User
from .models import Operation, Investor

# Create your views here.
def home(request):
  if request.user.is_authenticated:
    user = request.user
    investor = Investor.objects.get(user=user)

    # Operations separate per SHARE_NAME, counting the instances, average and sum.
    operations = Operation.objects.values('share_name').annotate(sum_shares=Sum('number_shares'), avg=Avg('unit_share_price'), sum=Sum('amount')).filter(investor=investor)
    # operations_purchased = Operation.objects.values('share_name').annotate(dcount=Count('share_name'), sum=Sum('amount')).filter(investor=investor, operation_type='PS')
    # operations_selled = Operation.objects.values('share_name').annotate(dcount=Count('share_name'), sum=Sum('amount')).filter(investor=investor, operation_type='SL')
    # TODO: Équivo a lógica atual, pois estou somando o histórioc de operaçoçes
    # O correto seria somar as operações que estão abertas, baseado na carteira atual e na data
    wallet = Operation.objects.filter(investor=investor, operation_type='PS').aggregate(sum=Sum('amount'))
    context = {
      "investor": investor,
      "operations": operations,
      "wallet": wallet,
    }

    return render(request, 'my_wallet/home.html', context=context)
  else:
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
def list_operations(request):
  user = request.user
  investor = Investor.objects.get(user=user)

  # if method is POST, return the query filtered
  if request.method == 'POST':
    filtrate = request.POST['filtrate']

    operations = Operation.objects.filter(investor=investor, share_name=filtrate)
  else:
    operations = Operation.objects.filter(investor=investor)

  context = {
    'operations': operations
  }

  return render(request, 'my_wallet/list_operations.html', context=context)