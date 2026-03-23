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

### 2. Install dependencies
```bash
python3 -m pip install -r requirements.txt

### 3. Run the script
```bash
python3 main.py

### Example output
Checking: https://api.github.com
Status: 200 OK
Response time: 0.27 seconds

Response Preview:
- current_user_url: https://api.github.com/user
- authorizations_url: https://api.github.com/authorizations
- repository_url: https://api.github.com/repos/{owner}/{repo}
--------------------------------------------------

Checking: https://api.agify.io/?name=sezen
Status: 200 OK
Response time: 0.19 seconds

Response Preview:
- count: 1234
- name: sezen
- age: 32
--------------------------------------------------

Checking: https://wrong-api-url.com
Connection error
--------------------------------------------------

### What I practiced
sending API requests with Python
measuring and interpreting response time
reading and previewing JSON responses
handling common API-related failures
building a small troubleshooting-oriented utility
