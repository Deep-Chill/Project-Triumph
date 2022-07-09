from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile
from Media.models import SocialPosts

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('country', 'region', 'bio')

class SocialPost(forms.ModelForm):

    class Meta:
        model = SocialPosts
        fields = ('text',)
