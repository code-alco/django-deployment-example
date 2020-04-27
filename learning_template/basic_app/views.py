from django.shortcuts import render

# Create your views here.
def index(request):
    dict={'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context=dict)
def other(request):
    return render(request,'basic_app/other.html')
def relative(r):
    return render(r,'basic_app/relative.html')
