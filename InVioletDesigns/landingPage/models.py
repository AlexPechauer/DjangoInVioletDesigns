from django.db import models


class photoGallery(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    image = models.ImageField(default='default.jpg', upload_to='photoGallery')

    def __str__(self):
        return self.name

    def __save__(self):
        super().save()
