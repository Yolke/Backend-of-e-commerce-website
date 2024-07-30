from django.contrib import admin
from .models import Categorie, Produit, Panier, PanierProduit, Commande, CommandeProduit

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'stock', 'categorie')

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('utilisateur',)

@admin.register(PanierProduit)
class PanierProduitAdmin(admin.ModelAdmin):
    list_display = ('panier', 'produit', 'quantite')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'adresse', 'statut')

@admin.register(CommandeProduit)
class CommandeProduitAdmin(admin.ModelAdmin):
    list_display = ('commande', 'produit', 'quantite')
