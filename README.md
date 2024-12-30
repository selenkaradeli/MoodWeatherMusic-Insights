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

Historical weather data for my location has been obtained using the [OpenWeatherMap API](https://openweathermap.org/api). The data includes:

- **Date**
- **Average Temperature (°C)**
- **Weather Condition** (such as, Clear, Rain, Clouds)
- **Hourly Weather Conditions**: Detailed weather information for each hour of the day.

*Weather data is fetched and stored in the `weather_data` directory.*

## Data Processing Steps

### 1. TikTok Data Parsing

1. **Organize Data**: Place all exported `.txt` TikTok data files into the `tiktok_data` folder.
2. **Parse `.txt` Files**: Use the `parse_tiktok_data.py` script to convert `.txt` files into structured CSV files.
    ```bash
    python scripts/parse_tiktok_data.py
    ```
3. **Clean Data**: Remove any entries with missing or incomplete information to ensure data quality.

### 2. Weather Data Collection

1. **API Setup**: Sign up for an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. **Fetch Data**: Use the `fetch_weather_data.py` script to retrieve historical weather data.
    ```bash
    python scripts/fetch_weather_data.py
    ```
3. **Process Data**: Convert the fetched JSON data into a structured CSV format for analysis.

### 3. Data Integration (Will be implemented)

1. **Merge Datasets**: Use the `merge_data.py` script to combine TikTok usage data with corresponding weather data based on the date and hour.
    ```bash
    python scripts/merge_data.py
    ```
2. **Finalize Dataset**: The merged and cleaned data is saved as `processed_data.csv` in the `data` directory.

## Analysis & Visualization

Using the `analysis.ipynb` Jupyter notebook, perform the following analyses:

- **Correlation Analysis**: Explore the relationship between weather conditions (average temperature, weather type) and TikTok usage metrics.
- **Time Series Analysis**: Track daily and hourly TikTok activity alongside weather changes over time.
- **Content Preference**: Identify which types of videos or sounds are favored under different weather conditions.
- **Peak Usage Times**: Analyze login history to determine peak times of TikTok activity and their correlation with weather.

*My visualizations will possibly include (may differ) scatter plots, bar charts, line graphs, and heatmaps to illustrate the findings.*

## Findings

*This section will be implemented with insights and results derived from the data analysis.*

## Future Work

*This section will be implemented later.*

## Project Structure

```
tiktok-weather-analysis/
├── README.md                   # Project documentation and overview
├── data/
│   ├── processed/             # Cleaned and merged datasets
│   │   └── processed_data.csv
│   ├── tiktok_data/          # Raw TikTok export data
│   │   ├── browsing_history.txt
│   │   ├── favorite_sounds.txt
│   │   ├── favorite_videos.txt
│   │   ├── like_list.txt
│   │   ├── share_history.txt
│   │   └── login_history.txt
│   └── weather_data/         # Weather API data
│       ├── hourly_weather.csv
│       └── daily_weather.csv
├── notebooks/
│   └── DataPreprocessing.ipynb # Data cleaning and preparation notebook
├── scripts/
│   ├── parse_tiktok_data.py   # Script to process TikTok data
│   ├── fetch_weather_data.py  # Script to fetch weather data
│   └── merge_data.py          # Script to combine datasets
├── requirements.txt           # Project dependencies
└── .env                      # Environment variables (API keys)
```

## Installation and Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/selenkaradeli/dsa210-tiktok-weather-analysis.git
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd dsa210-tiktok-weather-analysis
    ```

3. **Install Required Python Libraries**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Key (if you want to fetch weather data)**
    - Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
    - Create a `.env` file in the root directory and add API key:
        ```
        OPENWEATHER_API_KEY=api_key
        ```

5. **Run the Data Parsing and Fetching Scripts**
    ```bash
    python scripts/parse_tiktok_data.py
    python scripts/fetch_weather_data.py
    python scripts/merge_data.py
    ```

6. **Open the Analysis Notebook**
    ```bash
    jupyter notebook notebooks/analysis.ipynb
    ```

*`.gitignore`:*

```
.env
```

## Dependencies

List of Python libraries required for the project:

- pandas
- matplotlib
- seaborn
- lxml
- scipy
- requests
- python-dotenv

*These are listed in `requirements.txt` for easy installation.*

## Conclusion

*This section will be implemented at the end of the project.*

---

*This README.md file is a work in progress and will be updated as the project progresses.*
