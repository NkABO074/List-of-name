from django.db import models

# Create your models here.
class Dudes(models.Model):
    name = models.CharField(max_length= 100)
    surmname = models.CharField(max_length= 100)
    age = models.IntegerField()
    telephone = models.IntegerField()
    city = models.CharField(max_length= 100)
    postal_address = models.IntegerField()
    pub_date = models.DateTimeField("date published", auto_now=True)

    def __str__(self):
        return self.name