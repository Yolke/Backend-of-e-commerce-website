from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Produit, Categorie, Panier, PanierProduit, Commande
from .forms import FormulaireProduit, FormulaireCategorie, FormulaireCommande
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'shop/liste_produits.html', {'produits': produits})

def ajouter_produit(request):
    if request.method == 'POST':
        formulaire = FormulaireProduit(request.POST, request.FILES)
        if formulaire.is_valid():
            formulaire.save()
            return redirect('liste_produits')
    else:
        formulaire = FormulaireProduit()
    return render(request, 'shop/ajouter_produit.html', {'formulaire': formulaire})

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == 'POST':
        formulaire = FormulaireProduit(request.POST, request.FILES, instance=produit)
        if formulaire.is_valid():
            formulaire.save()
            return redirect('liste_produits')
    else:
        formulaire = FormulaireProduit(instance=produit)
    return render(request, 'shop/modifier_produit.html', {'formulaire': formulaire, 'produit': produit})

@login_required
def afficher_panier(request):
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    panier_produits = PanierProduit.objects.filter(panier=panier)
    return render(request, 'shop/panier.html', {'panier_produits': panier_produits})

@login_required
def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    panier_produit, created = PanierProduit.objects.get_or_create(
        panier=panier, produit=produit
    )
    panier_produit.quantite += 1
    panier_produit.save()
    return redirect('afficher_panier')

@login_required
def supprimer_du_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier = Panier.objects.get(utilisateur=request.user)
    panier_produit = get_object_or_404(PanierProduit, panier=panier, produit=produit)
    panier_produit.delete()
    return redirect('afficher_panier')

@login_required
def passer_commande(request):
    panier = Panier.objects.get(utilisateur=request.user)
    if request.method == 'POST':
        formulaire = FormulaireCommande(request.POST)
        if formulaire.is_valid():
            commande = formulaire.save(commit=False)
            commande.utilisateur = request.user
            commande.save()
            for item in PanierProduit.objects.filter(panier=panier):
                commande.produits.add(item.produit, through_defaults={'quantite': item.quantite})
            panier.delete()  # Vider le panier après la commande
            return redirect('confirmation_commande')
    else:
        formulaire = FormulaireCommande()
    return render(request, 'shop/passer_commande.html', {'formulaire': formulaire})

def confirmation_commande(request):
    return render(request, 'shop/confirmation_commande.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil ou une autre page après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
