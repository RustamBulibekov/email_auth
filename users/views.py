from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render, redirect

from .forms import OwnUserCreationForm


class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': OwnUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = OwnUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, template_name='registration/register.html', context=context)
