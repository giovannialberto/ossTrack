import os
import requests
import datetime
import sqlite3
import argparse


# Define command-line arguments
parser = argparse.ArgumentParser(description='Run the Flask app with a database URL')
parser.add_argument('--database-url', type=str, default='data/github_metrics.db',
                    help='The URL of the SQLite database')


def fetch_github(owner_name, repo_name):
    # Define the GitHub API endpoint
    api_endpoint = f"https://api.github.com/repos/{owner_name}/{repo_name}"

    # Define the date range for the issues and pull requests
    end_date = datetime.datetime.utcnow()
    start_date = end_date - datetime.timedelta(days=30)
    start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Make the API request to get the repository information
    response = requests.get(api_endpoint)
    repo_info = response.json()

    # Extract the required metrics from the repository information
    num_stars = repo_info["stargazers_count"]
    num_forks = repo_info["forks_count"]
    forks_to_stars_ratio = num_forks / num_stars
    num_subscribers = repo_info["subscribers_count"]

    # Make the API request to get the repository contributors
    response = requests.get(f"{api_endpoint}/contributors")
    contributors_info = response.json()
    num_contributors = len(contributors_info)

    # Make the API request to get the issues opened in the last month
    params = {
        "state": "all",
        "since": start_date_str
    }
    response = requests.get(f"{api_endpoint}/issues", params=params)
    issues = response.json()
    num_issues_opened = len([issue for issue in issues if "pull_request" not in issue])
    num_issues_closed = len([issue for issue in issues if "pull_request" not in issue and issue["state"] == "closed"])

    # Make the API request to get the pull requests merged in the last month
    params = {
        "state": "closed",
        "since": start_date_str
    }
    response = requests.get(f"{api_endpoint}/pulls", params=params)
    pull_requests = response.json()
    num_pull_requests_merged = len([pr for pr in pull_requests if pr["merged_at"] is not None and pr["merged_at"] > start_date_str])

    # Print the extracted metrics
    print(f"Number of stars: {num_stars}")
    print(f"Number of forks: {num_forks}")
    print(f"Forks to stars ratio: {forks_to_stars_ratio}")
    print(f"Number of subscribers: {num_subscribers}")
    print(f"Number of contributors: {num_contributors}")
    print(f"Number of issues opened in the last month: {num_issues_opened}")
    print(f"Number of issues closed in the last month: {num_issues_closed}")
    print(f"Number of pull requests merged in the last month: {num_pull_requests_merged}")

    # Create dictionary to store results
    results = {
        "num_stars": num_stars,
        "num_forks": num_forks,
        "forks_to_stars_ratio": forks_to_stars_ratio,
        "num_subscribers": num_subscribers,
        "num_contributors": num_contributors,
        "num_issues_opened": num_issues_opened,
        "num_issues_closed": num_issues_closed,
        "num_pull_requests_merged": num_pull_requests_merged
    }
    
    # Return results
    return results 



if __name__ == '__main__':
    # Parse command-line arguments
    args = parser.parse_args()

    # Get the repository name and owner
    repo_name = os.environ.get('REPO_NAME', 'pulsar')
    owner_name = os.environ.get('OWNER_NAME', 'Exein-io')

    # fetch the latest metrics
    metrics = fetch_github(owner_name=owner_name, repo_name=repo_name)

    # insert the metrics into the database
    date = datetime.date.today().strftime('%Y-%m-%d')
    conn = sqlite3.connect(args.database_url)
    c = conn.cursor()

    # Insert the computed metrics into the database
    c.execute('''INSERT OR IGNORE INTO metrics(date, stars, forks, subscribers, contributors, 
                                            issues_opened, issues_closed, pr_merged, forks_to_stars_ratio) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
            (date, metrics.get("num_stars"), metrics.get("num_forks"), metrics.get("num_subscribers"), metrics.get("num_contributors"), 
             metrics.get("num_issues_opened"), metrics.get("num_issues_closed"), metrics.get("num_pull_requests_merged"), metrics.get("forks_to_stars_ratio")))

    conn.commit()
    conn.close()