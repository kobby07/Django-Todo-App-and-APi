from django.db import models

# Create your models here.

class mytodo(models.Model):
    task = models.CharField( max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task