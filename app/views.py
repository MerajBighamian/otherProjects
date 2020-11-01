from django.shortcuts import render
from random import choice


# Create your views here.

def index(requests):
    context = {
        'hello': 'Hello To WebApp for Generator Password'
    }
    return render(requests, 'app/index.html', context)


def password(requests):
    ''' character for generate password'''
    characterOfPassword = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefjssdcngavx1234567890@#!~*&'
    passGenerated = ''
    for i in range(8):
        passGenerated += choice(characterOfPassword)
    context = {
        'password': passGenerated,
    }

    return render(requests, 'app/passwordgenrator.html', context)
