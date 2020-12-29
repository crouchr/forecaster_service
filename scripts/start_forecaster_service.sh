#!/bin/bash
set -e

echo 'entered start_forecaster_service.sh'
#docker pull registry:5000/forecaster_service:latest
docker-compose -f dev-forecaster-service-docker-compose.yml up

