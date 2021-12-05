from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager

CATEGORIES = (
    ('html', 'Html'),
    ('css', 'Css'),
    ('javascript', 'Javascript'),
    ('python', 'Python')
)

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name


    def get_absolute_url(self):
        return reverse('blog-home')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000000)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(default='Body')
    id = models.IntegerField(primary_key=True)
    #tags = TaggableManager()
    image = models.ImageField(blank=True, null=True, upload_to='image/')
    #category = models.CharField(max_length=128, choices = CATEGORIES, default='Python')
    category = models.CharField(max_length=255, default='Uncategorized')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article-page', args=[self.id])
