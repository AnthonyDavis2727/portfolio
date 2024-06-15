from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    date_posted = models.DateField()
    last_modified = models.DateField()
    blog_content = models.TextField(max_length=500)
