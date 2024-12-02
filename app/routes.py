from flask import Blueprint, render_template, request
from .utils import load_articles, get_categories, get_categories_icons

# Création d'un Blueprint pour regrouper les routes liées à la fonctionnalité principale
# Un Blueprint permet de modulariser les applications Flask en regroupant les routes par logique ou fonctionnalité.
main = Blueprint('main', __name__)

# Chargement des articles au démarrage de l'application
# `load_articles` est une fonction qui charge les articles depuis une source de données.
# Cela nous permet de précharger les articles une seule fois, évitant de les recharger à chaque requête.
articles_by_theme = load_articles()

# Extraction des catégories à partir des articles chargés
# Cela crée une liste des thèmes disponibles (comme "Communication", "Innovation", etc.).
categories = get_categories(articles_by_theme)

# Chargement des icônes associées à chaque catégorie
# Les icônes sont utilisées pour afficher une représentation visuelle de chaque thème sur le tableau de bord.
theme_emojis = get_categories_icons()


@main.route("/")
def dashboard():
    """
    Vue principale pour afficher le tableau de bord des articles classés par thème.

    Cette fonction génère une page HTML contenant :
    - Les articles filtrés par catégorie (si une catégorie est sélectionnée).
    - Les catégories disponibles pour la navigation.
    - Les icônes associées aux catégories.

    """
    # Récupération de la catégorie sélectionnée à partir des paramètres de requête
    # Exemple : si l'utilisateur visite "/?category=innovation", alors "category" vaudra "innovation".
    category = request.args.get("category")
    
    # Si aucune catégorie n'est spécifiée, on sélectionne par défaut la première catégorie.
    # Cela évite d'avoir une page vide si aucun filtre n'est appliqué.
    if not category:
        category = categories[0]
    
    # Vérification si la catégorie spécifiée existe dans les articles préchargés.
    if category in articles_by_theme:
        # Si la catégorie est valide, on filtre les articles correspondants.
        filtered_articles = {category: articles_by_theme[category]}
    else:
        # Si la catégorie n'existe pas (par exemple, un paramètre incorrect), on renvoie une liste vide.
        filtered_articles = {}
    
    # Rendu du modèle "dashboard.html" avec les données nécessaires
    # - `articles_by_theme`: Les articles filtrés par catégorie
    # - `categories`: La liste des catégories pour le menu
    # - `theme_emojis`: Les icônes associées aux catégories
    return render_template(
        "index.html", 
        articles_by_theme=filtered_articles, 
        categories=categories, 
        theme_emojis=theme_emojis
    )
