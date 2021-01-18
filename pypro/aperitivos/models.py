from django.db import models
from django.urls import reverse
from django.utils import timezone


class Video(models.Model):
    slug = models.CharField(max_length=32)
    titulo = models.CharField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    creation = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))
