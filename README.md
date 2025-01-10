# TikTok Usage and Weather Relation Analysis

## Overview

This project investigates the relationship between my personal TikTok usage and weather conditions. By analyzing data such as browsing history, favorite sounds, liked videos, shares, and login times alongside daily and hourly weather information, the goal is to uncover patterns and insights about how weather influence my TikTok habits.

Using my personal TikTok data and matching it with weather data from those same times, I'm trying to uncover if there are any interesting patterns. Such as, do I watch more videos when it's rainy?

## Motivation

The idea hit me during midterms when I was supposed to be studying but instead found myself deep in TikTok's algorithm (we've all been there 😅). I noticed I'd spent way more time on the app during that week of terrible weather, which got me thinking - does the weather actually influence how much time I spend on TikTok?

As a student diving into data science, I thought this would be a fun way to finally understand why I sometimes spend hours on TikTok (and blame it on the weather 😉)

## Data Sources

### TikTok Data

I have exported the following data from my TikTok account in `.txt` format and organized them into the `tiktok_data` folder:

- **Browsing History**: What I've browsed.
- **Favorite Sounds**: List of sounds I've favorited.
- **Favorite Videos**: Videos I have marked as favorites.
- **Like List**: Videos I have liked.
- **Share History**: Videos I have shared with friends.
- **Login History**: Timestamps of when I logged into TikTok.

*All TikTok data files are stored locally in the `tiktok_data` directory.*

### Weather Data
- Historical weather data from Open-Meteo API
- Hourly data including:
  - Temperature
  - Precipitation
  - Weather conditions (clear, cloudy, rain, etc.)
  - Weather codes for detailed classification

*Weather data is fetched and stored in the `weather_data` directory.*

## Analysis Process

1. **Data Collection**
   - Export personal TikTok data
   - Fetch historical weather data using Open-Meteo API
   - Process and clean raw data files

2. **Data Processing**
   - Merge TikTok activity with weather conditions
   - Calculate hourly and daily activity metrics
   - Map weather codes to readable descriptions

3. **Analysis**
   - Calculate basic usage statistics
   - Analyze weather correlations
   - Identify patterns in usage based on:
     - Weather conditions
     - Temperature ranges
     - Time of day
     - Day of week

## Key Findings

Based on the analysis results:

- Peak TikTok activity occurs at 22:00 (10 PM)
- Slight positive correlation with temperature (0.058)
- Negative correlation with precipitation (-0.063)
- Weather impact on usage:
  - Highest activity during clear sky conditions (22.37 actions/hour)
  - Reduced activity during rain (13.46 actions/hour)
  - Lowest activity during heavy rain/showers (4.9-5.0 actions/hour)
- Weekend vs. Weekday:
  - Weekend average: 20.49 actions/hour
  - Weekday average: 19.67 actions/hour

## Visualizations

The project generates several visualizations:

- Correlation heatmaps
- Activity distribution plots
- Weather-activity relationships
- Hourly usage patterns
- Temperature vs. activity scatter plots
- Monthly activity trends

All visualizations are saved in the `visualizations/` directory.

## Project Structure

```
tiktok-weather-analysis/
├── README.md                   # Project documentation
├── data/
│   ├── processed/             # Cleaned datasets
│   ├── tiktok_data/          # Raw TikTok export
│   ├── weather_data/         # Weather API data
│   ├── merged_data/          # Combined datasets
│   └── analysis_results/     # Analysis outputs
├── scripts/
│   ├── analyze_data.py       # Analysis functions
│   ├── fetch_weather_data.py # Weather API interface
│   ├── merge_data.py         # Data combination
│   └── visualize_data.py     # Visualization generation
├── visualizations/           # Generated plots
├── DSA210_Selen.pdf          # Project report
└── requirements.txt          # Dependencies

```

## Setup and Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the analysis:
```bash
python scripts/parse_tiktok_data.py
python scripts/fetch_weather_data.py
python scripts/merge_data.py
python scripts/analyze_data.py
python scripts/visualize_data.py
```

## Dependencies

- pandas (≥1.3.0)
- matplotlib (≥3.4.0)
- seaborn (≥0.11.0)
- numpy (≥1.21.0)
- scipy (≥1.7.0)
- requests (≥2.26.0)
- python-dotenv (≥0.19.0)
- jupyter (≥1.0.0)

## Conclusion

The analysis of my TikTok usage patterns in relation to weather conditions has revealed several interesting insights:

### Weather Impact
- **Clear Weather**: Shows the highest engagement (22.37 actions/hour), suggesting I'm more likely to actively interact with content during good weather
- **Rainy Conditions**: Activity drops significantly (13.46 actions/hour), possibly indicating more passive consumption
- **Heavy Rain**: Surprisingly shows the lowest activity (4.9-5.0 actions/hour), contrary to the initial hypothesis that bad weather would increase usage

### Temporal Patterns
- **Daily Peaks**: Strongest activity around 22:00 (10 PM), suggesting a consistent nighttime usage pattern
- **Weekend Effect**: Slightly higher average activity on weekends (20.49 vs 19.67 actions/hour)
- **Monthly Trends**: [Add specific monthly patterns you discovered]

### Activity Types
- **Browsing vs. Interaction**: [Add ratio or comparison of passive browsing vs. active interaction]
- **Engagement Patterns**: [Add patterns about likes, shares, and other interactions]
- **Login Frequency**: [Add insights about login patterns]

### Temperature Correlation
- Weak positive correlation with temperature (0.058)
- This suggests that while temperature does influence usage, the effect is subtle
- The relationship appears non-linear, with moderate temperatures showing different patterns than extremes

### Precipitation Effects
- Negative correlation with precipitation (-0.063)
- The impact varies by precipitation intensity
- Short-term rain shows different patterns compared to extended periods of precipitation

### Key Takeaways
1. Weather conditions do influence TikTok usage, but the relationship is more complex than initially hypothesized
2. Time of day and weekly patterns appear to be stronger determinants of usage than weather
3. The combination of multiple weather factors provides better insight than any single weather condition
4. Usage patterns suggest a balance between active engagement and passive consumption, varying with weather conditions

These findings not only provide insights into personal social media habits but also suggest potential applications for content delivery optimization and user engagement strategies. The analysis demonstrates that environmental factors play a subtle but measurable role in social media usage patterns, though the relationships are nuanced and likely interplay with various other behavioral and social factors.

---

*This README.md file is a work in progress and will be updated as the project progresses.*
