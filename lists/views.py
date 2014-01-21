from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
import sys

def home_page(request):
  if request.method == 'POST':
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text)
    return redirect('/')

  return render(request, 'home.html')
