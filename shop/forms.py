from django import forms
from .models import Produit, Categorie,Commande

class FormulaireProduit(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'image', 'stock', 'categorie']

class FormulaireCategorie(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'description']

class FormulaireCommande(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['adresse', 'statut']