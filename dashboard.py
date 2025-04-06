import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import datetime

# Charger les données depuis le fichier CSV
def load_data():
    try:
        df = pd.read_csv("nvda_prices.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except Exception as e:
        print("Erreur de lecture:", e)
        return pd.DataFrame(columns=["timestamp", "price"])

# Lire le rapport quotidien
def lire_rapport():
    try:
        with open("rapport_du_jour.txt", "r") as f:
            return f.read()
    except:
        return "Rapport non encore généré."

# Initialiser l'application Dash
app = Dash(__name__)
app.title = "NVDA Live Dashboard"

app.layout = html.Div([
    html.H1("Dashboard - Action NVIDIA (NVDA)"),
    
    html.Div(id='last-update', style={"marginBottom": "10px"}),
    html.Div(id='current-price', style={"fontSize": "24px", "fontWeight": "bold", "marginBottom": "20px"}),

    dcc.Graph(id='price-graph'),

    html.H2("Rapport quotidien"),
    html.Pre(id='daily-report', style={
        "whiteSpace": "pre-wrap",
        "backgroundColor": "#f7f7f7",
        "padding": "1em",
        "border": "1px solid #ccc"
    }),

    dcc.Interval(id='interval', interval=5*60*1000, n_intervals=0)  # mise à jour toutes les 5 minutes
])

@app.callback(
    [Output('current-price', 'children'),
     Output('price-graph', 'figure'),
     Output('last-update', 'children'),
     Output('daily-report', 'children')],
    [Input('interval', 'n_intervals')]
)
def update_dashboard(n):
    df = load_data()
    if df.empty:
        return "Aucune donnée disponible", {}, "", ""

    # Prix actuel
    current_price = df.iloc[-1]["price"]
    current_time = df.iloc[-1]["timestamp"]

    # Graphique
    fig = px.line(df, x="timestamp", y="price", title="Évolution du cours NVDA", markers=True)

    # Rapport
    rapport = lire_rapport()

    return (
        f"Prix actuel : {current_price:.2f} EUR",
        fig,
        f"Dernière mise à jour : {current_time}",
        rapport
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)

