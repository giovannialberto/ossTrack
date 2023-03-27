# ossTrack
Keeping track of some important OSS metrics


## API

### Run locally
To run the flask app locally, use:

```
python api/app.py --database-url data/github_metrics.db
```

### Docker
To run the docker image of the api, use:

```
docker build -t my-api-image -f ./api/Dockerfile ./api
docker run -p 5000:5000 -v $(pwd)/data:/app/data my-api-image
```

### Docker Compose
To run the docker compose, use:

```
docker-compose up
```

## Fetch metrics script
### Python
To run with python:
```
python3 scripts/fetch_metrics.py
```

### Docker
To run with docker:

