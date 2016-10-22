from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'the_wall/index.html')

def create_post(request):
    print request.POST['post']

    return redirect('/')
