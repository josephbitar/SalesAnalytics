# Sales Data Analysis with Elasticsearch and Flask

This project provides a simple API for analyzing sales data using Elasticsearch and Flask. It exposes three endpoints to perform different operations on sales data stored in Elasticsearch. Please make sure to install Elasticsearch and required Python dependencies before using this application.

## Installation

### Prerequisites

- Python 3.x installed
- Elasticsearch installed locally
- Insert the documents provided in documents file under "sales" index.

### Steps

1. **Clone this repository:**

    ```bash
    git clone https://github.com/your-username/sales-data-analysis.git
    cd sales-data-analysis
    ```

2. **Install required Python packages:**

    ```bash
     pip install requests Flask   
     pip install elasticsearch    
    ```

3. **Start the Flask server:**

    ```bash
    python app.py
    ```

## Endpoints

### 1. Search Sales Data

**Endpoint:** `/search` (POST)
- **Description:** Searches for documents based on a field name and its value. 
- **Request Body:** 
  - `field`: Field name to search in Elasticsearch
  - `value`: Value to search for in the specified field

Example Request Body:
```json
{
  "field": "product_name",
  "value": "Electronic"
}
```

### 2. Search Sales Data

**Endpoint:** `/sum-sales` (GET)
- **Description:** Calculates the total sum of all sales data.

### 3. Sales Trends Analysis

**Endpoint:** `/analyze-trends` (GET)
- **Description:** Analyzes sales trends by aggregating sales data based on categories and their sales.


## Usage:
1. Make sure Elasticsearch is running locally.
2. Send HTTP requests to the provided endpoints using tools like cURL, Postman, or any programming language's HTTP library.

