from django.shortcuts import render


# Create your views here.
def setcookie(request):
    response = render(request,  'setcookie.html')
    # instead of returning it, we will save it in a response variable
    response.set_cookie('name', 'django')
    return response


def getcookie(request):
    nm = request.COOKIES['name']
    return render(request, 'getcookie.html', {'xyz': nm})


def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response


def my_view(request):
    # Store a value in the session
    request.session['my_key2'] = 'my_value2'


def my_other_view(request):
    my_view(request)
    # Retrieve a value from the session
    result = request.session.get('my_key2')
    return render(request, 'session_demo.html', {'session_name': result})


def my_third_view(request):
    # Remove a value from the session
    del request.session['my_key']


def my_newview(request):
    # Get the session ID
    session_id = request.session.session_key
    return render(request, 'session_demo2.html', {'session_id': session_id})

