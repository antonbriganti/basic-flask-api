#/bin/sh

export LATEST_COMMIT_SHA=$(git rev-parse HEAD)
docker-compose build
docker-compose up app