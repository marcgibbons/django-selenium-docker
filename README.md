# Example: Django Selenium Tests with Docker

## Requirements

- Docker & Docker compose

## Installation

```bash
docker compose build
```

## Start Selenium

```bash
docker compose up -d selenium
```

## Connect to browser using noVNC

On your host, open http://localhost:7900 and click "Connect".

## Run tests

```
docker compose run --rm --use-aliases django pytest
```

You can interact with the browser using breakpoints.

Example: drop into pdb at the beginning of each test with `--trace`.

```
docker compose run --rm --use-aliases django pytest --trace
```
