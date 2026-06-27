# Architecture

The project follows a layered architecture.

Client

↓

API Layer (FastAPI Routes)

↓

Service Layer (Business Logic)

↓

Machine Learning Layer (Whisper)

↓

Response

---

## Design Principles

- Separation of Concerns
- Single Responsibility Principle
- Modular Design
- Production-ready Structure

---

## Why this Architecture?

The API layer is responsible only for handling HTTP requests.

The Service layer contains all Machine Learning logic.

This separation makes the project easier to test, maintain and extend.