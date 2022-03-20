<h1 align="center">ML Models</h1>
<p align="center">Build, deploy and monitor machine learning models 🤖</p>

## Overview

`ML Models` is a showcase of popular machine learning models.

* frontend: [www.mlmodels.org](https://www.mlmodels.org)
* backend: [api.mlmodels.org](https://api.mlmodels.org/docs)

### Frontend

* `TypeScript`
* `React`
* `React-Query` - data synchronization
* `Styled Components` - styling
* `NextUI` - styling
* `Netlify` - CI/CD and hosting

### Backend

* `Python`
* `Poetry` - dependency management and packaging
* `FastAPI` - API
* `ONNX` - machine learning models and inference runtime
* `Traefik` - reverse proxy and SSL
* `Docker Compose` - deployment
* `GitHub Actions` - CI/CD
* `DigitalOcean` - hosting

## Installation

### Frontend

* install packages:

```shell
yarn install
```

* add environment variables to `.env` file in project root:

```txt
#.env
REACT_APP_MNIST_URL=<backend_url>/v1/predict/mnist
```

* run app for development:

```shell
yarn start
```

* build app for production in `build` folder:

```shell
yarn build
```

### Backend

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

### Frontend

The frontend application is running at [www.mlmodels.org](https://www.mlmodels.org). It is deployed via GitHub through Netlify.

### Backend

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
