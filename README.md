# Lab 1 - CI/CD Web Service

## Description

A simple REST API web service for managing items.

## Technologies

- Python
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub
- Azure DevOps
- Docker Hub

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/items | Get all items |
| GET | /api/items/{id} | Get item by ID |
| POST | /api/items | Create item |
| PUT | /api/items/{id} | Update item |
| DELETE | /api/items/{id} | Delete item |

## Run locally

pip install -r requirements.txt
uvicorn app.main:app --reload

## Swagger UI:

http://localhost:8000/docs

## Run tests

pytest

## Build Docker image

docker build -t lab1-cicd .

## Run Docker container

docker run -d -p 8000:8000 --name lab1-container lab1-cicd
