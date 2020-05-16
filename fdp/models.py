from django.db import models


# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=1024)
    sender = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "(%s): %s" % (self.sender, self.text)

class YT(models.Model):
	just_id = models.CharField(max_length = 20)

	def __str__(self):
		return "ytlink here"
