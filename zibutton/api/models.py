from django.db import models

def default_five_sublists():
    return [[], [], [], [], []]

class List(models.Model):
    name = models.CharField(max_length=255, default='Untitled List')
    owner = models.ForeignKey('auth.User', related_name='lists', on_delete=models.CASCADE)
    language = models.CharField(max_length=50, default='zh-CN')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    characters = models.JSONField(default=list)

class Progress(models.Model):
    user = models.ForeignKey('auth.User', related_name='progress', on_delete=models.CASCADE)
    list = models.ForeignKey('List', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    progress = models.JSONField(default=default_five_sublists)