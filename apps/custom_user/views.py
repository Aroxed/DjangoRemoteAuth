from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from apps.custom_user.forms import LoginForm


def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('OK. Username is %s, IsAuthenticated = %s'
                                    % (user.username, user.is_authenticated))
            else:
                return HttpResponse('NOT AUTHENTICATED')
        else:
            return HttpResponse('NOT AUTHENTICATED')
    form = LoginForm()
    return render(request, "login.html", {'form': form})
