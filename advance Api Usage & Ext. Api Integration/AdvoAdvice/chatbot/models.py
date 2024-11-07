from django.db import models
from userAuth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat")
    question = models.TextField()
    response = models.TextField(default=False)
