# MoodWeatherMusic-Insights

## **Project Overview**
This project aims to explore how daily weather conditions influence mood and music preferences. By combining weather data, self-reported mood records, and Spotify music data, I plan to uncover meaningful patterns and insights. This project will involve all stages, including data collection, cleaning, analysis, and visualization.


## **Objective**
The primary objectives of this project are:
1. To analyze the impact of weather on mood.
2. To investigate the relationship between mood and music preferences.
3. To combine insights from both analyses to understand how weather, mood, and music interact.


## **Plan**
### **1. Data Collection**
I will gather data from the following sources:
- **Weather Data:** Daily weather conditions for Istanbul in 2024, sourced from [Weather and Climate](https://weather-and-climate.com/).
- **Mood Data:** Self-reported mood ratings logged daily into an Excel file.
- **Spotify Data:** User-specific music data such as recently played tracks and top genres, fetched using the Spotify Web API.

### **2. Data Cleaning and Preparation**
- Handle missing or inconsistent entries.
- Format data into a unified structure for analysis.

### **3. Exploratory Data Analysis (EDA)**
- Use visualization techniques like scatter plots, bar charts, and correlation heatmaps to identify trends and relationships.

### **4. Insights and Findings**
- Analyze how weather conditions (e.g., sunny, rainy) correlate with mood and music preferences.


## **Technologies to Be Used**
- **Programming Language:** Python
- **Libraries:**
  - `Pandas`, `NumPy`: For data processing.
  - `Matplotlib`, `Seaborn`: For creating visualizations.
  - `Spotipy`: For accessing Spotify data via its Web API.


## **Questions to Address**
1. How do different weather conditions (e.g., rainy, sunny) influence mood?
2. Which music genres are most frequently associated with specific moods?
3. Are there patterns that link weather and music preferences?


## **Expected Results**
I expect to observe:
- **Rainy Days → Sad moods → Acoustic or calming music.**
- **Sunny Days → Happy moods → Energetic or pop music.**
- **Stressful Days → Relaxing playlists or instrumental music.**


## **Limitations**
- **Subjectivity of Mood Data:** Mood data will be self-reported, which may introduce bias.
- **Spotify API Constraints:** The API only allows access to data from the authenticated user's account.
- **Weather Data Granularity:** Weather data will be limited to daily averages rather than hourly details.


## **Future Work**
If time permits or in future iterations:
1. Automate mood tracking using sentiment analysis on text data (e.g., diary entries).
2. Include additional weather parameters like wind speed and humidity.
3. Develop a predictive model that recommends music based on real-time weather and mood inputs.


## **Acknowledgements**
This project relies on:
- [Spotify API](https://developer.spotify.com/) for accessing user-specific music data.
- [Weather and Climate](https://weather-and-climate.com/) for weather data resources.


## **Deliverables**
Upon completion, this project will include:
1. A well-documented GitHub repository with all scripts, datasets, and results.
2. Visualizations that highlight key insights.
3. A summary report detailing findings and future recommendations.
