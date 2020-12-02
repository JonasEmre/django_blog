from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'yazar': 'Habel',
    'title': "Habel'in Makale Konusu",
    'tarih': '03/12/2020',
    'content': 'Birinci post içeriği ve görülecekler.'},
    {
        'yazar': 'Cain',
        'title': "Cain'in Makale Konusu",
        'tarih': '05/12/2020',
        'content': 'İkinci post içeriği ve görülecekler.'}]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Hakkımızda'})

# Create your views here.
