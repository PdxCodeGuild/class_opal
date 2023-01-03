from django.shortcuts import render, redirect
from .models import BothUrl
from .forms import URLForm
import random

def urlCode(request): # gets long URL from user and generates a short code (short URL) & then saves that and the long form as a matched pair in database
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            options = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            new_url = BothUrl.objects.create(
                long_url = form.cleaned_data["long_url"],
                short_code = ''.join(random.choice(options) for i in range(10)),
            )
            return redirect('/')
    else:
        form = URLForm()
    data = BothUrl.objects.all()
    data_list = []
    for i in data:
        data_list.append(str(i)) #w/o converting the data here to a string, the data remains a special class that can't be returned
    #print(type(data_list[0])) - used to see what type the data is
    context = {
        'form': form,
        'data': data_list,
    }
    return render(request, 'url_short/index.html', context)


def urlRedirect(request, short_codes):
    data = BothUrl.objects.get(short_code=short_codes)
    print(data)
    return redirect(data.long_url)#long_url makes it so when you click the link it goes to the original website / follows the long_url