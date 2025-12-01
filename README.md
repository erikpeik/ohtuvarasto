# ohtuvarasto

[![Build Status](https://github.com/erikpeik/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/erikpeik/ohtuvarasto/actions)
[![codecov](https://codecov.io/github/erikpeik/ohtuvarasto/graph/badge.svg?token=JW3HZT0LLK)](https://codecov.io/github/erikpeik/ohtuvarasto)

## Web Application

A Flask-based web interface for managing multiple warehouses.

### Features

- Create new warehouses with custom names and capacity
- Add or take content from warehouses
- Delete warehouses
- View all warehouses and their current stock levels

### Running the Application

```bash
poetry install
cd src
poetry run flask --app app run
```

Then open http://127.0.0.1:5000 in your browser.
