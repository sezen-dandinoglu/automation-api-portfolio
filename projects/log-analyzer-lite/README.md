# Log Analyzer Lite

A simple Python tool that reads a log file and analyzes the number of:

- ERROR messages
- WARNING messages
- INFO messages

It provides a summary both in the terminal and in an output file.

## Project goal

This project was built to practice:

- reading and processing log files
- basic text parsing
- building troubleshooting-oriented tools
- working with file input/output in Python

## Features

- Reads log files line by line
- Counts occurrences of ERROR, WARNING, and INFO
- Case-insensitive matching
- Prints a clean summary in the terminal
- Writes results to an output file

## Tech stack

- Python

## How to run

```bash
cd projects/log-analyzer-lite
python3 main.py

**## Example output**

Log Summary
--------------------
ERROR: 3
WARNING: 2
INFO: 4
Total entries matched: 9

Notes
The sample log file contains synthetic (dummy) data.
The analysis output file is not tracked in version control.
