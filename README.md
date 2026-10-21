# AQI Forecasting System

Forecasts PM2.5 air pollution levels 24 hours ahead for Indian cities.

Work in progress. Currently, the project foundation is set up: Python environment, PostgreSQL database, migrations, tests and CI.

## Tech stack

Python 3.12, uv, PostgreSQL, SQLAlchemy, Alembic, Docker, pytest, Ruff, GitHub Actions

## How to run

You need Git, uv and Docker Desktop installed.

```powershell
git clone https://github.com/Kopal05/aqi-forecast.git
cd aqi-forecast

Copy-Item .env.example .env   # then set your password in .env

uv sync
docker compose up -d
uv run alembic upgrade head
uv run pytest -v
```

## Stop the database

```powershell
docker compose stop
```
