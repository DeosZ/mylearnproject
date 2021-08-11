from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_up(request):
    data = dict()   # словарь данных
    if request.method == 'GET':
        return render(request, 'account/sign_up.html')
    elif request.method == 'POST':
        # получение данных из формы
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # отправка даннх

        data['login_x'] = login_x
        data['pass1_x'] = pass1_x
        data['pass2_x'] = pass2_x
        data['email_x'] = email_x

        # Сoхранение даных в базе
        user = User.objects.create_user(login_x, email_x, pass1_x)
        user.save()
        if user is None:
            data['color_x'] = 'red'
            data['report_x'] = 'В регистрации отказано'
        else:
            data['color_x'] = 'green'
            data['report_x'] = 'Успех регистрации'

        # загрузка страницы отчёта
        data['caption'] = 'отчёты по регистрации'
        return render(request, 'account/reports.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        return render(request, 'account/sign_in.html')
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        passw_x = request.POST.get('pass1')
        user = authenticate(request, username=login_x, password=passw_x)
    if user is None:
        data['color_x'] = 'red'
        data['report_x'] = 'Пользователь не найден!'
        return render(request, 'account/reports.html', context=data)
    else:
        login(request, user)
        data['color_x'] = 'green'
        data['report_x'] = 'Пользователь авторизован!'
        return render(request, 'account/reports.html', context=data)



def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    return render(request, 'account/profile.html')


def ajax_reg(request):
    response = dict()
    login_x = request.GET.get('login')
    try:
        User.object.get(username=login_x)
        response['message'] = 'занят'
    except User.DoesNoteExist:
        response['message'] = 'свободен'
    return JsonResponse(response)

