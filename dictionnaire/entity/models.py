from django.db import models
# Create your models here.


class NaturesCourrier(models.Model):
    natureName = models.CharField(max_length=255, blank=False, default="")
    natureCode = models.CharField(max_length=50, blank=False, default="")
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.natureName

class TypesCourrier(models.Model):
    typeName = models.CharField(max_length=255, blank=False)
    typeCode = models.CharField(max_length=50, blank=False)
    isActive = models.BooleanField( default=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.typeName

class TypesOrganisme(models.Model):
    typeName = models.CharField(max_length=255, blank=False)
    typeCode = models.CharField(max_length=50, blank=False)
    isActive = models.BooleanField( default=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.typeName


class Organisme(models.Model):
    nom = models.CharField(max_length=255, blank=False)
    code = models.CharField(max_length=50, blank=False)
    isActive = models.BooleanField( default=True)
    isDelete = models.BooleanField(default=False)
    typeOrganisme = models.ForeignKey(
        'TypesOrganisme',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.nom

class Pays(models.Model):
    code = models.IntegerField(blank=True, default=0)
    alpha2 =models.CharField(max_length=2, blank=False)
    alpha3 = models.CharField(max_length=3, blank=False)
    nom_en_gb = models.CharField(max_length=100, blank=False)
    nom_fr_fr = models.CharField(max_length=150, blank=False)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        nom = self.nom_fr_fr
        return nom


class Workflow(models.Model):
    intitule = models.CharField(max_length=255, blank=False)
    step = models.IntegerField(auto_created=True)
    isActive = models.BooleanField( default=True)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.intitule