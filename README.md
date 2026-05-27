# Discover Karabakh - FastAPI Microservice

This repository contains a lightweight, fully containerized backend microservice extracted from the broader **Discover Karabakh** project. It is specifically built to demonstrate modern backend development practices, data extraction, and asynchronous programming in Python.

## Key Features

* Asynchronous Architecture: Built with FastAPI utilizing `async/await` patterns to ensure high-performance, non-blocking API endpoints.
* Data Extraction & Parsing: Uses `pandas` to read, parse, and process structured data from CSV sources (`regions.csv`), ensuring clean data delivery.
* Smart Thread Management: Synchronous file I/O operations are offloaded to background threads using `asyncio.to_thread` to prevent event loop blocking.
* Containerization: Fully orchestrated using Docker and Docker Compose for a seamless, "works-on-my-machine" local development experience.
* Interactive Documentation: Out-of-the-box Swagger UI integration for easy API testing and client integration.

---

## Tech Stack

| Category | Technology |
| :--- | :--- |
| **Framework** | Python 3.10, FastAPI |
| **Data Processing** | Pandas |
| **Server** | Uvicorn |
| **DevOps** | Docker, Docker Compose |

---

## Getting Started

Running this microservice requires zero local Python configuration. All you need is Docker installed on your machine.

1. Clone the repository:

git clone [https://github.com/ilkinabdulla1/FastAPI-Dataparser-poc.git]
cd fastapi-data-parser-poc

2. Build and start the container:

docker-compose up --build

3. Access the Application:

Once the container is running, open your browser and navigate to:

API Response: http://localhost:8000/api/regions

Swagger UI Docs: http://localhost:8000/docs

## Project Structure

main.py — The core FastAPI application containing async endpoints and data processing logic.

regions.csv — The structured data source simulating external file extraction.

Dockerfile — Slim, optimized container definition.

docker-compose.yml — Service orchestration with volume mapping for hot-reloading.

requirements.txt — Project dependencies.

## About This Demo

While my primary frontend stack relies heavily on React and TypeScript, I built this specific microservice to showcase my adaptability to backend environments using Python and FastAPI. It reflects my commitment to writing clean code, understanding containerization workflows, and safely handling data from diverse formats.