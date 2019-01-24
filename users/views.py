from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserCreateForm
from django.views.decorators.csrf import csrf_protect
from .models import MyUser
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return render(request, 'users/created.html')
    form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


def profile(request, userid):
    user = get_object_or_404(MyUser, id=userid)
    return render(request, 'users/profile.html', {'user': user})


@csrf_protect
def login_view(request):
    redirect_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        return redirect('shop:ProductList')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.get_user())
            return redirect('shop:ProductList')
        else:
            return render(request, 'users/login.html', {'form': form})
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('shop:ProductList')
