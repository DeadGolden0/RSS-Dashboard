from app import create_app

# Appelle la fonction `create_app` pour initialiser et configurer l'application Flask
app = create_app()

# Point d'entrée principal de l'application
if __name__ == "__main__":
    """
    Cette section est exécutée uniquement si ce fichier est lancé directement
    (par exemple, avec `python app.py`).

    - `app.run(debug=True)` démarre le serveur Flask en mode développement :
        - Le mode debug permet de voir les erreurs en détail dans le navigateur.
        - Cela active également le rechargement automatique (auto-reload), 
          ce qui signifie que toute modification du code redémarrera le serveur.
    """
    app.run(debug=False)
