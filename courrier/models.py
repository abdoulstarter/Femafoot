import datetime

from django.db import models

# Create your models here.
from archivage.settings import MEDIA_ROOT
from dictionnaire.entity.models import Pays


class Courrier(models.Model):
    titre = models.CharField(max_length=255, blank=False)
    description = models.TextField( blank=True)



    class Urgence(models.TextChoices):
        URGENT = 'UR',
        NORMAL = 'NM',
        PAS_URGENT = 'PS',
        PEU_URGENT = 'PU',

    urgence = models.CharField(
        max_length=2,
        choices=Urgence.choices,
        default=Urgence.NORMAL,
    )

    organisme = models.ForeignKey(
        'dictionnaire.Organisme',
        on_delete=models.CASCADE,
    )
    type_courrier = models.ForeignKey(
        'dictionnaire.TypesCourrier',
        on_delete=models.CASCADE,
    )
    nature_courrier = models.ForeignKey(
        'dictionnaire.NaturesCourrier',
        on_delete=models.CASCADE,
    )

    assigner_a = models.ForeignKey(
        'auth.User',
        on_delete= models.CASCADE,
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='templates/static/documents')

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ("titre",
                    "organisme",
                    "type_courrier",
                    "nature_courrier",
                    "assigner_a",
                    "date_creation"
                    )