# ossTrack
A simple monitor tool for keeping track of important OSS metrics evolution through time.

## Overview
The tool consists of three main services:

- a Rest [API](./api/) (port `5000`): lets you query each metric and export it for further custom visualizations
- a Web [Dashboard](./dashboard/) (port `8050`): lets you easily visualize all the metrics fetched so far
- the [fetch](./scripts/fetch_metrics.py) service: a simple script that collects all the latest metrics from the GitHub API and stores it in a local [database](./data/)

## Usage

### Prerequisites
You only need [docker compose](https://docs.docker.com/compose/install/) installed to run the monitoring tool.

### Set Up
Before launching the application, make sure to modify inside the [docker-compose.yml](./docker-compose.yml) file the name (`REPO_NAME`) and organization (`OWNER_NAME`) of the repository you want to track. Those are specified as environment variables for the `fetch` service.

Once you have setup the correct repo and organization name, simply launch osstrack with docker compose:

```
docker compose up
```

This will fetch the latest metrics from the GitHub API, store them in the SQLite DB it just created, and expose the API and Dashboard to let you export/visualize the results.

### Automate Fetching
By default, osstrack will fetch the latest up-to-date metrics from the GitHub API and store them in the DB alongside a unique **date** timestamp. It will only store one snapshot of the latest metrics **per day**.

What this means is that osstrack is meant to be run once every day. For this reason, it is very convenient to automate the daily execution of the docker compose, so that all the metrics can be updated every day.

This can be done simply with cron, for example:
```
0 0 * * * cd /path/to/osstrack && docker-compose restart
```
