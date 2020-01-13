from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import UserProfile,Post
from django.db import models

from django.contrib.auth.models import (User)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password')


class ProfileAccountTypeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('account_type',)


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)

class ProfileLifeForm(forms.ModelForm):
    life_desc=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = UserProfile
        fields = ('life_desc',)

class ProfileWayForm(forms.ModelForm):
    way_desc = forms.CharField (widget=forms.Textarea (attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = UserProfile
        fields = ('way_desc',)

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class EditProfileForm(UserChangeForm):
    life_desc = forms.CharField (widget=forms.Textarea (attrs={'cols': 80, 'rows': 20}))
    way_desc = forms.CharField (widget=forms.Textarea (attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = UserProfile
        fields = ('account_type', 'profile_pic', 'life_desc', 'way_desc')


class NoteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)