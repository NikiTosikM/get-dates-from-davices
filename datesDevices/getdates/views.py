from django.shortcuts import render, HttpResponse
from .forms import FormSystemParamets

# Create your views here.
def getMainPage(request):
    if request.method == 'POST':
        
        form = FormSystemParamets(request.POST)

        if form.is_valid():

            if 'functionality check' in request.POST.keys():
                form = FormSystemParamets(request.POST)

                return render(request, 'getdates/main site page.html', context={'form': form})

            else:
                form.save()

                form = FormSystemParamets()

                return render(request, 'getdates\main site page.html', context={'form': form})

    else:
        form = FormSystemParamets()

        return render(request, 'getdates\main site page.html', context={'form': form})
