#! /usr/bin/env sh
set -e
if [ ! "$(docker network ls | grep traefik-public)" ]; then
  echo "Creating traefik-public network ..."
  docker network create traefik-public
else
  echo "traefik-public network exists."
fi
