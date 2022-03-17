#! /usr/bin/env sh
set -e
if [ ! "$(docker network ls | grep traefik-public)" ]; then
  echo "Creating network ..."
  docker network create traefik-public
else
  echo "Network exists ..."
fi
