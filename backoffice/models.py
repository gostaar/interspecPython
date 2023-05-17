import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Genre(models.Model):
    nom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom


class Editeur(models.Model):
    nom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom


class Auteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom + " " + self.prenom


class Livre(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField(max_length=2048, default="")
    isbn = models.CharField(max_length=250, default="")
    archive = models.BooleanField(default=False)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Stock(models.Model):
    emplacement = models.CharField(max_length=250)

    def __str__(self):
        return self.emplacement


class Usure(models.Model):
    nom = models.CharField(max_length=250)

    def __str__(self):
        return self.nom


class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    usure = models.ForeignKey(Usure, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def __str__(self):
        return self.livre.titre


class Adherent(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, default="")
    caution = models.BooleanField(default=False)

    def __str__(self):
        return self.nom + " " + self.prenom


class Emprunt(models.Model):
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE)
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    date_emprunt = models.DateField("date emprunt")
    date_retour = models.DateField("date retour")
    status = models.CharField(max_length=250)

    def __str__(self):
        return self.exemplaire.livre.titre

    def emprunte_recemment(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_emprunt <= now

    def en_retard(self):
        now = timezone.now()
        return self.date_retour <= now