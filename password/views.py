from django.shortcuts import render, redirect
from password.models import passwords
from login.urls import path
import requests
import random
import string
import json
import base64

# Create your views here.

url = "https://logo4.p.rapidapi.com/logo/amazon.com"

headers = {
    "X-RapidAPI-Key": "ce3ab88910msh7ee1ff64510fe4fp19d55ejsn0bb4bc9e36d1",
    "X-RapidAPI-Host": "logo4.p.rapidapi.com"
}

response = requests.get(url, headers=headers)


def generate():
    ss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=+{[]}'
    s = ''

    for i in range(15):
        s += random.choice(ss)
    return s


def saved(request, em, val):
    if request.method == 'POST':
        site = request.POST['site']
        pas = request.POST['password']

        url = f"https://api.brandfetch.io/v2/brands/{site}"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer lUaO4eqfYYJUVN1O+jZmDeNDcjOnA6LLGJBZmd/51pI="
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            logo_url = data.get('logos', [{}])[3].get(
                'formats', [{}])[0].get('src')
        else:
            logo_url = 'https://lh3.googleusercontent.com/05m3CO1Wi8si9ienyCy78gqfVCDo9thVtCSdReNuFxrFedCMsy2NwQfLefqhFkGfNTz3UztUX2QTp1KkmaTykIp0y_M3ritQmSE4JA=w1064-v0'
        # if response.status_code == 200:
        #     try:
        #         logo_data = response.json()
        #     except json.JSONDecodeError:
        #         # Handle the case where the JSON data is empty or invalid
        #         logo_data = None
        # else:
        #     # Handle the case where the API request fails or returns an error
        #     logo_data = None

        # if logo_data is not None:
        #     logo_data_encoded = json.dumps(logo_data).encode('utf-8')
        #     logo_data_base64 = base64.b64encode(logo_data_encoded)
        # else:
        #     logo_data_base64 = None

        if len(pas) == 0:
            pas = generate()

        if len(site) != 0:
            if passwords.objects.filter(ste=site, username=em).exists():
                return redirect('pas', em=em, val=val)
            else:
                # if logo_data is not None:
                #     logo_data_encoded = json.dumps(logo_data).encode('utf-8')
                # else:
                #     logo_data_encoded = None

                password_obj = passwords(
                    ste=site, password=pas, username=em, logo=logo_url)
                password_obj.save()

                passes = passwords.objects.filter(username=em).all()
                context = {'passes': passes, 'em': em,
                           'val': val, 'logo': logo_url}
                return render(request, 'password.html', context)
        else:
            return redirect('pas', em=em, val=val)
    else:
        return render(request, 'password.html')


def pas(request, em, val):
    passes = passwords.objects.filter(username=em).all()
    context = {'passes': passes, 'em': em, 'val': val}
    return render(request, 'password.html', context)


def dela(request, em, val, ste):

    obj = passwords.objects.get(ste=ste)
    obj.delete()

    return redirect('pas', em, val)


def logu(request, val):
    val = False
    return redirect('log')
