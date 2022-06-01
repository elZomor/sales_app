from django.db import models


class Engineer(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Engineer'
        verbose_name_plural = 'Engineers'
