# Experiment No. 8 – Docker

## Aim
To understand Docker and containerize a Machine Learning application.

## Introduction
Docker is a platform used to build, package, and run applications inside containers.

## Tools Used
- Docker Desktop
- Python
- Flask
- GitHub

## Files
- `app.py` – Flask application
- `requirements.txt` – Required Python library
- `Dockerfile` – Instructions to build Docker image

## Implementation
1. Created a Flask application using Python.
2. Created a Dockerfile.
3. Built Docker image using `docker build -t ml-docker-app .`
4. Ran the container using `docker run -d -p 5000:5000 --name ml-container ml-docker-app`
5. Tested the application at `http://localhost:5000`.

## Output
Machine Learning Application is Running!

Status: Success

## Result
Successfully created a Docker image, ran a container, and tested the containerized Flask application.
