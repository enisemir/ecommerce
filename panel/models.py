from django.db import models


class Index_slider(models.Model):
    slogan = models.CharField(max_length=200)
    icerik = models.TextField()
    image_url = models.ImageField(upload_to='media/',
                                  default='media/fuel.png')
