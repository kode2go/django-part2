from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    # id = pk
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return '%s %s' % (self.title, self.body)


class Article(models.Model):
    # id = pk
    title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=True)

    # get_abs is part of create and update view
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})

