# NVDA Dashboard Project

Ce projet réalise un scraping du cours de l’action NVIDIA (NVDA) depuis le site Boursorama, toutes les 5 minutes, à l’aide d’un script Bash. Les données sont stockées dans un fichier CSV et visualisées en temps réel à travers un tableau de bord interactif développé avec Dash (Python).

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
