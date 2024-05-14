from django.db import models

class House(models.Model):
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.TextField()
    image = models.ImageField(upload_to='house_images/', blank=True, null=True)
    price=models.IntegerField()
   
    def __str__(self):
        return self.address

