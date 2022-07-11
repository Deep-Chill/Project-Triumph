from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile
from Location.models import Country, Region
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.none()


class SocialPostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    class Meta:
        model = SocialPosts
        fields = ['text']
