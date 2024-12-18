import requests
import feedparser
from newspaper import Article
from dateutil import parser
from datetime import datetime
from babel.dates import format_date
from .decode_url import decode_google_news_url
from .config import RSS_FEEDS, THEMES_KEYWORDS, CATEGORIES_ICONS, DEBUG_MODE, USE_TRUELINK

# Utilisez les constantes importées
rss_feeds = RSS_FEEDS
themes_keywords = THEMES_KEYWORDS
categories_icons = CATEGORIES_ICONS

# Téléchargement d'un flux RSS
def fetch_rss(url):
    """
    Télécharge le contenu d'un flux RSS à partir d'une URL donnée.

    :param url: L'URL du flux RSS.
    :return: Contenu brut du flux RSS ou None en cas d'erreur.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement du flux {url}: {e}")
        return None

# Retourne le dictionnaire des icônes par catégorie
def get_categories_icons():
    return categories_icons

# Retourne la liste des catégories disponibles
def get_categories(articles_by_theme):
    return list(articles_by_theme.keys())

# Fonction pour classifier un article par thème
def classify_article(article, themes_keywords):
    """
    Classe un article dans un ou plusieurs thèmes en fonction des mots-clés.

    :param article: Dictionnaire contenant les détails d'un article.
    :param themes_keywords: Dictionnaire des mots-clés par thème.
    :return: Liste des thèmes associés à l'article.
    """
    title = article['Titre'].lower()
    return [
        theme for theme, keywords in themes_keywords.items()
        if any(keyword in title for keyword in keywords)
    ]

# Fonction pour décoder l'URL réelle d'un article Google News
def fetch_real_url(url):
    """
    Décode l'URL réelle d'un article Google News.

    :param url: L'URL Google News.
    :return: L'URL décodée ou l'URL de base si la décodée n'est pas disponible.
    """
    try:
        real_url = decode_google_news_url(url, interval=2)

        if DEBUG_MODE:
            print("=-=-=-=-" * 5)
            print("[🔗] URL d'origine:", url)
            print(f"[🌐] URL réelle: {real_url["decoded_url"]}")

        if real_url["status"] == False:
            return url
        
        return real_url["decoded_url"]
    except requests.RequestException as e:
        print(f"Erreur lors du décodage de l'URL {url}: {e}")
        return url

# Fonction pour obtenir le résumé d'un article
def get_article_summary_and_image(url):
    """
    Télécharge et analyse un article pour en extraire le résumé et l'image principale.

    :param url: URL de l'article.
    :return: Tuple contenant le résumé et l'URL de l'image principale.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        summary = article.summary if article.summary else "Résumé non disponible"
        image = article.top_image if article.top_image else None

        if DEBUG_MODE:
            print("=-=-=-=-" * 10)
            print(f"[📝] Résumé trouvé: {'✅' if summary != 'Résumé non disponible' else '❌'}")
            print(f"[🖼️] Image trouvée: {'✅' if image else '❌'}")

        return summary, image
    except Exception as e:
        print(f"Erreur lors de l'extraction de l'article pour {url}: {e}")
        return "Résumé non disponible", None

def parse_date(date_str):
    """ 
    Convertit une chaîne de caractères en objet date.
    
    :param date_str: La chaîne de caractères représentant la date.
    :return: Un objet date ou None si la conversion échoue.

    exemple : Wed, 05 Jun 2024 07:00:00 GMT -> 2024/06/05 -- Format Anglais
    """
    if not date_str:
        return None
    try:
        parsed_date = parser.parse(date_str)
        return parsed_date.date()
    except (ValueError, TypeError):
        return None

def format_date_french(date_obj):
    """
    Formate une date en français.
    
    :param date_obj: L'objet date à formater.
    :return: La date formatée en français.

    Exemple : 2024/06/05 -> 05 juin 2024 -- Format Francais
    """
    if not date_obj:
        return None
    return format_date(date_obj, format='long', locale='fr_FR')

# Analyse et classification des articles
def load_articles():
    """
    Télécharge, analyse et classe les articles à partir des flux RSS.

    :param rss_feeds: Liste des flux RSS.
    :param themes_keywords: Dictionnaire des mots-clés par thème.
    :return: Dictionnaire des articles classés par thème.
    """
    articles_by_theme = {theme: [] for theme in themes_keywords.keys()}

    for rss_url in rss_feeds:
        rss_content = fetch_rss(rss_url)
        if rss_content:
            flux = feedparser.parse(rss_content)
            for entry in flux.entries[:3]:
                # Extraire l'URL réelle
                if USE_TRUELINK:
                    real_url = fetch_real_url(entry.link)
                else:
                    real_url = entry.link

                # Obtenir le résumé et l'image principale
                summary, image = get_article_summary_and_image(real_url)

                # Formater la date en français
                date = entry.get("published", None)
                parsed_date = parse_date(date) # = Format Anglais
                formatted_date = format_date_french(parsed_date) # = Format Francais

                # Créer un article
                article = {
                    "Titre": entry.title,
                    "Lien": real_url,
                    "Résumé": summary,
                    "Image": image,
                    "Date": parsed_date, # = Format Anglais
                    "Date_fr": formatted_date, # = Format Francais
                }

                # Classer l'article selon les mots-clés
                themes = classify_article(article, themes_keywords)
                for theme in themes:
                    articles_by_theme[theme].append(article)

    # Trier les articles par date (les plus récents en premier)
    for theme in articles_by_theme:
        articles_by_theme[theme].sort(key=lambda x: x["Date"] or datetime.min.date(), reverse=True)

    return articles_by_theme
