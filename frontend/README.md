<h1 align="center">ML Models (Frontend)</h1>
<p align="center">Build, deploy and monitor machine learning models 🤖</p>

## Installation

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

## Deployment

The frontend application is running at [www.mlmodels.org](https://www.mlmodels.org). It is deployed via GitHub through Netlify.
