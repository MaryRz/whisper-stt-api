# Sprint 3

## Goal

Build a secure and production-ready file upload mechanism for the Whisper STT API.

Instead of directly accepting and saving user-uploaded files, this sprint focuses on implementing secure file management utilities that prevent common security issues and prepare the project for production deployment.

---

## Completed

- Created `app/utils/file_manager.py`
- Created `app/core/config.py`
- Implemented secure filename generation using UUID
- Implemented file extension validation
- Centralized upload directory configuration

---

## Security Decisions

### 1. UUID-based Filenames

User-provided filenames are never used as the storage filename.

Instead, each uploaded file receives a randomly generated UUID while preserving its original extension.

Example:

```
Original:
meeting.wav

Stored:
550e8400-e29b-41d4-a716-446655440000.wav
```

**Reason**

- Prevent filename collisions
- Prevent overwriting existing files
- Reduce security risks related to user-controlled filenames

---

### 2. File Extension Validation

Only supported audio formats are accepted.

Current supported extensions:

- `.wav`
- `.mp3`
- `.m4a`
- `.flac`
- `.ogg`

**Reason**

Reject unsupported or potentially dangerous files before processing.

---

### 3. Centralized Upload Directory

The upload directory is defined inside `core/config.py`.

This keeps configuration separated from business logic and makes future migration to environment variables straightforward.

---

## Design Decisions

The file management logic is intentionally separated from the API layer.

Responsibilities are divided as follows:

- API Layer → Receive HTTP requests
- File Manager → Validate and generate safe filenames
- Service Layer → Perform Whisper inference

This design follows the **Single Responsibility Principle (SRP)** and **Separation of Concerns (SoC)**.

---

## Interview Notes

### Question

Why didn't you save uploaded files using their original filenames?

### Answer

Using user-provided filenames can lead to filename collisions, overwriting existing files, and potential security risks. I generated UUID-based filenames to ensure uniqueness and avoid relying on user-controlled input.

---

### Question

Why did you create a separate File Manager instead of placing everything inside the route?

### Answer

The API layer should only handle HTTP communication. File validation and file management are separate responsibilities and belong in a dedicated utility module. This makes the project easier to maintain, test, and extend.

---

### Question

Why validate file extensions?

### Answer

File validation is the first layer of defense. It prevents unsupported file types from reaching the Machine Learning pipeline and reduces unnecessary processing and security risks.

---

## Engineering Journal

This sprint reinforced the importance of designing secure software before adding functionality.

Initially, it seemed easier to save uploaded files directly using their original filenames. However, I learned that production systems should never trust user input blindly.

Separating file management into its own module also improved the overall architecture and made the codebase more maintainable.

---

## Tech Lead Review

### Strengths

- Good separation of responsibilities
- Secure filename generation
- Clean project organization
- Configuration isolated from business logic

### Improvements

- Add MIME type validation
- Limit maximum upload size
- Implement exception handling
- Automatically remove temporary files after transcription

### Overall Evaluation

**9.3 / 10**

The project is moving from a simple proof of concept toward a production-ready backend service. The architectural decisions made in this sprint provide a solid foundation for future development.