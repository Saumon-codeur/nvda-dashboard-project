import pandas as pd 
from datetime import datetime

# Charger les données
df = pd.read_csv("nvda_prices.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df[pd.notnull(df["price"])]  # Ignorer les lignes sans prix

# Filtrer pour aujourd'hui
aujourd_hui = datetime.now().date()
df_jour = df[df["timestamp"].dt.date == aujourd_hui]

if not df_jour.empty:
    prix_ouverture = df_jour.iloc[0]["price"]
    prix_cloture = df_jour.iloc[-1]["price"]
    variation = ((prix_cloture - prix_ouverture) / prix_ouverture) * 100
    volatilite = df_jour["price"].std()
    prix_max = df_jour["price"].max()
    prix_min = df_jour["price"].min()
    moyenne = df_jour["price"].mean()

    # Créer un rapport texte
    with open("rapport_du_jour.txt", "w") as f:
        f.write(f"Rapport du {aujourd_hui}\n")
        f.write(f"Prix d'ouverture : {prix_ouverture:.2f} EUR\n")
        f.write(f"Prix de clôture : {prix_cloture:.2f} EUR\n")
        f.write(f"Moyenne du jour : {moyenne:.2f} EUR\n")
        f.write(f"Variation : {variation:.2f} %\n")
        f.write(f"Volatilité (écart-type) : {volatilite:.4f}\n")
        f.write(f"Prix max : {prix_max:.2f} EUR\n")
        f.write(f"Prix min : {prix_min:.2f} EUR\n")
else:
    with open("rapport_du_jour.txt", "w") as f:
        f.write("Pas de données disponibles pour aujourd'hui.\n")

