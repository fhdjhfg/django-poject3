from django.shortcuts import render

# Create your views here.
def test (request):
    return render(request,'test.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')