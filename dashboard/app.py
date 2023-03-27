import os
import argparse
import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go
import sqlite3


# Create the Dash app
app = dash.Dash(__name__)

# Define command-line arguments
parser = argparse.ArgumentParser(description='Run the Dash app with a database URL')
parser.add_argument('--database-url', type=str, default='data/github_metrics.db',
                    help='The URL of the SQLite database')

# Parse command-line arguments
args = parser.parse_args()

# Connect to the SQLite database and retrieve the data
conn = sqlite3.connect(args.database_url)
df = pd.read_sql_query("SELECT * FROM metrics WHERE date >= DATE('now', '-30 days')", conn)
conn.close()

# Convert the 'date' column to a pandas datetime object
df['date'] = pd.to_datetime(df['date'])

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='GitHub Metrics Dashboard'),
    dcc.Graph(
        id='stars',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['stars'],
                    mode='lines+markers',
                    name='Number of stars'
                )
            ],
            'layout': {
                'title': 'Number of Stars'
            }
        }
    ),
    dcc.Graph(
        id='forks',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['forks'],
                    mode='lines+markers',
                    name='Number of forks'
                )
            ],
            'layout': {
                'title': 'Number of Forks'
            }
        }
    ),
    dcc.Graph(
        id='forks-to-stars',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['forks_to_stars_ratio'],
                    mode='lines+markers',
                    name='Forks to stars ratio'
                )
            ],
            'layout': {
                'title': 'Forks to Stars Ratio'
            }
        }
    ),
    dcc.Graph(
        id='subscribers',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['subscribers'],
                    mode='lines+markers',
                    name='Number of subscribers'
                )
            ],
            'layout': {
                'title': 'Number of Subscribers'
            }
        }
    ),
    dcc.Graph(
        id='contributors',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['contributors'],
                    mode='lines+markers',
                    name='Number of contributors'
                )
            ],
            'layout': {
                'title': 'Number of Contributors'
            }
        }
    ),
    dcc.Graph(
        id='issues-opened',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['issues_opened'],
                    mode='lines+markers',
                    name='Number of issues opened in the last month'
                )
            ],
            'layout': {
                'title': 'Number of Issues Opened in the Last Month'
            }
        }
    ),
    dcc.Graph(
        id='issues-closed',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['issues_closed'],
                    mode='lines+markers',
                    name='Number of issues closed in the last month'
                )
            ],
            'layout': {
                'title': 'Number of Issues Closed in the Last Month'
            }
        }
    ),
    dcc.Graph(
        id='pull-requests-merged',
        figure={
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['pr_merged'],
                    mode='lines+markers',
                    name='Number of PRs merged in the last month'
                )
            ],
            'layout': {
                'title': 'Number of PRs merged in the Last Month'
            }
        }
    )
])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)