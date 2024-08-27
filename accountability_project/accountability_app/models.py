from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    start_date = models.DateTimeField()
    time = models.DateTimeField()

    
    def __str__(self):
        return self.title

class DayModel(models.Model):
      title = models.CharField(max_length=100)
      note = models.TextField()
      date = models.DateField(null=True)
      def __str__(self):
        return self.title
             
