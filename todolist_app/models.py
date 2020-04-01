from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
	manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None) #to apply these changes, make sure all earlier created task should be deleted, else this will give error
	task = models.CharField(max_length=300)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.task +"-"+str(self.done)