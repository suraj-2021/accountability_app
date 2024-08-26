from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    date = models.DateTimeField()
    time = models.DateTimeField()

    
    def __str__(self):
        return self.title
    