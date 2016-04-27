# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

def validator_even_length(s):
    if len(s) % 2 != 0:
        raise ValidationError('짝수길이로 입력하세요.')


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=200, validators=[validator_even_length])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])
#        return reverse('blog:post_detail', kargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    #many to many
    name = models.CharField(max_length=100)