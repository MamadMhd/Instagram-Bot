from django.db import models

class BotConfig(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    target_hashtags = models.TextField()  # JSON array or comma-separated
    is_active = models.BooleanField(default=False)

class BotLog(models.Model):
    bot = models.ForeignKey(BotConfig, on_delete=models.CASCADE, related_name="logs")
    action = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
