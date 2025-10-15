from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length = 100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"