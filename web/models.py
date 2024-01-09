import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class NewsTag(models.Model):
    title = models.CharField(max_length=32, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    text = models.TextField(verbose_name='Текст новости')
    tags = models.ManyToManyField(NewsTag, verbose_name='Теги', blank=True)

    def __str__(self):
        return f'{self.user.name}: {self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
