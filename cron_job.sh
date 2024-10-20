#!/bin/bash

docker compose build

while true; do
  docker compose up --remove-orphans
  sleep 10
done
