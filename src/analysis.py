import pandas as pd

def load_data(filepath='data/global_trade_data.csv'):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_country_aggregates(df):
    """Aggregates trade volume by country for map visualization."""
    # Group by Origin Country
    origin_agg = df.groupby('Origin_Country')['Trade_Volume_USD'].sum().reset_index()
    origin_agg.columns = ['Country', 'Total_Export_Volume']
    
    # Group by Destination Country
    dest_agg = df.groupby('Destination_Country')['Trade_Volume_USD'].sum().reset_index()
    dest_agg.columns = ['Country', 'Total_Import_Volume']
    
    # Merge
    country_stats = pd.merge(origin_agg, dest_agg, on='Country', how='outer').fillna(0)
    country_stats['Total_Trade_Volume'] = country_stats['Total_Export_Volume'] + country_stats['Total_Import_Volume']
    
    return country_stats

def get_monthly_trends(df):
    """Aggregates trade volume by month for trend analysis."""
    # Ensure sorted by date
    df = df.sort_values('Date')
    # Resample to monthly
    monthly_trend = df.set_index('Date').resample('M')['Trade_Volume_USD'].sum().reset_index()
    return monthly_trend

if __name__ == "__main__":
    df = load_data()
    print("Country Aggregates Head:")
    print(get_country_aggregates(df).head())
    print("\nMonthly Trends Head:")
    print(get_monthly_trends(df).head())
