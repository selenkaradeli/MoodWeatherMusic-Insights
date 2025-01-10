# example script just a placeholder for now:

import pandas as pd
import requests
from datetime import datetime, timedelta
import os

class WeatherDataFetcher:
    def __init__(self):
        self.base_url = "https://archive-api.open-meteo.com/v1/archive"
        self.lat = "41.0082"  # Istanbul coordinates
        self.lon = "28.9784"
        
    def fetch_weather_data(self, start_date, end_date):
        """Fetch historical weather data for a date range."""
        params = {
            'latitude': self.lat,
            'longitude': self.lon,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'hourly': ['temperature_2m', 'precipitation', 'weathercode'],
            'timezone': 'Europe/Istanbul'
        }
        
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return None

    def process_weather_data(self, raw_data):
        """Process raw weather data into structured format."""
        if not raw_data:
            return None
        
        hourly_data = []
        timestamps = raw_data['hourly']['time']
        temps = raw_data['hourly']['temperature_2m']
        precip = raw_data['hourly']['precipitation']
        weather_codes = raw_data['hourly']['weathercode']
        
        for i in range(len(timestamps)):
            hourly_data.append({
                'timestamp': pd.to_datetime(timestamps[i]),
                'temperature': temps[i],
                'precipitation': precip[i],
                'weather_code': weather_codes[i]
            })
            
        return pd.DataFrame(hourly_data)

def main():
    # Read date range from processed TikTok data
    date_range_path = 'data/processed/date_range.csv'
    if not os.path.exists(date_range_path):
        print("Please run parse_tiktok_data.py first to generate date range")
        return
        
    date_range = pd.read_csv(date_range_path)
    start_date = pd.to_datetime(date_range['start_date'].iloc[0])
    end_date = pd.to_datetime(date_range['end_date'].iloc[0])
    
    output_dir = 'data/weather_data'
    os.makedirs(output_dir, exist_ok=True)
    
    fetcher = WeatherDataFetcher()
    print(f"Fetching weather data from {start_date} to {end_date}...")
    
    raw_data = fetcher.fetch_weather_data(start_date, end_date)
    if raw_data:
        df = fetcher.process_weather_data(raw_data)
        if df is not None:
            df.to_csv(f"{output_dir}/hourly_weather.csv", index=False)
            print("Weather data saved successfully!")

if __name__ == "__main__":
    main() 