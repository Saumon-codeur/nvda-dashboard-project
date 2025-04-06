# NVDA Dashboard Project

Ce projet réalise un scraping du cours de l’action NVIDIA (NVDA) depuis le site Boursorama, toutes les 5 minutes, à l’aide d’un script Bash. Les données sont stockées dans un fichier CSV et visualisées en temps réel à travers un tableau de bord interactif développé avec Dash (Python).Le projet repose sur les horaires du marché NASDAQ (15h30–22h). En dehors de ces horaires, le cours reste figé car aucun échange n’a lieu.

## Fonctionnalités

- Scraping automatisé toutes les 5 minutes via `cron`
- Stockage des données dans un fichier `nvda_prices.csv`
- Dashboard interactif affichant :
  - Le prix actuel
  - Un graphique d’évolution des prix
  - Un rapport quotidien contenant des statistiques
- Rapport généré automatiquement chaque jour à 20h, comprenant :
  - Prix d’ouverture
  - Prix de clôture
  - Moyenne du jour
  - Variation en pourcentage
  - Volatilité (écart-type)
  - Prix minimum et maximum

## Technologies utilisées

- Bash (pour le scraping)
- Python 3
  - Dash
  - Pandas
  - Plotly
- cron (pour l’automatisation)
- tmux (pour le déploiement en continu sur la VM)

## Installation et exécution

1. Créer un environnement virtuel :
   ```bash
   python3 -m venv dash_env
   source dash_env/bin/activate

### 2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

### 3. Lancer le dashboard :

```bash
python3 dashboard.py
```

Accessible à l’adresse : [http://192.168.1.25:8050](http://192.168.1.25:8050)

---

##  Structure du projet

```
nvda-dashboard-project/
├── scraper_nvda.sh            # Scraper Bash
├── nvda_prices.csv            # Données historisées
├── dashboard.py               # Dashboard Dash
├── rapport.py                 # Générateur de rapport quotidien
├── rapport_du_jour.txt        # Rapport du jour
├── requirements.txt           # Dépendances Python
└── README.md                  # Description du projet
```
