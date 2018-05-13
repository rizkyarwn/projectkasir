from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.views import logout

def login(request):
    template_name = 'app_user/user_login.html'
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home_page')
        else:
            context.update({'error_message': 'User tidak ada!'})
            return render(request, template_name, context)
    return render(request, template_name, context)

def logout(request):
    auth_logout(request)
    return redirect('login_page')

