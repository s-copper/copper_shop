from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserCreateForm, UserAddressForm, UserEditForm, UserChangePassword, UserChangeEmail
from django.views.decorators.csrf import csrf_protect
from .models import MyUser, UserAddress
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


@csrf_protect
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            UserAddress.objects.create(user=user)
            login(request, user)
            return render(request, 'users/created.html', {'user': user})
        else:
            form = UserCreateForm(request.POST)
            return render(request, 'users/create.html', {'form': form})
    form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


@csrf_protect
def profile(request, userid):
    if request.user.is_authenticated:
        user = get_object_or_404(MyUser, id=userid)
        return render(request, 'users/profile.html', {'user': user})
    else:
        return redirect('shop:ProductList')


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        return redirect('shop:ProductList')
    if request.method == 'POST':
        redirect_url = request.COOKIES['previous_url']
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            form.clean()
            login(request, form.get_user())
            return redirect(redirect_url)
        else:
            return render(request, 'users/login.html', {'form': form})
    form = AuthenticationForm()
    redirect_url = request.META.get('HTTP_REFERER')
    response = render(request, 'users/login.html', {'form': form})
    response.set_cookie('previous_url', redirect_url)
    return response


def logout_view(request):
    logout(request)
    redirect_url = request.META.get('HTTP_REFERER')
    return redirect(redirect_url)


def edit_profile(request):
    if request.user.is_authenticated:
        success = request.COOKIES.get('success', '')
        user = MyUser.objects.get(pk=request.user.pk)
        if request.method == 'POST':
            form1 = UserEditForm(data=request.POST, instance=user)
            form2 = UserAddressForm(data=request.POST, instance=user.useraddress)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                response = redirect('users:edit_profile')
                response.set_cookie('success', 'changed')
                return response
            else:
                return render(request, 'users/edit.html', {
                    'form1': form1,
                    'form2': form2
                })
        form1 = UserEditForm(instance=user)
        form2 = UserAddressForm(instance=user.useraddress)
        response = render(request, 'users/edit.html', {
            'form1': form1,
            'form2': form2,
            'success': success
        })
        response.set_cookie('success', '')
        return response
    else:
        return redirect('shop:ProductList')


@csrf_protect
def change_password(request):
    if request.user.is_authenticated:
        success = request.COOKIES.get('success', '')
        user = MyUser.objects.get(pk=request.user.pk)
        if request.method == 'POST':
            form = UserChangePassword(data=request.POST, instance=user)
            if form.is_valid():
                form.save(commit=False)
                password = form.cleaned_data["new_password1"]
                user.set_password(password)
                form.save()
                login(request, user)
                response = redirect('users:change_password')
                response.set_cookie('success', 'changed')
                return response
            else:
                return render(request, 'users/change_password.html', {'form': form})
        form = UserChangePassword(instance=user)
        response = render(request, 'users/change_password.html', {'form': form, 'success': success})
        response.set_cookie('success', '')
        return response
    else:
        return redirect('shop:ProductList')


def change_email(request):
    if request.user.is_authenticated:
        success = request.COOKIES.get('success', '')
        user = MyUser.objects.get(pk=request.user.pk)
        if request.method == 'POST':
            form = UserChangeEmail(data=request.POST, instance=user)
            if form.is_valid():
                form.save()
                response = redirect('users:change_email')
                response.set_cookie('success', 'changed')
                return response
            else:
                return render(request, 'users/change_email.html', {'form': form})
        form = UserChangeEmail()
        response = render(request, 'users/change_email.html', {'form': form, 'success': success})
        response.set_cookie('success', '')
        return response
    else:
        return redirect('shop:ProductList')


def my_reset_password_complete(request):
    if request.user.is_authenticated:
        return redirect('shop:ProductList')
    return render(request, 'users/reset_password_complete.html')
