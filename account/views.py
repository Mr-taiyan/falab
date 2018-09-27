from django.shortcuts import render

# Create your views here.
def signup(request):
    """
    Sign up page for account app
    """
    return render(request,
                  'accounts/signup.html',
                  {

                  })

def login(request):
    """
    Sign in page for account app
    """
    return render(request,
                  'accounts/login.html',
                  {

                  })
