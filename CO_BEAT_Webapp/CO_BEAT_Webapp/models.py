from django.db import models

class Alerts(models.Model):
    time_date = models.DateTimeField()
    venue = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.venue