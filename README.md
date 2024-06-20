# ETL Pipeline with Pandas

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Pandas, a versatile library for data manipulation and analysis in Python. The pipeline extracts data from various sources, such as JSON and CSV files, transforms it through data cleaning, aggregation, and manipulation operations using Pandas DataFrames, and loads the transformed data into CSV output files.
## Technologies Used

- **Python:** Programming language used for scripting and data transformations.
- **Pandas:** Library for data manipulation and analysis.
- **Git:** Version control system for collaborative development.
- **Pytest:** Framework for testing Python code.
- **JSON and CSV:** File formats for data extraction and storage.

## Project Structure

The project is structured as follows:

- **main.py**: Entry point for the ETL pipeline, initializes Spark session and orchestrates the data flow.
- **scripts/**
  - **extract.py**: Contains classes for data extraction from JSON and CSV files.
  - **transform.py**: Implements data transformations using PySpark DataFrame API.
  - **load.py**: Handles loading of transformed data into a CSV file.
- **tests/**: Directory for unit tests.
- **data/**: Directory containing sample JSON and CSV data files.

## Pipeline Logic

1. **Initialization**: The `main.py` script initializes a Spark session to start processing data.
2. **Extraction**: Data is extracted from JSON and CSV files using the `Extract` class in `extract.py`.
3. **Transformation**: The `Transform` class in `transform.py` processes the extracted data. It performs operations like adding new columns, joining datasets, and ensuring data quality.
4. **Loading**: Transformed data is loaded into a CSV file using the `Load` class in `load.py`.
5. **Output**: The final output is stored in the `output/etl_output.csv` file.

## Problems Faced

1. **Schema Mismatch**: Ensuring that the schema of extracted data matches the expected format in transformation steps.
2. **Column Missing Errors**: Handling errors due to missing columns in extracted data files.
3. **Execution Plans**: Dealing with large execution plans in Spark, which required tuning the logging level and configuration parameters.
4. **Unit Testing**: Setting up unit tests with Pytest for ensuring the correctness of data transformations and pipeline behavior.

## Running the Project

To run the ETL pipeline:

1. Ensure you have Python and PySpark installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/jteoni/pandas-etl-nyctaxi
   cd pandas-etl-nyctaxi
3. Install dependencies:
   ```bash
   pip install -r requeriments.txt
4. Execute the main script:
   ```bash
   python main.py
