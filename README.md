# Number Analyzer API

A simple Flask API that counts positive numbers and sums negative numbers from a list.

---

## Features

- Count positive numbers
- Sum negative numbers
- Ignore zeros
- Simple REST API using Flask

---

## Tech Stack

- Python
- Flask

---

## Project Structure


---
number-analyzer-api/
│── app.py
│── README.md

## How to Run

### 1. Install Flask
pip install flask

### 2. Run the app
python app.py


### 3. Open in browser
http://127.0.0.1:5000/

---

## API Usage

### Endpoint
POST /analyze

### URL
http://127.0.0.1:5000/analyze

---

## Example Input

```json
{
  "numbers": [3, -1, 0, 7, -5, 8, -2]
}
example output
[3, -8]