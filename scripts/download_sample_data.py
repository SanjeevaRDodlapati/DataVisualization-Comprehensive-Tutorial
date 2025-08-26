#!/usr/bin/env python3
"""
Data Download Script for Data Visualization Comprehensive Series
==============================================================

This script downloads all sample datasets used in the tutorial series.
Datasets are organized by module and include real-world data sources.

Usage:
    python scripts/download_sample_data.py
    python scripts/download_sample_data.py --module 5  # Download specific module
    python scripts/download_sample_data.py --quick     # Download minimal samples only
"""

import os
import sys
import requests
import zipfile
import gzip
import pandas as pd
from pathlib import Path
import argparse
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Data directory
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def download_file(url, filepath, description="Downloading"):
    """Download a file with progress bar."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filepath, 'wb') as file, tqdm(
        desc=description,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for chunk in response.iter_content(chunk_size=8192):
            size = file.write(chunk)
            pbar.update(size)

def download_gapminder_data():
    """Download Gapminder data for Module 1."""
    logger.info("Downloading Gapminder data...")
    
    # Gapminder life expectancy, population, and GDP data (working URL)
    gapminder_url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
    download_file(gapminder_url, DATA_DIR / "gapminder.csv", "Gapminder dataset")

def download_palmer_penguins():
    """Download Palmer Penguins data for Module 1."""
    logger.info("Downloading Palmer Penguins data...")
    
    penguins_url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
    download_file(penguins_url, DATA_DIR / "penguins.csv", "Palmer Penguins dataset")

def download_covid_data():
    """Download COVID-19 data for Module 2."""
    logger.info("Downloading COVID-19 data...")
    
    # Johns Hopkins COVID-19 data (archived)
    covid_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    download_file(covid_url, DATA_DIR / "covid19_confirmed_global.csv", "COVID-19 confirmed cases")

def download_climate_data():
    """Download climate data for Module 3."""
    logger.info("Downloading climate data...")
    
    # Berkeley Earth global temperature data (sample)
    # Note: This is a simplified version for tutorial purposes
    climate_url = "https://raw.githubusercontent.com/plotly/datasets/master/2016-weather-data-seattle.csv"
    download_file(climate_url, DATA_DIR / "seattle_weather.csv", "Seattle weather data")

def download_geospatial_data():
    """Download geospatial data for Modules 5-7."""
    logger.info("Downloading geospatial data...")
    
    # Natural Earth data - Countries
    countries_url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip"
    countries_zip = DATA_DIR / "ne_50m_admin_0_countries.zip"
    download_file(countries_url, countries_zip, "Natural Earth countries")
    
    # Extract zip file
    with zipfile.ZipFile(countries_zip, 'r') as zip_ref:
        zip_ref.extractall(DATA_DIR / "natural_earth")
    
    # US States for choropleth examples
    states_url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    download_file(states_url, DATA_DIR / "us_counties.geojson", "US counties GeoJSON")

def download_sample_datasets():
    """Download sample datasets for various modules."""
    logger.info("Downloading additional sample datasets...")
    
    # Tips dataset for statistical examples
    tips_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    download_file(tips_url, DATA_DIR / "tips.csv", "Tips dataset")
    
    # Flights dataset for time series
    flights_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    download_file(flights_url, DATA_DIR / "flights.csv", "Flights dataset")
    
    # Iris dataset for correlation examples
    iris_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    download_file(iris_url, DATA_DIR / "iris.csv", "Iris dataset")

def create_synthetic_data():
    """Create synthetic datasets for specific examples."""
    logger.info("Creating synthetic datasets...")
    
    # Large dataset sample for big data module
    import numpy as np
    np.random.seed(42)
    
    n_points = 100000
    synthetic_large = pd.DataFrame({
        'x': np.random.normal(0, 1, n_points),
        'y': np.random.normal(0, 1, n_points),
        'category': np.random.choice(['A', 'B', 'C'], n_points),
        'value': np.random.exponential(1, n_points)
    })
    synthetic_large.to_csv(DATA_DIR / "synthetic_large_dataset.csv", index=False)
    
    # Time series with uncertainty
    dates = pd.date_range('2020-01-01', periods=365, freq='D')
    trend = np.linspace(0, 10, 365)
    noise = np.random.normal(0, 1, 365)
    uncertainty = np.random.uniform(0.5, 2.0, 365)
    
    time_series_data = pd.DataFrame({
        'date': dates,
        'value': trend + noise,
        'lower_ci': trend + noise - uncertainty,
        'upper_ci': trend + noise + uncertainty
    })
    time_series_data.to_csv(DATA_DIR / "time_series_with_uncertainty.csv", index=False)

def download_module_data(module_num):
    """Download data for a specific module."""
    module_map = {
        1: [download_gapminder_data, download_palmer_penguins],
        2: [download_covid_data, download_sample_datasets],
        3: [download_climate_data],
        5: [download_geospatial_data],
        6: [download_geospatial_data],
        7: [download_geospatial_data],
        8: [create_synthetic_data]
    }
    
    if module_num in module_map:
        for func in module_map[module_num]:
            func()
    else:
        logger.warning(f"No specific data download function for module {module_num}")

def main():
    parser = argparse.ArgumentParser(description="Download sample data for Data Visualization Tutorial Series")
    parser.add_argument("--module", type=int, help="Download data for specific module only")
    parser.add_argument("--quick", action="store_true", help="Download minimal sample data only")
    
    args = parser.parse_args()
    
    logger.info("Starting data download for Data Visualization Tutorial Series")
    logger.info(f"Data will be saved to: {DATA_DIR.absolute()}")
    
    try:
        if args.module:
            logger.info(f"Downloading data for Module {args.module} only")
            download_module_data(args.module)
        elif args.quick:
            logger.info("Quick download: essential datasets only")
            download_gapminder_data()
            download_palmer_penguins()
            download_sample_datasets()
        else:
            logger.info("Downloading all tutorial datasets")
            download_gapminder_data()
            download_palmer_penguins()
            download_covid_data()
            download_climate_data()
            download_geospatial_data()
            download_sample_datasets()
            create_synthetic_data()
        
        logger.info("✅ Data download completed successfully!")
        logger.info(f"📁 Data available in: {DATA_DIR.absolute()}")
        
        # List downloaded files
        files = list(DATA_DIR.rglob("*"))
        data_files = [f for f in files if f.is_file() and f.suffix in ['.csv', '.geojson', '.shp']]
        logger.info(f"📊 Downloaded {len(data_files)} data files")
        
    except Exception as e:
        logger.error(f"❌ Error downloading data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
