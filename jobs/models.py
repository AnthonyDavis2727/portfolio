from django.db import models

class Job(models.Model):
    thumbnail = models.ImageField(upload_to='images/')
    job_name = models.CharField(default='Placeholder',max_length=75)
    github_link = models.CharField(default='Placeholder', max_length=256)
    summary = models.CharField(max_length=256)

    def __str__(self):
        return self.job_name