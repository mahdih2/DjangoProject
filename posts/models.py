from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(blank=True)
    is_enable = models.BooleanField(default=False)
    publish = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    text = models.TextField()
    publish = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)