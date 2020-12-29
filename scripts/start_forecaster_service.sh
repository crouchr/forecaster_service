#!/bin/bash
set -e

echo 'entered start_forecaster_service.sh'
docker-compose -f dev-forecaster-service-docker-compose.yml up &
echo 'exited start_forecaster_service.sh'
