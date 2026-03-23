# API Monitor Lite

A lightweight Python tool that checks multiple API endpoints and reports:

- HTTP status code
- response time
- JSON response preview
- common request errors such as timeout, connection, and HTTP errors

## Project goal

I built this project to practice API troubleshooting in a practical way and to strengthen skills relevant to technical support and production systems work.

The focus of the project is not only sending requests, but also handling failures clearly and presenting useful diagnostic output.

## Features

- Checks multiple API endpoints
- Measures response time
- Displays status code and status text
- Parses JSON responses safely
- Handles:
  - connection errors
  - timeouts
  - HTTP errors
  - non-JSON responses

## Tech stack

- Python
- requests

## How to run

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
