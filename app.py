import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import sqlite3

# Connect to the SQLite database and retrieve the data
conn = sqlite3.connect('github_metrics.db')
df = pd.read_sql_query("SELECT * FROM metrics WHERE date >= DATE('now', '-30 days')", conn)
conn.close()

# Convert the 'date' column to a pandas datetime object
df['date'] = pd.to_datetime(df['date'])

# Create the Dash app
app = dash.Dash(__name__)

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
    app.run_server(debug=False)
