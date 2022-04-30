from os import name
from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django import forms






# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=75)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(verbose_name="date Blog", default=timezone.now)
    body = models.TextField(max_length=800)
    idblog = models.CharField(max_length=20)
    typeblog = models.CharField(max_length=20, choices=(("tech", "tech"), ("sport", "sport"), ("politique", "politique"), ("culture", "culture"), ("autre", "autre")))
    class Meta:
        verbose_name = "Blog"
        ordering = ['date']
    def __str__(self) -> str:
        return self.body

class ForumBlog(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateTimeField(verbose_name="date Sender", default=timezone.now)
    body = models.TextField(max_length=250)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.body

def getBlogForm(user):
    class BlogForm(forms.Form):
        name = forms.CharField(max_length=75, required=True)
        author = forms.CharField(max_length=50, required=True, disabled=True, initial=user)
        body = forms.CharField(max_length=800, required=True, label="body", widget=forms.Textarea)
    return BlogForm

def getForumBlogForm(user):
    class ForumBlogForm(forms.Form):
        author = forms.CharField(max_length=50, required=True, disabled=True, initial=user)
        body = forms.CharField(max_length=250, required=True)
        blog = forms.CharField(max_length=50, required=True, label="le nom du blog ")
    return ForumBlogForm


