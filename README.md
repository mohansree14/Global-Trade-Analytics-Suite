# Global Trade Data Analysis Simulation

## Project Overview
This project simulates and analyzes international trade patterns to demonstrate data analysis and predictive modeling capabilities. It was built to substantiate the following resume points:

- **Analyzed international trade patterns** using statistical modeling and geospatial analysis.
- **Created predictive models for market trends** with ~88% forecasting accuracy.
- **Developed interactive visualizations** for complex economic datasets.

## Features
- **Synthetic Data Generation**: Creates a realistic dataset of global trade transactions including Origin, Destination, Product, Volume (USD), and Weight (KG).
- **Geospatial Analysis**: Interactive Choropleth maps showing trade volume by country.
- **Predictive Modeling**: Random Forest Regressor trained to predict Trade Volume based on year, month, country, and product.
- **Interactive Dashboard**: Built with Streamlit for data exploration and trend visualization.

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```
   The app will automatically generate the synthetic data if it doesn't exist.

## Project Structure
- `src/generate_data.py`: Script to generate synthetic trade data.
- `src/analysis.py`: Functions for data aggregation and analysis.
- `src/model.py`: Predictive model training and evaluation.
- `app.py`: Streamlit application entry point.
- `data/`: Directory where the dataset is stored (`global_trade_data.csv`).
