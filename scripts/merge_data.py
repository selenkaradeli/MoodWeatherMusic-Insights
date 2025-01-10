# example script just a placeholder for now:

import pandas as pd
import os
from datetime import datetime

# Weather code mapping for better readability
WEATHER_CODE_MAPPING = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Fog in the morning",
    51: "Drizzle",
    53: "Rain",
    55: "Heavy rain",
    61: "Showers",
    63: "Heavy showers",
    80: "Thunderstorm",
    81: "Snow",
    82: "Heavy snow",
    85: "Rain showers",
    86: "Snow showers"
}

def load_tiktok_data():
    """Load and combine all processed TikTok data."""
    tiktok_data = {}
    processed_dir = 'data/processed'
    
    for filename in os.listdir(processed_dir):
        if filename.endswith('.csv') and not filename.startswith(('merged_', 'date_range', 'processed')):
            name = filename.replace('.csv', '')
            file_path = os.path.join(processed_dir, filename)
            df = pd.read_csv(file_path)
            
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                # Round timestamps to the nearest hour for better matching
                df['timestamp'] = df['timestamp'].dt.floor('H')
                tiktok_data[name] = df
    
    return tiktok_data

def load_weather_data():
    """Load weather data and add weather descriptions."""
    weather_dir = 'data/weather_data'
    weather_data = pd.read_csv(os.path.join(weather_dir, 'hourly_weather.csv'))
    weather_data['timestamp'] = pd.to_datetime(weather_data['timestamp'])
    
    # Add weather description
    weather_data['weather_description'] = weather_data['weather_code'].map(WEATHER_CODE_MAPPING)
    
    return weather_data

def create_hourly_activity_counts(tiktok_data):
    """Create hourly activity counts for each type of interaction."""
    hourly_counts = {}
    
    for data_type, df in tiktok_data.items():
        # Count activities per hour
        hourly_counts[data_type] = (
            df.groupby('timestamp')
            .size()
            .reset_index(name=f'{data_type}_count')
        )
    
    # Merge all hourly counts
    base_df = pd.DataFrame()
    for data_type, counts in hourly_counts.items():
        if base_df.empty:
            base_df = counts
        else:
            base_df = pd.merge(base_df, counts, on='timestamp', how='outer')
    
    # Fill NaN values with 0 (hours with no activity)
    base_df = base_df.fillna(0)
    return base_df

def main():
    output_dir = 'data/merged_data'
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading TikTok data...")
    tiktok_data = load_tiktok_data()
    
    print("Loading weather data...")
    weather_data = load_weather_data()
    
    print("Creating hourly activity summary...")
    hourly_activity = create_hourly_activity_counts(tiktok_data)
    
    print("Merging with weather data...")
    final_dataset = pd.merge(
        hourly_activity,
        weather_data,
        on='timestamp',
        how='inner'
    )
    
    # Add time-based features
    final_dataset['hour'] = final_dataset['timestamp'].dt.hour
    final_dataset['day_of_week'] = final_dataset['timestamp'].dt.day_name()
    final_dataset['is_weekend'] = final_dataset['timestamp'].dt.dayofweek.isin([5, 6])
    
    # Calculate total activity per hour
    activity_columns = [col for col in final_dataset.columns if col.endswith('_count')]
    final_dataset['total_activity'] = final_dataset[activity_columns].sum(axis=1)
    
    # Save the final dataset
    output_path = os.path.join(output_dir, 'merged_data.csv')
    final_dataset.to_csv(output_path, index=False)
    print(f"Final dataset saved to {output_path}")
    
    # Print summary statistics
    print("\nDataset Summary:")
    print(f"Date Range: {final_dataset['timestamp'].min()} to {final_dataset['timestamp'].max()}")
    print(f"Total Hours: {len(final_dataset)}")
    print("\nActivity Totals:")
    for col in activity_columns:
        total = final_dataset[col].sum()
        print(f"{col}: {total:,.0f}")

if __name__ == "__main__":
    main() 