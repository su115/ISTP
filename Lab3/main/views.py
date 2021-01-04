from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import os
def MyView(request):
    return render(request, 'main.html',{'selector':'value'})
def MyJson(request):
    resault={
            'word1':'value1',
            'word2':'value2',
            'word3':'value3',
            'word4':'value4',
            'word5':'value5',
            }
    return JsonResponse(resault)
