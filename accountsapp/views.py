from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegistrationForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegistrationForm()
    context = {'form': form}

    return render(request, 'registration.html', context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            # Just example of context and rendering
            # template=load.get_template('register.html')
            # context = {'k1': 'django'}
            # return HttpResponse(template.render(context, request))
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    print('Email already registered.')
                    messages.info(request, 'Email already registered.')
                    return redirect('register')
                else:
                    u1 = User.objects.create_user(
                        username=username, email=email, password=password1,
                        first_name=first_name, last_name=last_name)
                    u1.save()
                    print("Success....")
                    return redirect('login')
            else:
                print('Password does not match.')
                messages.info(request, 'Password does not match. ')
                return redirect('register')
        except Exception:
            if User.objects.filter(username=username).exists():
                print('User id already exists.')
                messages.info(request, 'User id already exists.')
                return redirect('register')

        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials.')
            print('Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
