from django.shortcuts import render, HttpResponse
from .forms import FormSystemParamets

# Create your views here.
def getMainPage(request):
    forms = FormSystemParamets()
    return render(request, 'getdates/main site page.html', context={'form':forms})