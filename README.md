# Receipt Processor

This project implements a web service for processing receipts and calculating points based on predefined rules. The service is designed to fulfill the documented API specifications provided by Fetch Rewards.

## Overview

The Receipt Processor service provides two main endpoints:
- **Process Receipts:** Accepts a receipt in JSON format and returns a unique ID for the receipt.
- **Get Points:** Returns the number of points awarded for a receipt based on its ID.

## API Specification

### Endpoint: Process Receipts

- **Path:** `/receipts/process`
- **Method:** `POST`
- **Payload:** Receipt JSON
- **Response:** JSON containing an ID for the receipt.

Example Response:
```json
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

### Endpoint: Get Points

- **Path:** `/receipts/{id}/points`
- **Method:** `GET`
- **Response:** A JSON object containing the number of points awarded.

Example Response:
```json
{ "points": 32 }
```

## Points Calculation Rules

- 1 point for every alphanumeric character in the retailer name.
- 50 points if the total is a round dollar amount with no cents.
- 25 points if the total is a multiple of `0.25`.
- 5 points for every two items on the receipt.
- If the trimmed length of the item description is a multiple of 3, multiply the price by `0.2` and round up to the nearest integer. The result is the number of points earned.
- 6 points if the day in the purchase date is odd.
- 10 points if the time of purchase is after 2:00pm and before 4:00pm.

## Setup Instructions

### Method A: Running with Docker Compose

#### Prerequisites

- Docker and Docker Compose

#### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/JoshJarabek7/fetch_rewards.git
   cd fetch_rewards
   ```

2. Build and run the application using Docker Compose:
   ```bash
   docker compose up --build
   ```

3. The application will be available at `http://localhost:8001`.

### Method B: Running Locally with Python and Poetry

#### Prerequisites

- Python 3.13 (or compatible version)
- Poetry for dependency management

#### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/JoshJarabek7/fetch_rewards.git
   cd fetch_rewards
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Run the application:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

4. The application will be available at `http://localhost:8001`.

## Testing

### Running Tests with Poetry

To run tests using Poetry:

```bash
poetry run pytest
```

### Running Tests Inside Docker

To run tests inside a Docker container:

```bash
docker compose run tests
```

## Documentation

To build the Sphinx documentation:

1. Navigate to the `docs` directory:
   ```bash
   cd docs
   ```

2. Build the documentation:
   ```bash
   make html
   ```

3. Open `_build/html/index.html` in a browser to view the documentation.