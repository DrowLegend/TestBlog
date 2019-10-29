from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор статьи')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания статьи')
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    text = models.TextField(verbose_name='Текст статьи')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория статьи')
    short_description = models.CharField(max_length=200, default='', verbose_name='Краткое описание')
    img = models.ImageField(upload_to='img/title_article', blank=False, default='', verbose_name='Картинка статьи')
    moderation = models.BooleanField('Модерация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']


class Comment(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='Имя пользователя')
    post = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Комментируемый пост')
    content = models.CharField(max_length=200, verbose_name='Текст комментария')
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата комментария')
    moderation = models.BooleanField('Модерация', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']







