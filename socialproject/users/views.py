from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("Login Successful")
            else:
                return HttpResponse("Login Failed")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')