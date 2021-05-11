#/bin/sh

docker-compose build
docker-compose run --rm test python -m black --diff --check src/ tests/
docker-compose run --rm test python -m flake8 src/ tests/