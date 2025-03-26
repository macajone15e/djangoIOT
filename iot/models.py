from django.db import models

class Devices(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastSeenAt = models.DateTimeField(auto_now=True)

class Temperatures(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE, related_name='temperatures')
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ({self.uid})"