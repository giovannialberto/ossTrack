import requests
from datetime import datetime, timedelta

# Define the repository name and owner
repo_name = "pulsar"
owner_name = "Exein-io"

# Define the GitHub API endpoint
api_endpoint = f"https://api.github.com/repos/{owner_name}/{repo_name}"

# Define the date range for the issues and pull requests
end_date = datetime.utcnow()
start_date = end_date - timedelta(days=30)
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
