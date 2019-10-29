from django.shortcuts import render, redirect, get_object_or_404
from blogapp.forms import UserForm, ArticleForm, CommentForm
from blogapp.models import Article, Comment, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
import datetime

# Create your views here.


def red(request):
    return redirect(home)


"""
Представление базовой страницы с выводом статей, которые прошли модерацию
"""


def home(request):
    articles = Article.objects.filter(moderation=True)

    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page', 1)

    page = paginator.get_page(page_number)

    return render(request, 'blogapp/home.html', {
        'page': page,
    })


"""
Регистрация пользователя
"""


def sign_up(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create_user(**user_form.cleaned_data)

            return redirect(home)

    return render(request, 'blogapp/sign_up.html', {
        'user_form': user_form,
    })


"""
Вывод статей по определнной категории
"""


def category(request, pk):
    article_by_category = Article.objects.filter(category=pk)
    paginator = Paginator(article_by_category, 2)
    page_number = request.GET.get('page', 1)

    page_article_by_category = paginator.get_page(page_number)
    return render(request, 'blogapp/category.html', {
        'article_by_category': article_by_category,
        'page_article_by_category': page_article_by_category
    })


"""
Вывод полной статьи с комментариями и формой для их добавления
"""


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    users = User.objects.all()
    comments = Comment.objects.filter(post=pk)

    paginator = Paginator(comments, 2)
    page_number = request.GET.get('page', 1)

    page_comments = paginator.get_page(page_number)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.name = request.user
            form.post = article
            form.save()
            return redirect(article_detail, pk)
    else:
        form = CommentForm()

    return render(request, 'blogapp/article.html', {
        'article': article,
        'form': form,
        'comments': comments,
        'users': users,
        'page_comments': page_comments
    })


"""
Добавление статьи только для авторизованых пользователей
"""


@login_required(login_url='/blog/sign-in')
def add_article(request):
    article_form = ArticleForm()

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)

        if article_form.is_valid():
            post = article_form.save(commit=False)
            post.author = request.user
            post.date = datetime.datetime.now()
            post.save()

            return redirect(home)

    return render(request, 'blogapp/add_article.html', {
        'article_form': article_form,
    })

