<h1 align="center">ML Models (Backend)</h1>
<p align="center">Build, deploy and monitor machine learning models 🤖</p>

## Installation

* install packages:

```shell
poetry install
```

* add environment variables to `.env` file in project root:

```txt
#.env
CORS_ORIGINS=<frontend_url>
```

* run app for development:

```shell
poetry run python scripts/main.py
```

## Deployment

The backend application is running at [api.mlmodels.org](https://api.mlmodels.org/docs). It is deployed via GitHub through GitHub Actions using Docker and Docker Compose.

The following GitHub secrets are required:

* `BACKEND_URL` - the URL of the backend
* `DASHBOARD_PASSWORD` - the password for the Traefik dashboard
* `DASHBOARD_URL` - the URL of the Traefik dashboard
* `FRONTEND_URL` - the URL of the frontend
* `HOST` - the ssh host
* `KEY` - the ssh private key of the client
* `PORT` - the ssh port of the server
* `USERNAME` - the ssh username
