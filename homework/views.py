from django.shortcuts import render
import datetime


def eng_view(request):
    text = ['«We are the champions, my friends', "And we'll keep on fighting till the end»",
            'Queen, We are the champions']

    model = request.GET.get('model')

    if model == 'budslive':
        return render(request, 'homework/headphones.html', context={
            'text': 'BUDS LIVE',
            'url': 'https://img.tvc-mall.com/uploads/details/680901947A-1.jpg'
        })

    if model == 'airpods':
        return render(request, 'homework/headphones.html', context={
            'text': 'AIRPODS',
            'url': 'https://iphoriya.ru/wp-content/uploads/airpods-pro-2022.jpeg'
        })

    return render(request, 'homework/main.html', context={
        'text': text
    })


def fr_view(request):
    text = ['«Nous sommes les champions Mes amis', "Et nous continuerons à nous battre jusqu'à la fin»",
            'Queen, We are the champions']

    return render(request, 'homework/main.html', context={
        'text': text
    })


def de_view(request):
    text = ['«Wir sind die Champions, meine Freunde', "Und wir werden bis zum Ende weiterkämpfen»",
            'Queen, We are the champions']

    return render(request, 'homework/main.html', context={
        'text': text
    })


def es_view(request):
    text = ['«Somos los campeones mis amigos', "Y seguiremos luchando hasta el final»",
            'Queen, We are the champions']

    return render(request, 'homework/main.html', context={
        'text': text
    })


def toyota_view(request):
    text = 'TOYOTA'
    url = 'https://rg.ru/uploads/images/2023/03/23/76_352.jpg'
    return render(request, 'homework/cars.html', context={
        'text': text,
        'url': url
    })


def honda_view(request):
    text = 'HONDA'
    url = 'https://www.aoyama.ru/pix/auto/accord/accord_1400.png'
    return render(request, 'homework/cars.html', context={
        'text': text,
        'url': url
    })


def renault_view(request):
    text = 'RENAULT'
    url = 'https://motor.ru/imgs/2021/01/21/07/4467330/2361cc5f72c2c9a146d0c4bfc161d4d6ca2493e8.jpg'
    return render(request, 'homework/cars.html', context={
        'text': text,
        'url': url
    })


def today_day(request):
    today = datetime.datetime.today()
    weekday = datetime.datetime.isoweekday(today)
    week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    colors = ['green', 'yellow', 'red', 'blue', 'orange', 'purple', 'pink']
    return render(request, 'homework/today.html', context={
        'day': week[weekday - 1],
        'color': colors[weekday - 1]
    })