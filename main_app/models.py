from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Blogpost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=3000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'blogpost_id': self.id})

class Comment(models.Model):
    body = models.TextField(max_length=3000)
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.body