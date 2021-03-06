# Generated by Django 2.2.5 on 2019-10-17 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20191017_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания статьи'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Article', verbose_name='Комментируемый пост'),
        ),
    ]
