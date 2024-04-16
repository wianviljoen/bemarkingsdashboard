from django.db import models

# Create your models here.
class KPA(models.Model):
    jaar = models.CharField(max_length=4)
    naam = models.CharField(max_length=264)
    target = models.IntegerField()

    def __str__(self):
        return self.naam
class DataMaand(models.Model):
    MAANDE = (
        ('Januarie', 'Januarie'),
        ('Februarie', 'Februarie'),
        ('Maart', 'Maart'),
        ('April', 'April'),
        ('Mei', 'Mei'),
        ('Junie', 'Junie'),
        ('Julie', 'Julie'),
        ('Augustus', 'Augustus'),
        ('September', 'September'),
        ('Oktober', 'Oktober'),
        ('November', 'November'),
        ('Desember', 'Desember'),


    )
    jaar = models.ForeignKey(KPA, on_delete=models.CASCADE)
    maand = models.CharField(max_length=20, choices=MAANDE, null=True)

    def __str__(self):
        return self.maand

class Data(models.Model):
    maand = models.ForeignKey(DataMaand, on_delete=models.CASCADE)
    kpa = models.ForeignKey(
        KPA,
        on_delete=models.CASCADE,  # Or another on_delete behavior that suits your requirement
        null=True,
        blank=True,
        verbose_name='KPA'
    )

    begin = models.IntegerField(default=0)
    data = models.IntegerField()

    def __str__(self):
        return f"{self.maand.maand} - {self.kpa.naam} - {self.data}"




