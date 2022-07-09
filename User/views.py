from django.shortcuts import render, redirect
from .models import Profile, UserBalance
from Media.models import SocialPosts
from django.contrib.auth.views import LogoutView, LoginView
from . import forms

class logout(LogoutView):
    next_page = '/'
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class login(LoginView):
    template_name = 'User/Login.html'
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

def increase_usd(request, id):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        profile.USD_balance += 1
        profile.save()
        context = {
            'user': user,
            'profile': profile,
        }
        return render(request, 'User/profile.html', context)
    else:
        return render(request, 'User/index.html')

# Create your views here.
def index(request):
    form = forms.SocialPost()
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        posts = SocialPosts.objects.filter(user__in=profile.friends.all()) | (SocialPosts.objects.filter(user=profile))
        context = {
            'user': user,
            'profile': profile,
            'posts': posts.order_by('-creation_date')
        }
        if request.method is "POST":
            form = forms.SocialPost(request.POST)
            if form.is_valid():
                post = form.save()
        return render(request, 'User/HomePage.html', context)
    else:
        return render(request, 'User/index.html')

def Profile_page(request, id):
    if request.user.is_authenticated:
        user = request.user
        my_profile = Profile.objects.get(user=user)
        profile = Profile.objects.get(user=id)
        balance = UserBalance.objects.filter(user=id)
        # increase_balance = UserBalance.objects.get(user=id, currency_id = 1)
        context = {
            'user': user,
            'profile': profile,
            'balance': balance,
            'my_profile': my_profile,
            # 'increase_money': increase_balance.increase_balance()
        }
        return render(request, 'User/profile.html', context)
    else:
        return render(request, 'User/index.html')

def register(request):
    form = forms.NewUserForm()
    profile_form = forms.UserProfileForm
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('index')
    else:
        pass
    return render(request, 'User/Register.html', {'form': form, 'profile_form': profile_form})
