from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    email = forms.EmailField()
  
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpView, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def signup(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    
    if request.method == 'POST':
        form = SignUpView(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpView()
    return render(request, 'registration/signup.html', {'form': form, "context": context})

@login_required(login_url='signup/')
def index(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    
    if request.user.is_authenticated:
        # User is logged in, do something
        return render(request, 'accounts/profile.html', {'username': request.user.username, "context": context})
    else:
        # User is not logged in, do something else
        form = SignUpView()
        return render(request, 'registration/login.html', {'form': form , "context": context})

@login_required(login_url='registration/login.html')
def profile(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    
    return render(request, 'accounts/profile.html', context)