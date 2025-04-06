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
server = app.server  
app.title = "NVDA Live Dashboard"


app.layout = html.Div(style={"fontFamily": "Arial, sans-serif", "padding": "20px"}, children=[

    #  header
    html.Div("📈 NVDA Live Dashboard", style={
        "backgroundColor": "#0d47a1",
        "color": "white",
        "padding": "1em",
        "textAlign": "center",
        "fontSize": "30px",
        "borderRadius": "8px",
        "marginBottom": "20px"
    }),

    # last update
    html.Div(id='last-update', style={
        "marginBottom": "10px",
        "color": "#555",
        "fontSize": "16px"
    }),

    #current price
    html.Div(id='current-price', style={
        "fontSize": "28px",
        "fontWeight": "bold",
        "color": "#2e7d32",
        "marginBottom": "20px"
    }),

    # graphs
    dcc.Graph(id='price-graph'),

    # daily report
    html.H2("📘 Rapport quotidien", style={
        "marginTop": "40px",
        "color": "#1565c0"
    }),
    html.Pre(id='daily-report', style={
        "whiteSpace": "pre-wrap",
        "backgroundColor": "#f7f7f7",
        "padding": "1em",
        "border": "1px solid #ccc",
        "borderRadius": "8px"
    }),

    # automatic refresh
    dcc.Interval(id='interval', interval=5*60*1000, n_intervals=0),

    # footer
    html.Footer(" scraping project - coworkers : Sami MEKKI - Leslie NJOUKOUE", style={
        "textAlign": "center",
        "marginTop": "50px",
        "paddingTop": "20px",
        "borderTop": "1px solid #ccc",
        "color": "#888",
        "fontSize": "14px"
    })
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

    current_price = df.iloc[-1]["price"]
    current_time = df.iloc[-1]["timestamp"]

    # Graphs
    fig = px.line(df, x="timestamp", y="price", title="Évolution du cours NVDA")

    # Report
    rapport = lire_rapport()

    return (
        f"💶 current price : {current_price:.2f} EUR",
        fig,
        f"🕒 last update : {current_time}",
        rapport
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)

