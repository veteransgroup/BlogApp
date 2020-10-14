from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    url = models.URLField('Web address', blank=True)
    text = models.TextField('Content')
    created_time = models.DateTimeField('created_at', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='Article', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
