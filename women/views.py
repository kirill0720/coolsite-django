from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse(f"<h1>Пустая страница</h1>")


def contact(request):
    return HttpResponse(f"<h1>Пустая страница</h1>")


def login(request):
    return HttpResponse(f"<h1>Пустая страница</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat,
    }
    return render(request, 'women/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_category(request, cat_slug):
    context = {
        'menu': menu,
        'title': 'Отображение по рубрикам страница',
        'cat_selected': cat_slug,
    }

    return render(request, 'women/index.html', context=context)
