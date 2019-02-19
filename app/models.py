from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse



class Post(models.Model):
    POST_CATEGORY = (
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Entertainment', 'Entertainment'),

        ('Lifestyle', 'Lifestyle'),
        ('Fashion', 'Fashion'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(choices=POST_CATEGORY,max_length=80,default='Science',blank=False)
    content = models.TextField(max_length=2000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics/',default='monitor.jpg')
    is_mvp = models.BooleanField(default=False)
    is_editors_pick = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
