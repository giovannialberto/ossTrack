import sqlite3

conn = sqlite3.connect('github_metrics.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS metrics
             (date TEXT, stars INTEGER, forks INTEGER, subscribers INTEGER, contributors INTEGER, 
              issues_opened INTEGER, issues_closed INTEGER, pr_merged INTEGER, forks_to_stars_ratio real,
              UNIQUE(date))''')

conn.commit()
conn.close()