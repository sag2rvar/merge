from django import forms
from .models import Post
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Comment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password','confirm_password','image','gender','phone_no')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','image','gender','phone_no')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tags', 'featured_image', 'thumbnail_image') 
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'text', 'email')
