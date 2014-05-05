from django.db import models

# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created at")
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")

    def __unicode__(self):
        return self.title
