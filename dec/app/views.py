from django.shortcuts import render, redirect
from .forms import ShowProd
from .models import Prod


def index(request):
    if request.method == 'POST':
        return redirect('create')
    prod = Prod.objects.all()
    return render(request, 'app/index.html', context={'prod': prod})


def create(request):
    if request.method == 'POST':
        form = ShowProd(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            description = form.cleaned_data['description']

            prod, _ = Prod.objects.get_or_create(name=name, price=price,
                                                count=count,
                                                description=description)
            return redirect('index')
        else:
            form = ShowProd()
            return render(request, 'app/create.html', context={'form': form})
    else:
        form = ShowProd()
        return render(request, 'app/create.html', context={'form': form})
