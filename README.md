# Home Sales Analysis

This project analyses home sales data using PySpark and SQL. It involves reading a dataset from AWS S3, performing various queries to extract insights, and comparing runtimes for different operations, including caching and partitioning the data.

## Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Notebooks](#running-the-notebooks)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Project Overview
This project uses PySpark to analyse home sales data. The analysis includes calculating average prices for homes based on various criteria such as the number of bedrooms, bathrooms, and the year the home was built. Additionally, the project explores the performance impact of caching and partitioning the data.

## Repository Structure
```plaintext
Home-Sales/
├── .gitignore
├── README.md
├── repo_structure.py
├── requirements.txt
├── collab_jupyter/
│   ├── content/
│   │   └── home_sales_partitioned/
│   └── notebooks/
│       └── Home_Sales_starter_code_colab.ipynb
├── local_jupyter/
│   ├── data/
│   │   ├── home_sales_output.csv
│   │   └── home_sales_revised.csv
│   └── notebooks/
│       └── Home_Sales_starter_code.ipynb
└── Starter_Code/
    ├── Home_Sales_starter_code.ipynb
    └── Home_Sales_starter_code_colab.ipynb
```

- **collab_jupyter/**: Contains the work done in Google Colab, including the partitioned Parquet data and the notebook used.
- **local_jupyter/**: Contains the local Jupyter notebook and related data files. I could not set up Java and Hadoop, but wanted to explore doing this in Visual Studio. This is not part of the main submission because much of the functionality was removed due to the challenges.
- **Starter_Code/**: The original starter code provided for the challenge.
- **requirements.txt**: Lists the dependencies required for this project.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- [PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
- [Pandas](https://pandas.pydata.org/)
- [Google Colab](https://colab.research.google.com/) for running notebooks in the cloud

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/Home-Sales.git
   cd Home-Sales
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv home_sales_env
   source home_sales_env/bin/activate  # On Windows: home_sales_env\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Notebooks
- **Google Colab:**
  - Open the notebook `collab_jupyter/notebooks/Home_Sales_starter_code_colab.ipynb` in Google Colab.
  - Run the cells in order. You can upload the partitioned Parquet files and run the queries accordingly.

- **Local Jupyter Notebook:**
  - Open the notebook `local_jupyter/notebooks/Home_Sales_starter_code.ipynb` in your local Jupyter environment.
  - Ensure the CSV files are correctly placed in the `data/` directory, then run the cells in order.

## Usage
This project is intended for educational purposes and demonstrates how to use PySpark for data analysis, including advanced operations like caching, partitioning, and performance comparisons.

## Results
- **Query Performance:** The project explores the performance of queries on cached vs. uncached data, as well as partitioned vs. non-partitioned data.
- **Data Insights:** The analysis provides insights into how home prices vary by different criteria, such as the number of bedrooms, bathrooms, and the year the home was built.

