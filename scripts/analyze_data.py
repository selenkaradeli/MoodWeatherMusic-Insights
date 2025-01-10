import pandas as pd
import numpy as np
from scipy import stats
import os

class TikTokWeatherAnalyzer:
    def __init__(self, data_path='data/merged_data/merged_data.csv'):
        self.df = pd.read_csv(data_path)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        
    def calculate_basic_stats(self):
        """Calculate basic statistics about TikTok usage."""
        stats_dict = {
            'total_days': len(self.df['timestamp'].dt.date.unique()),
            'total_activities': self.df['total_activity'].sum(),
            'avg_daily_activities': self.df.groupby(self.df['timestamp'].dt.date)['total_activity'].sum().mean(),
            'peak_activity_hour': self.df.groupby(self.df['timestamp'].dt.hour)['total_activity'].mean().idxmax(),
            'weekend_vs_weekday': {
                'weekend_avg': self.df[self.df['is_weekend']]['total_activity'].mean(),
                'weekday_avg': self.df[~self.df['is_weekend']]['total_activity'].mean()
            }
        }
        return stats_dict
    
    def analyze_weather_correlation(self):
        """Analyze correlation between weather conditions and TikTok activity."""
        weather_correlations = {
            'temperature': stats.pearsonr(self.df['temperature'], self.df['total_activity']),
            'precipitation': stats.pearsonr(self.df['precipitation'], self.df['total_activity'])
        }
        
        # Average activity by weather description
        weather_activity = (self.df.groupby('weather_description')
                          .agg({
                              'total_activity': 'mean',
                              'timestamp': 'count'
                          })
                          .rename(columns={'timestamp': 'occurrence_count'})
                          .sort_values('total_activity', ascending=False))
        
        return {
            'correlations': weather_correlations,
            'activity_by_weather': weather_activity
        }
    
    def get_hourly_patterns(self):
        """Analyze hourly patterns in TikTok usage."""
        return (self.df.groupby('hour')['total_activity']
                .agg(['mean', 'count', 'sum'])
                .round(2))

def main():
    analyzer = TikTokWeatherAnalyzer()
    
    # Calculate and save basic stats
    basic_stats = analyzer.calculate_basic_stats()
    weather_analysis = analyzer.analyze_weather_correlation()
    hourly_patterns = analyzer.get_hourly_patterns()
    
    # Create output directory if it doesn't exist
    output_dir = 'data/analysis_results'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save results
    with open(f"{output_dir}/analysis_summary.txt", 'w') as f:
        f.write("=== TikTok Weather Analysis Results ===\n\n")
        
        f.write("Basic Statistics:\n")
        for key, value in basic_stats.items():
            f.write(f"{key}: {value}\n")
        
        f.write("\nWeather Correlations:\n")
        for weather_type, (corr, p_value) in weather_analysis['correlations'].items():
            f.write(f"{weather_type}: correlation={corr:.3f}, p-value={p_value:.3f}\n")
    
    # Save detailed results as CSV
    weather_analysis['activity_by_weather'].to_csv(f"{output_dir}/weather_activity_patterns.csv")
    hourly_patterns.to_csv(f"{output_dir}/hourly_patterns.csv")

if __name__ == "__main__":
    main() 