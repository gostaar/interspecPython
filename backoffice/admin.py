from django.contrib import admin

from backoffice.models import Genre, Editeur, Auteur, Livre, Stock, Usure, Exemplaire, Emprunt, Adherent

# Register your models here.

admin.site.register(Genre)
admin.site.register(Editeur)
admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Stock)
admin.site.register(Usure)
admin.site.register(Exemplaire)
admin.site.register(Emprunt)
admin.site.register(Adherent)
