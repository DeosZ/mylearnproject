from django.shortcuts import render


def index(request):
    return render(request, 'news/index.html')


def create(request):
    return render(request, 'news/create.html')


def details(request):
    return render(request, 'news/details.html')


def edit(request):
    return render(request, 'news/edit.html')


def delete(request):
    return render(request, 'news/delete.html')