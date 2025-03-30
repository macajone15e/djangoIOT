from django.db import models

class Devices(models.Model):
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField
    createdAt = models.DateTimeField(auto_now_add=True)
    lastSeenAt = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField()
    room = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    attach = models.PositiveIntegerField(default=0)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, related_name='devices')
    otaPassword = models.CharField(max_length=100)
    sensorDelay = models.PositiveIntegerField(default=0)
    rssi = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.name}, {self.uid}"
    class Meta : 
        verbose_name = "Device"
        verbose_name_plural = "Devices"

class Temperatures(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE, related_name='temperatures')
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.device} : {self.value}°C at {self.timestamp}"
    class Meta :
        verbose_name = "Temperature"
        verbose_name_plural = "Temperatures"