from django.db import models

# Create your models here.


class Messages(models.Model):
    name = models.CharField(max_length=255)
    email=models.EmailField()
    phone_no=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self) -> str:
        return self.name