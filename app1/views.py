from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_html(request):
    return render(request,'index.html')

def string_response(request):
    return HttpResponse('HI, This is my Training poc')