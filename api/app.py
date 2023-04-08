import argparse
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Define command-line arguments
parser = argparse.ArgumentParser(description='Run the Flask app with a database URL')
parser.add_argument('--database-url', type=str, default='data/github_metrics.db',
                    help='The URL of the SQLite database')

# Endpoint to fetch number of stars for a date range
@app.route('/stars')
def get_stars():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, stars FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)


# Endpoint to fetch number of forks for a date range
@app.route('/forks')
def get_forks():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, forks FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)

# Endpoint to fetch forks to stars ratio for a date range
@app.route('/forks-to-stars')
def get_forks_to_stars():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, forks_to_stars_ratio FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)

# Endpoint to fetch number of subscribers for a date range
@app.route('/subscribers')
def get_subscribers():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, subscribers FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)

# Endpoint to fetch number of contributors for a date range
@app.route('/contributors')
def get_contributors():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, contributors FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)

# Endpoint to fetch number of issues opened for a date range
@app.route('/issues-opened')
def get_issues_opened():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, issues_opened FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)

# Endpoint to fetch number of issues closed for a date range
@app.route('/issues-closed')
def get_issues_closed():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()
    
    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    query = f"SELECT date, issues_closed FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()
    
    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }
    
    conn.close()
    return jsonify(result)

# Endpoint to fetch number of PRs merged for a date range
@app.route('/prs-merged')
def get_prs_merged():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()

    if start_date_str is None and end_date_str is None:
        # By default, return last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    else:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    query = f"SELECT date, pr_merged FROM metrics WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    c.execute(query)
    rows = c.fetchall()

    result = {
        'data': [{
            'date': row[0],
            'value': row[1]
        } for row in rows]
    }

    conn.close()
    return jsonify(result)


if __name__ == '__main__':
    # Parse command-line arguments
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=8080, debug=True)