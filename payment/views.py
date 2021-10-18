from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse

def index(request):
  return render(request, 'payment/index.html', { 'a' : 'a' })

def subscription(request):
  return JsonResponse({'foo': 'bar'})