from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
      user = models.OneToOneField(User, on_delete = models.CASCADE)
      bio = models.TextField(blank=True)
      def __str__(self):
          return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    start_date = models.DateTimeField()
    time = models.DateTimeField()

    
    def __str__(self):
        return self.title

class DayModel(models.Model):
      user = models.ForeignKey(User, on_delete = models.CASCADE,default=1)
      title = models.CharField(max_length=100)
      note = models.TextField()
      date = models.DateField(null=True)
      is_public = models.BooleanField(default=False)

      def __str__(self):
        return f"{self.note[:20]} - {self.user.username}"

#MESSAGES FUNCTIONALITY
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete= models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages',on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Message From {self.sender} to {self.recipient} at {self.timestamp}'
         
