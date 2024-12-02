# Liste des flux RSS
# Chaque URL correspond à un flux RSS qui sera analysé pour extraire des articles.
# Ces flux peuvent provenir de diverses sources liées à des thèmes spécifiques.
RSS_FEEDS = [
    "https://news.google.com/rss/search?q=j%27ai%20un%20pote%20dans%20la%20com&hl=fr&gl=FR&ceid=FR%3Afr", 
    "https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lemondeinformatique.fr%2Fbig-data-139.html&hl=fr&gl=FR&ceid=FR%3Afr",
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.futura-sciences.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.sciencesetavenir.fr%2Fhigh-tech%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fdatascientest.com%2Fblog-data-ia-actualites&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lemagit.fr%2Factualites%2FIntelligence-Artificielle-et-Data-Science&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.datasciencecentral.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Finsideainews.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fdataconomy.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.usinenouvelle.com%2Fmanagement%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fculture-rh.com%2Fcategory%2Fmanagement%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lesechos.fr%2Fidees-debats%2Fleadership-management%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lemonde.fr%2Fmanagement%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lefigaro.fr%2Fdecideurs%2Fmanagement&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fspringwise.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/search?q=https%3A%2F%2Fwww.engadget.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fcleantechnica.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.zdnet.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.pcmag.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fsingularityhub.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lemonde.fr%2Fsncf%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.groupe-sncf.com%2Ffr%2Fgroupe%2Fportrait-entreprise%2Fgroupe-societes%2Fsncf-sa%2Fsncf-immobilier&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.hp.com%2Ffr-fr%2Fpoly.html&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=j%27ai%20un%20pote%20dans%20la%20com&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Flareclame.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.influencia.net%2F&hl=fr&gl=FR&ceid=FR%3Afrv"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.strategies.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Filetaitunepub.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.vice.com%2Ffr%2Ftag%2Ftech%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.lesnumeriques.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.numerama.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fhitek.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.sncf-voyageurs.com%2Ffr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.sncf-voyageurs.com%2Ffr%2Fvoyagez-avec-nous%2Fhoraires-et-itineraires%2Finformations-trafic%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fressources.data.sncf.com%2Fpages%2Faccueil%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.laviedurail.com%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.actu-marketing.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fwww.e-marketing.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fcomarketing-news.fr%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=https%3A%2F%2Fsiecledigital.fr%2Fmarketing%2F&hl=fr&gl=FR&ceid=FR%3Afr"
    #"https://news.google.com/rss/search?q=blog%20du%20moderateur&hl=fr&gl=FR&ceid=FR%3Afr"
]

# Dictionnaire de mots-clés par thème
# Chaque clé est un thème, et les valeurs sont des listes de mots-clés.
# Ces mots-clés sont utilisés pour classer les articles selon leur contenu.
THEMES_KEYWORDS = {
    "Communication": [
        "communication", "réseaux sociaux", "media", "relations publiques", 
        "communiqué de presse", "interactions", "stratégie de communication", 
        "publicité", "journalisme", "presse", "influence", "notoriété"
    ],
    "Innovation": [
        "innovation", "technologie", "recherche et développement", "nouveau produit", 
        "brevet", "startups", "nouvelles tendances", "disruption", "progrès", 
        "technologique", "futur", "incubateur", "digitalisation"
    ],
    "Data": [
        "données", "data", "big data", "analyse de données", "visualisation de données", 
        "science des données", "exploitation des données", "tableau de bord", "statistiques", 
        "modélisation", "prévision", "data science", "décisionnel", "algorithme"
    ],
    "SNCF voyageurs": [
        "SNCF voyageurs", "TGV", "train", "TER", "mobilité", "service de transport", 
        "transport ferroviaire", "billets de train", "horaire SNCF", "voyage", 
        "passager", "réseau ferré", "itinéraire", "retard", "correspondance", "embarquement"
    ],
    "Ouigo": [
        "OUIGO", "low-cost", "train OUIGO", "billet OUIGO", "tarif réduit", 
        "voyages OUIGO", "TGV low-cost", "embarquement OUIGO", "trajets OUIGO"
    ],
    "Marketing": [
        "marketing", "stratégie marketing", "campagne", "publicité", "ciblage", 
        "promotion", "contenu marketing", "emailing", "marketing digital", 
        "inbound marketing", "SEO", "branding", "acquisition", "conversion", 
        "taux de clic", "marketing automation"
    ],
    "IA": [
        "intelligence artificielle", "IA", "machine learning", "réseaux neuronaux", 
        "apprentissage automatique", "algorithmes", "intelligence machine", 
        "reconnaissance d'image", "automatisation", "robotique", "chatbot", 
        "NLP", "vision par ordinateur", "IA générative"
    ],
    "Base de données": [
        "base de données", "SGBD", "gestion de données", "SQL", "NoSQL", 
        "MongoDB", "MySQL", "Oracle", "stockage de données", "data warehouse", 
        "BigQuery", "postgreSQL", "recherche de données", "système de gestion", 
        "indexation", "optimisation des requêtes"
    ],
    "Management": [
        "management", "gestion de projet", "gestion d'équipe", "leadership", 
        "planification", "stratégie de gestion", "organisation", "processus de travail", 
        "ressources humaines", "productivité", "efficacité", "coordination", 
        "performance", "coaching", "supervision", "productivité", "coordination", "gestion"
    ],
    "SNCF Groupe": [
        "SNCF Groupe", "SNCF", "mobilité durable", "transport public", "environnement", 
        "plan stratégique", "fret", "logistique", "service de transport", "innovation SNCF", 
        "investissements", "gouvernance", "actionnaires", "régulation", "partenariat", 
        "responsabilité sociétale"
    ],
    "SNCF immobilier": [
        "SNCF immobilier", "gestion immobilière", "bâtiment", "patrimoine", 
        "urbanisme", "développement immobilier", "projets immobiliers", "logement", 
        "rénovation", "aménagement urbain", "valorisation immobilière", 
        "immeuble", "bail", "environnement", "optimisation d'espace", "gare"
    ],
    "Audiovisuel": [
        "audiovisuel", "télévision", "radio", "cinéma", "production audiovisuelle", 
        "médias", "contenu vidéo", "documentaire", "émission", "streaming", 
        "diffusion", "plateformes", "publicité audiovisuelle", "broadcasting", 
        "production", "réalisation"
    ]
}

# Dictionnaire des icônes par thème
# Chaque thème a une icône qui peut être utilisée dans l'interface utilisateur.
CATEGORIES_ICONS = {
    "Communication": '<i class="fa-solid fa-tty"></i>',
    "Innovation": '<i class="fa-regular fa-lightbulb"></i>',
    "Data": '<i class="fas fa-chart-bar"></i>',
    "IA": '<i class="fas fa-robot"></i>',
    "Management": '<i class="fas fa-tasks"></i>',
    "Marketing": '<i class="fas fa-chart-line"></i>',
    "Audiovisuel": '<i class="fas fa-video"></i>',
    "SNCF voyageurs": '<i class="fas fa-train"></i>',
    "Ouigo": '<i class="fas fa-ticket-alt"></i>',
    "SNCF Groupe": '<i class="fas fa-building"></i>',
    "SNCF immobilier": '<i class="fas fa-home"></i>',
}

DEBUG_MODE = True
