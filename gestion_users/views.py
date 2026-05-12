from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# READ
def user_list(request):
    users = User.objects.all()
    return render(request, 'gestion_users/user_list.html', {'users': users})

# CREATE
def add_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('user_list')

    return render(request, 'gestion_users/user_form.html', {'form': form})

# UPDATE
def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('user_list')

    return render(request, 'gestion_users/user_form.html', {'form': form})

# DELETE
def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    user.delete()

    return redirect('user_list')