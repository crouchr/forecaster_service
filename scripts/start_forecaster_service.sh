#!/bin/bash
set -e

echo 'entered start_forecaster_service.sh'
#docker pull registry:5000/forecaster_service:1.0.0
docker-compose --verbose --no-ansi -f dev-forecaster-service-docker-compose.yml up

