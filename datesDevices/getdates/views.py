from django.shortcuts import render, HttpResponse
from .forms import FormSystemParamets

# Create your views here.
def getMainPage(request):
    if request.method == 'POST':
        
        form = FormSystemParamets(request.POST)


        if form.is_valid():

            user_dates = form.cleaned_data

            search_user_dates = {}

            for name_field, field in user_dates.items():
                search_user_dates[name_field] = field

            print(search_user_dates, 'все ок')

            

            form.save()
            form = FormSystemParamets()

            return render(request, 'getdates\main site page.html', context={'form': form})

    else:
        form = FormSystemParamets()

        return render(request, 'getdates\main site page.html', context={'form': form})
