from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    summary = models.CharField(max_length=100, default = "This is a summary")
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title