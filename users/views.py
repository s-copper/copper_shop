from django.shortcuts import render
from .forms import UserCreateForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/created.html')
    form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})
