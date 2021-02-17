from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from my_wallet.models import Investor

# Create your views here.
def create_form(request):
  return render(request, 'accounts/create_form.html')

def create_view(request):
  if request.method != 'POST':
    messages.error(request, 'Fill out all of the fields')

    return redirect('create_form')
  
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  password_verify = request.POST['password_verify']

  name_investor = request.POST['name_investor']
  risk_profile = request.POST['risk_profile']

  # Check if the PASSWORD's are iguals
  if password != password_verify:
    messages.info(request, 'The passwords dont match')

    return redirect('create_form')

  # Check if USERNAME already exists  
  if User.objects.filter(username=username).exists():
    messages.error(request, 'The username already exists')

    return redirect('create_form')

  # Check if EMAIL already exists
  if User.objects(email=email).exists():
    messages.error(request, 'The email already exists')

    return redirect('create_form')

  user = User.objects.create_user(username=username, email=email, password=password)
  user.save()

  Investor.objects.create(
    name_investor = name_investor,
    risk_profile = risk_profile
  )

  print(
    ['username={}, email={}, password={}, name_investor={}, risk_profile={}']
    .format(username, email, password, name_investor, risk_profile))

  return render(request, 'accounts/login_form')

def login_form(request):
  return render(request, 'accounts/login_form')

def login_view(request):
  if request.method != 'POST':
    messages.error(request, 'Fill out all of the fields')

    return redirect('login_form')
  
  username = request.POST['username']
  password = request.POST['password']

  user = authenticate(username=username, password=password)

  # Check if USER is validated
  if user is None:
    return redirect('login_form')

  login(request, user)

  return redirect('home')

def logout_view(request):
  logout(request)

  return redirect('logout')