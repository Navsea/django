from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "blog/index.html");

def posts(request):
    return HttpResponse("ALL THE POSTS");

def post(request, post_id):
    return HttpResponse("SINGLE POST: " + post_id);