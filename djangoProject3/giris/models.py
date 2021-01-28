from django.db import models

class Satıs(models.Model):
    id=models.AutoField(primary_key=True)
    marka=models.CharField(max_length=60)
    model=models.CharField(max_length=50)
    fiyat = models.IntegerField(max_length=50)
    tel=models.CharField(max_length=20)
    adres=models.TextField(blank=True)

    def __str__(self):
        return self.marka