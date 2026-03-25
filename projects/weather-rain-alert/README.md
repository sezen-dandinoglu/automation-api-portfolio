# Weather Rain Alert

A simple Python project that checks upcoming precipitation data from a weather API and tells whether rain is expected in the next 12 hours.

## Project goal

I built this project to practice:

- working with APIs in Python
- parsing JSON responses
- applying conditional logic to real data
- handling request and response errors in a practical way

## Features

- calls the Open-Meteo API
- checks precipitation values for the next 12 hours
- prints whether rain is expected
- shows the first detected rain time and precipitation value
- handles connection, timeout, HTTP, and JSON parsing errors

## Tech stack

- Python
- requests

## How to run

```bash
cd projects/weather-rain-alert
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py

Example output
It will rain 🌧️

Time: 2026-03-25T14:00
Precipitation: 0.2