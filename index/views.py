# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UploadNumber
from django.shortcuts import render
from .models import Number
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        number_form = UploadNumber(request.POST, request.FILES)
        if number_form.is_valid():
            number_form.save().get_numbers()
            number_form.save()
            return HttpResponseRedirect('/home/results')
    else: 
        number_form = UploadNumber()
    return render(request, "index/index.html", {'form':number_form})

def result(request):
    
    number = Number.objects.last()
    print(number.photo.url)
    return render(request, "index/results.html", {"number":number})
