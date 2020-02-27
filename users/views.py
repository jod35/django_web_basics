from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
        	form.save()
        	username=form.cleaned_data.get('username')
        	messages.success(request,f"Account for {username} has been created successfully")
        	return redirect('blog_home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
