from flask import Flask

def create_app():
    """
    Fonction pour créer et configurer une instance de l'application Flask.

    Cette fonction suit le modèle d'usine (factory pattern) utilisé dans Flask
    pour permettre une création flexible et modulaire de l'application.
    """
    # Création de l'application Flask
    # `template_folder="../templates"` indique le chemin des fichiers HTML
    # (templates) utilisés pour le rendu des pages.
    app = Flask(__name__, template_folder="../templates")

    # Importer et enregistrer les routes via un Blueprint
    # Les routes sont définies dans `routes.py` et organisées sous le Blueprint `main`.
    # Cela permet de modulariser le code et de séparer les responsabilités.
    from .routes import main
    app.register_blueprint(main)

    # Retourne l'instance configurée de l'application Flask
    return app
