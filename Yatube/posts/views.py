from django.shortcuts import render
from django.http import HttpResponse
# Импортируем загрузчик.

# Главная страница
def index(request):    
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context) 

def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = f'Здесь будет информация о группах проекта Yatubes {slug}'
    slug = "test"
    context = {
        'text': text,
    }
    return render(request, template, context)