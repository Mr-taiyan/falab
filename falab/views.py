from django.http import HttpResponse
from django.shortcuts import render

def indexTest(request):
    """
    Test for Connectivity
    """
    return HttpResponse('Hello')

def index(request):
    """
    Temporary homepage for fun!!!
    """
    # username = request.user.get_username()
    return render(request,
                  'index.html',
                  {
                      # 'username': username,
                  })
