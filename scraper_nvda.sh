#!/bin/bash

URL="https://www.boursorama.com/cours/NVDA/"

# Télécharger le HTML
html=$(curl -s "$URL")

# Extraire le prix via une balise span spécifique
price=$(echo "$html" | grep -oP '<span class="c-instrument c-instrument--last"[^>]*>\K[0-9]+\,[0-9]+' | head -1)

# Remplacer la virgule par un point pour les décimales
price=$(echo "$price" | sed 's/,/./')

# Timestamp actuel
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# Fichier CSV avec chemin absolu
FILE="/home/vboxuser/nvda-dashboard-project/nvda_prices.csv"
if [ ! -f "$FILE" ]; then
    echo "timestamp,price" > "$FILE"
fi

# Enregistrer dans le fichier
echo "$timestamp,$price" >> "$FILE"

# Affichage console
echo "[$timestamp] Prix actuel de NVDA : $price EUR"

