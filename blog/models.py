from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length = 200)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/')