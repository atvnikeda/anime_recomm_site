from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

# Create your views here.
def signup(request):
    """signup
    サインアップ
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})

def signin(LoginView):
    """signin
    サインイン
    """
    form_class = forms.LoginForm
    template_name = "accounts/signin.html"
