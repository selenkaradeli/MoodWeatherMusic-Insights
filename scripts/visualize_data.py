import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from calendar import month_name

class TikTokWeatherVisualizer:
    def __init__(self, data_path='data/merged_data/merged_data.csv'):
        self.df = pd.read_csv(data_path)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df['month'] = self.df['timestamp'].dt.month
        self.df['month_name'] = self.df['timestamp'].dt.month.map(lambda x: month_name[x])
        self.output_dir = 'visualizations'
        os.makedirs(self.output_dir, exist_ok=True)
        
        plt.style.use('default')
        sns.set_theme()
    
    def plot_correlation_heatmap(self):
        """Create a heatmap of correlations between activities and weather conditions."""
        # Select activity columns
        activity_cols = [col for col in self.df.columns if col.endswith('_count')]
        
        # Select weather-related columns
        weather_cols = ['temperature', 'precipitation', 'weather_code', 'is_weekend', 'hour']
        
        # Calculate correlation matrix between activities and weather
        correlation_matrix = pd.DataFrame(
            np.corrcoef(
                self.df[activity_cols].T,
                self.df[weather_cols].T
            )[:len(activity_cols), len(activity_cols):],
            index=[col.replace('_count', '').replace('_', ' ').title() for col in activity_cols],
            columns=[col.replace('_', ' ').title() for col in weather_cols]
        )
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Create heatmap
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap='cool',
            center=0,
            fmt='.2f',
            ax=ax,
            vmin=-1,
            vmax=1,
            cbar_kws={'label': 'Correlation Coefficient'}
        )
        
        # Customize the plot
        ax.set_title('Correlation between Activities and Weather Conditions')
        
        # Rotate labels for better readability
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        
        # Save the plot
        plt.savefig(
            f"{self.output_dir}/correlation_heatmap.png",
            dpi=300,
            bbox_inches='tight'
        )
        plt.close(fig)

    def plot_activity_distributions(self):
        """Create distribution plots for different types of activities, split into two groups."""
        activity_cols = [col for col in self.df.columns if col.endswith('_count')]
        colors = plt.cm.cool(np.linspace(0, 1, len(activity_cols)))
        
        # Split activities into two groups
        first_group = activity_cols[:3]
        second_group = activity_cols[3:]
        
        # First group of distributions
        fig1, axes1 = plt.subplots(3, 1, figsize=(12, 12))
        for i, col in enumerate(first_group):
            sns.histplot(data=self.df, x=col, ax=axes1[i], kde=True, color=colors[i])
            axes1[i].set_title(f'Distribution of {col.replace("_count", "").replace("_", " ").title()}')
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/activity_distributions_1.png", dpi=300, bbox_inches='tight')
        plt.close(fig1)
        
        # Second group of distributions
        fig2, axes2 = plt.subplots(3, 1, figsize=(12, 12))
        for i, col in enumerate(second_group):
            sns.histplot(data=self.df, x=col, ax=axes2[i], kde=True, color=colors[i+3])
            axes2[i].set_title(f'Distribution of {col.replace("_count", "").replace("_", " ").title()}')
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/activity_distributions_2.png", dpi=300, bbox_inches='tight')
        plt.close(fig2)

    def plot_monthly_patterns(self):
        """Create a plot showing monthly patterns in activity."""
        monthly_activity = self.df.groupby('month_name')['total_activity'].agg(['mean', 'std'])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_activity['mean'].plot(kind='bar', 
                                    yerr=monthly_activity['std'], 
                                    capsize=5, 
                                    ax=ax, 
                                    color='blueviolet')
        
        ax.set_title('Monthly TikTok Activity Patterns')
        ax.set_xlabel('Month')
        ax.set_ylabel('Average Activity (with std dev)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/monthly_patterns.png", dpi=300, bbox_inches='tight')
        plt.close(fig)

    def plot_weather_activity_boxplot(self):
        """Create boxplots showing activity distribution for each weather condition."""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Get number of weather conditions for color mapping
        n_weather = len(self.df['weather_description'].unique())
        colors = plt.cm.cool(np.linspace(0, 1, n_weather))
        
        sns.boxplot(data=self.df, x='weather_description', y='total_activity', 
                   ax=ax, palette=colors)
        
        plt.xticks(rotation=45, ha='right')
        ax.set_title('Activity Distribution by Weather Condition')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/weather_activity_boxplot.png", dpi=300, bbox_inches='tight')
        plt.close(fig)

    def plot_hourly_heatmap(self):
        """Create a heatmap showing activity patterns by hour and day of week."""
        pivot_table = pd.pivot_table(self.df, 
                                   values='total_activity',
                                   index='hour',
                                   columns='day_of_week',
                                   aggfunc='mean')
        
        # Reorder columns for correct day order
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                     'Friday', 'Saturday', 'Sunday']
        pivot_table = pivot_table[days_order]
        
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(pivot_table, 
                   cmap='cool',
                   annot=True, 
                   fmt='.1f', 
                   ax=ax)
        ax.set_title('Average Activity by Hour and Day of Week')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/hourly_heatmap.png", dpi=300, bbox_inches='tight')
        plt.close(fig)

    def plot_temperature_activity_hexbin(self):
        """Create a hexbin plot of temperature vs activity."""
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.hexbin(self.df['temperature'], self.df['total_activity'], 
                  gridsize=20, cmap='cool')
        plt.colorbar(label='Count')
        ax.set_title('Temperature vs Activity Density')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Activity Count')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/temperature_activity_hexbin.png", dpi=300, bbox_inches='tight')
        plt.close(fig)

    def plot_activity_type_comparison(self):
        """Create a comparison of different activity types."""
        activity_cols = [col for col in self.df.columns if col.endswith('_count')]
        activity_means = self.df[activity_cols].mean()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = plt.cm.tab20b(np.linspace(0, 1, len(activity_cols)))
        activity_means.plot(kind='pie', autopct='%1.1f%%', colors=colors)
        
        ax.set_title('Distribution of Activity Types')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/activity_type_comparison.png", dpi=300, bbox_inches='tight')
        plt.close(fig)

    def plot_activity_by_weather(self):
        """Create a bar plot of average activity by weather condition."""
        fig, ax = plt.subplots(figsize=(12, 6))
        weather_activity = (self.df.groupby('weather_description')['total_activity']
                          .mean()
                          .sort_values(ascending=True))
        
        weather_activity.plot(kind='barh', color='blueviolet', ax=ax)
        ax.set_title('Average TikTok Activity by Weather Condition')
        ax.set_xlabel('Average Activity')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/activity_by_weather.png", dpi=300, bbox_inches='tight')
        plt.close(fig)
    
    def plot_temperature_correlation(self):
        """Create a scatter plot of temperature vs activity."""
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='temperature', y='total_activity', alpha=0.5, ax=ax)
        sns.regplot(data=self.df, x='temperature', y='total_activity', 
                   scatter=False, color='red', ax=ax)
        ax.set_title('TikTok Activity vs Temperature')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Activity Count')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/temperature_correlation.png", dpi=300, bbox_inches='tight')
        plt.close(fig)
    
    def plot_hourly_patterns(self):
        """Create a line plot of average activity by hour."""
        fig, ax = plt.subplots(figsize=(12, 6))
        hourly_avg = self.df.groupby('hour')['total_activity'].mean()
        
        plt.plot(hourly_avg.index, hourly_avg.values, 
                color=plt.cm.cool(0.6),
                linewidth=2, 
                marker='o')
        
        ax.set_title('Average TikTok Activity Throughout the Day')
        ax.set_xlabel('Hour of Day')
        ax.set_ylabel('Average Activity')
        ax.set_xticks(range(0, 24))
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/hourly_patterns.png", dpi=300, bbox_inches='tight')
        plt.close(fig)
    
    def plot_weekly_patterns(self):
        """Create a bar plot of average activity by day of week."""
        fig, ax = plt.subplots(figsize=(12, 6))
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekly_avg = (self.df.groupby('day_of_week')['total_activity']
                     .mean()
                     .reindex(days_order))
        
        weekly_avg.plot(kind='bar', ax=ax, color='blueviolet')
        ax.set_title('Average TikTok Activity by Day of Week')
        ax.set_xlabel('Day of Week')
        ax.set_ylabel('Average Activity')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/weekly_patterns.png", dpi=300, bbox_inches='tight')
        plt.close(fig)
    
    def plot_weather_activity_heatmaps(self):
        """Create detailed heatmaps for weather conditions vs different activities."""
        activity_cols = [col for col in self.df.columns if col.endswith('_count')]
        
        for activity_col in activity_cols:
            pivot_data = pd.pivot_table(
                self.df,
                values=activity_col,
                index='hour',
                columns='weather_description',
                aggfunc='mean'
            )
            
            fig, ax = plt.subplots(figsize=(15, 8))
            sns.heatmap(
                pivot_data,
                cmap='cool',
                annot=True,
                fmt='.1f',
                ax=ax,
                cbar_kws={'label': 'Average Activity Count'}
            )
            
            activity_name = activity_col.replace('_count', '').replace('_', ' ').title()
            ax.set_title(f'{activity_name} by Hour and Weather Condition')
            ax.set_xlabel('Weather Condition')
            ax.set_ylabel('Hour of Day')
            
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f"{self.output_dir}/heatmap_{activity_col}.png", dpi=300, bbox_inches='tight')
            plt.close(fig)

    def plot_activity_correlation_heatmap(self):
        """Create a heatmap showing correlations between different types of activities."""
        # Get all activity columns
        activity_cols = [col for col in self.df.columns if col.endswith('_count')]
        
        # Calculate correlation matrix for activities
        correlation_matrix = self.df[activity_cols].corr()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create heatmap
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap='coolwarm',
            center=0,
            fmt='.2f',
            ax=ax,
            square=True
        )
        
        # Customize the plot
        ax.set_title('Correlation Between Different Types of Activities')
        
        # Rotate labels for better readability
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        
        # Save the plot
        plt.savefig(
            f"{self.output_dir}/activity_correlation_heatmap.png",
            dpi=300,
            bbox_inches='tight'
        )
        plt.close(fig)

    def plot_weather_activity_time_heatmap(self):
        """Create a heatmap showing activity patterns across weather conditions and time."""
        # Create pivot table for total activity
        pivot_data = pd.pivot_table(
            self.df,
            values='total_activity',
            index=[self.df['timestamp'].dt.date, 'weather_description'],
            aggfunc='sum'
        ).reset_index()
        
        # Create a matrix form of the data
        matrix_data = pivot_data.pivot(
            index='timestamp',
            columns='weather_description',
            values='total_activity'
        )
        
        # Create figure
        fig, ax = plt.subplots(figsize=(15, 10))
        
        # Create heatmap
        sns.heatmap(
            matrix_data,
            cmap='cool',
            ax=ax,
            cbar_kws={'label': 'Total Activity Count'}
        )
        
        # Customize the plot
        ax.set_title('Activity Patterns Across Weather Conditions Over Time')
        ax.set_xlabel('Weather Condition')
        ax.set_ylabel('Date')
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save the plot
        plt.savefig(
            f"{self.output_dir}/weather_activity_time_heatmap.png",
            dpi=300,
            bbox_inches='tight'
        )
        plt.close(fig)

    def create_all_visualizations(self):
        """Generate all visualizations."""
        print("Generating visualizations...")
        
        visualization_methods = [
            self.plot_correlation_heatmap,
            self.plot_activity_distributions,
            self.plot_monthly_patterns,
            self.plot_weather_activity_boxplot,
            self.plot_hourly_heatmap,
            self.plot_temperature_activity_hexbin,
            self.plot_activity_type_comparison,
            self.plot_activity_by_weather,
            self.plot_temperature_correlation,
            self.plot_hourly_patterns,
            self.plot_weekly_patterns,
            self.plot_weather_activity_heatmaps,
            self.plot_activity_correlation_heatmap,
            self.plot_weather_activity_time_heatmap
        ]
        
        for method in visualization_methods:
            try:
                print(f"- Generating {method.__name__}")
                method()
            except Exception as e:
                print(f"Error in {method.__name__}: {str(e)}")
        
        print(f"All visualizations saved in {self.output_dir}/")

def main():
    visualizer = TikTokWeatherVisualizer()
    visualizer.create_all_visualizations()

if __name__ == "__main__":
    main() 