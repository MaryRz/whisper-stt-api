# ADR-001

## Title
Separate Storage Layer

## Status
Accepted

## Context
Routes should not manage filesystem operations.

## Decision
A dedicated Storage Layer was introduced.

## Consequences
- Better maintainability
- Easier cloud migration
- Improved testability