# MyShop

MyShop est une application web Django pour gérer une boutique en ligne. Ce projet fournit une interface pour gérer les produits, les catégories, et les utilisateurs.

## Prérequis

- Python 3.8 ou supérieur
- Django 4.x
- SQLite (ou un autre SGBD selon configuration)


## Utilisation

- Accédez à l'interface d'administration Django pour gérer les produits et les catégories : `http://127.0.0.1:8000/admin/`.
- Utilisez les vues et les modèles fournis pour interagir avec les produits et les catégories via l'interface utilisateur.

## Structure du Projet

- **myshop/** : Le répertoire principal du projet.
  - **manage.py** : Le script de gestion de Django.
  - **myshop/** : Le répertoire du projet Django.
    - **settings.py** : Les paramètres du projet.
    - **urls.py** : Les URLs du projet.
    - **wsgi.py** : Le point d'entrée WSGI pour les déploiements.
  - **shop/** : L'application principale de la boutique.
    - **migrations/** : Les migrations de la base de données.
    - **models.py** : Les modèles de la boutique.
    - **views.py** : Les vues de la boutique.
    - **admin.py** : L'interface d'administration de la boutique.
    - **templates/** : Les modèles HTML.
    - **static/** : Les fichiers statiques (CSS, JS, images).

