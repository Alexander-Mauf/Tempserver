from django.db import models



class Standort(models.Model):
    name = models.CharField(max_length=255)
    land = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Standort: {}".format(self.name)

    def __repr__(self):
        return "Standort: {}".format(self.name)


class Messwert(models.Model):
    wert = models.FloatField(
        default=0.0
    )
    messeinheit = models.CharField(max_length=255)
    sensor_read_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    standort = models.ForeignKey(
        Standort,
        related_name='messwerte',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return "Messwert: {}".format(self.pk)

    def __repr__(self):
        return "Messwert: {}".format(self.pk)





class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()