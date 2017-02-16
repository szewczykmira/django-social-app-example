from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')


def done(request):
    return render(request, 'app/done.html')
