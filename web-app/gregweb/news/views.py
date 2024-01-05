from django.shortcuts import render
from .models import Artiles
from .form import ArtilesForm


def news(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return request('news')
        else:
            error = 'ФОРМА БЫЛА НЕ ВЕРНОЙ'
    form = ArtilesForm()

    data = {
        'form':form,
        'error':error
    }
    return render(request, 'news/create.html', data)
