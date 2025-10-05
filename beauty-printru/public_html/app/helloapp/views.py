from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    if request.method == 'POST':
        return HttpResponse("Привет, МИР!")
    return render(request, 'hello.html')