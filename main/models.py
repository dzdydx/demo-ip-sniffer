from django.db import models

# Create your models here.

class IPAddr(models.Model):
  ip = models.CharField(max_length=50)
  visitCount = models.IntegerField(default=1)
  visitTime = models.DateTimeField(auto_now=False,auto_now_add=True)

  def __str__(self):
    return self.ip