from django.db import models

class userdata(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name