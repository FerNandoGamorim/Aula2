from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.

#@method_decorator(login_required, name='dispatch')
#class HomePageView(TemplateView):
#   template_name = 'home.html'


#@login_required
def index(request):
    return render(request,"index.html")

def londrina(request):
    return render(request,"londrina.html")  

def calculadora(request):
    return render(request,"calculadora.html")      

def form_namehtml(request):
    return render(request,"form_name.html")
                                



