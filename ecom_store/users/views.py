
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect



def login_user(response):
    if response.method == 'POST':

        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(response, username=username, password=password)

        if user is not None:
            # display success message
            success_msg = 'Login Successful !'
            login(response, user)
            return render(response, 'login.html',
                          {'success_msg': success_msg})
        else:
            error_msg = 'Username or password not found'
            return render(response, 'login.html', {'error_msg': error_msg})

    return render(response, 'login.html', {})


# Register for account here
@csrf_protect
def register(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')
        password2 = response.POST.get('password')

        if not username:
            error_msg = "Username is required"
            return render(response, 'register.html', {'error_msg': error_msg})

        elif User.objects.filter(username=username).exists():
            error_msg = "Username already exists"
            return render(response, 'register.html', {'error_msg': error_msg})

        elif not password:
            error_msg = "Password is required"
            return render(response, 'register.html', {'error_msg': error_msg})

        elif password != password2:
            error_msg = "Passwords do not match"
            return render(response, 'register.html', {'error_msg': error_msg})
        else:
            if response.user.is_authenticated:  # makes sure we won't log user in if they are already logged in
                error_msg = 'Please log out before creating new account !'
                return render(response, 'register.html',
                              {'error_msg': error_msg, })
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                user = authenticate(response, username=username, password=password)
                login(response, user)  # login here
                success_msg = 'User registered and logged in ! '
                return render(response, 'register.html', {'success_msg': success_msg})

    return render(response, 'register.html', {})


# Confirm with user that they want to log out
def logout_user(response):
    if response.method == 'POST':
        user_choice = response.POST.get('logout-form')
        if 'confirm' in user_choice:
            print('confirm')
            logout(response)
            success_msg = 'Logged out, see you next time ! '
            return render(response, 'logout.html', {'success_msg': success_msg})

            # logout here
        else:
            print('cancel')
            pass
            # do not logout
    return render(response, 'logout.html', {})


# Page for managing accounts ex: change pwd
def accounts(response):
    return render(response, 'accounts.html', {})
