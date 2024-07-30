from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
]
urlpatterns += [
    path('panier/', views.afficher_panier, name='afficher_panier'),
    path('ajouter_au_panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer_du_panier/<int:produit_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('passer_commande/', views.passer_commande, name='passer_commande'),
]
