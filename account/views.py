from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    """
    Sign in page for account app
    """
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,
                              'accounts/sign.html',
                              {
                                  'error': 'Username has already been taken.',
                              })
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'],
                                                email=request.POST['email'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request,
                          'accounts/signup.html',
                          {
                              'error': 'Passwords must be matched!',
                          })
    else:
        return render(request,
                      'accounts/signup.html',
                      {

                      })

def login(request):
    """
    Login page
    """
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],
                          password=request.POST['password'],)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request,
                          'accounts/login.html',
                          {
                              'error': 'Username or password is incorrect!',
                          }
                          )
    else:
        return render(request,
                      'accounts/login.html',
                      {
                      }
                      )

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index')
