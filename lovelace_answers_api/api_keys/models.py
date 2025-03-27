from django.db import models


class APIKey(models.Model):

    LEVEL_CHOICES = [
        ('read', 'Only Read'),
        ('write', 'Read + Write'),
        ('admin', 'All access')
        ]

    key = models.CharField(max_length=64, unique=True, blank=True)
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.level.upper()} API Key ({self.key[:8]}...)"
