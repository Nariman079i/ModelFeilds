from django.shortcuts import render
from .models import *


# Create your views here.

def index(requests):
    int_post = IntFields()
    file = 'main/index.html'
    context = {
        'post': int_post
    }
    return render(requests, file, context=context)