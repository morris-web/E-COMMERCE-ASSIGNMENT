# E-COMMERCE-ASSIGNMENT

A repository and pipeline for generating, processing, and indexing synthetic e-commerce customer behavior data for analytics and search using MeiliSearch.

## Project Overview

This project simulates e-commerce customer behavior, generates a dataset, and indexes it into a MeiliSearch instance for fast search and analytics. It is ideal for experimenting with search, analytics, and machine learning on realistic e-commerce data.

## Features
- Generate synthetic e-commerce customer data (`create_dataset.py`)
- Convert the dataset to JSON for search indexing (`test.py`)
- Index the dataset into MeiliSearch and run sample queries (`big_data.py`)
- Jupyter Notebooks for EDA and model training (see `Notebooks/`)

## Requirements
- Python 3.8+
- [MeiliSearch](https://www.meilisearch.com/) (self-hosted, Windows instructions below)
- Python packages (see `requirements.txt`):
  - `meilisearch`, `faker`, `pandas`, `numpy`, and more

Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup Instructions

### 1. Generate the Dataset
Run the following to create a synthetic e-commerce dataset:
```bash
python create_dataset.py
```
This creates `ecommerce_data_2k25.csv`.

### 2. Convert CSV to JSON
Convert the CSV to JSON format for MeiliSearch:
```bash
python test.py
```
This creates `dataset.json`.

### 3. Set Up MeiliSearch (Windows)
1. Download `meilisearch.exe` from [MeiliSearch Downloads](https://www.meilisearch.com/download).
2. Move it to your project folder or another accessible location.
3. Open Command Prompt and navigate to the folder:
   ```
   cd path\to\your\folder
   ```
4. Start the server with the provided master key:
   ```
   meilisearch.exe --master-key _r0BYxHVyU7qvaNaedwC0fr9As-fFrgGFYv52hL8IFQ
   ```
   Leave this window open. The server should be running at `http://localhost:7700`.

### 4. Index the Dataset
With MeiliSearch running and `dataset.json` present, run:
```bash
python big_data.py
```
This will:
- Connect to MeiliSearch
- Upload your dataset
- Print sample search results

### 5. (Optional) Explore MeiliSearch Web UI
Visit [http://localhost:7700](http://localhost:7700) in your browser to explore your indexes and documents.

## Troubleshooting
- **Connection errors:** Ensure MeiliSearch is running and listening on port 7700.
- **ModuleNotFoundError:** Make sure you installed dependencies in the correct Python environment.

## Notebooks
- See the `Notebooks/` directory for EDA and model training workflows.

## License
This project is for educational and demonstration purposes.
