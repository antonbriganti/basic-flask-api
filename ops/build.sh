#/bin/sh

COMMIT_SHA = $(git rev-parse HEAD)

echo "latest build sha is $(git rev-parse HEAD)"
docker build -t anton-basic-flask-api:latest --target app --build-arg LATEST_COMMIT_SHA=$COMMIT_SHA .