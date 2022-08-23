from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_, logout as logout_
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MemberProfile
from .forms import CustomUserCreationForm, LoginForm, MemberProfileForm


def index(request):
    if request.user.is_authenticated:
            return redirect('profile/')
    
    return render(request, "user/index.html", {})


def logout(request):
    logout_(request)
    return redirect("/")


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        form = LoginForm()
        next = request.GET.get("next")
        context = {
            'form': form,
            'next': next
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        next = request.POST.get("next")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login_(request, user)
                if next:
                    return redirect(next)
                return redirect('profile')
            else:
                return redirect('login')

                
class SignUp(View):
    
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)


class MemberProfileView(LoginRequiredMixin, View):
    
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request):
        profile = MemberProfile.objects.get(username= request.user.username)
        form = MemberProfileForm(instance= profile)
        context = {
            'form': form,
            'image': profile.img
        }
        return render(request, 'user/profile.html', context)

    def post(self, request):
        profile = MemberProfile.objects.get(username= request.user.username)
        form = MemberProfileForm(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
        return redirect('profile')