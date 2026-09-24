# Python REST API with FastAPI

This project is a hands-on journey through building production-style REST APIs with FastAPI, from the fundamentals of web communication to deploying an AI agent as an API.

## What You Will Learn

- How APIs work and how the frontend, backend, and database communicate
- The HTTP protocol, routes, path parameters, and query parameters
- HTTP methods: `GET`, `POST`, `PUT`, and `DELETE`
- CRUD operations through a complete Product API
- Data validation with Pydantic DTOs and schemas
- HTTP status codes and custom exception handling
- Sending emails with FastAPI-Mail
- Running long-running work efficiently with background tasks
- Generative AI and large language models (LLMs)
- Connecting LLMs with LangChain
- Using the Groq API for fast LLM inference
- Building an AI agent with tools, including Google Search integration
- Deploying the AI agent as a REST API with LangServe
- Connecting the agent to LangGraph Studio and Agent Chat UI

## Project Goals

By the end of this project, you will have a practical understanding of FastAPI development and a foundation for building, integrating, and deploying AI-powered backend services.

## Tech Stack

- Python
- FastAPI
- Pydantic
- FastAPI-Mail
- LangChain
- Groq API
- LangServe
- LangGraph Studio

## Getting Started

Create and activate the virtual environment, then start the FastAPI development server:

```bash
source envv/bin/activate
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive API documentation is available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
