from django.db import models

# Create your models here.
class Entry(models.Model):
    name=models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # id = models.PositiveIntegerField(primary_key=True)
    # id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name} {self.date}'
