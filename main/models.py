from django.db import models

class PreviewImage(models.Model):
    objects = None
    image = models.ImageField(upload_to='preview_images/')
    description = models.TextField()

    def __str__(self):
        return self.description

class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.phone_number} ({self.email})'
