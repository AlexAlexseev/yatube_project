from django.db import models
# Из модуля auth импортируем функцию get_user_model 
from django.contrib.auth import get_user_model

# Group = get_user_model()
User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        # Не обязательно указывать сообщество 'Group'
        blank=True,
        null=True,
        related_name='group'
    )


class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
