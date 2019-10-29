from django import forms
from blogapp.models import User, Article, Comment


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'category', 'img', 'short_description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)




