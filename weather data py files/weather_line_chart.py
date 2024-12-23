#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:32:59 2024

@author: selenkaradeli
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np

file_path = "/Users/selenkaradeli/Desktop/weather_data_2024 .txt"

import os
if not os.path.exists(file_path):
    raise FileNotFoundError("File not found. Verify the file path.")

df = pd.read_csv(file_path, sep="\t", encoding="utf-8")

df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d.%m.%Y', errors="coerce")

df = df.dropna(subset=['timestamp'])

# Strip whitespace from column names
df.columns = df.columns.str.strip()

numeric_columns = ['Temperature Maximum', 'Temperature Minimum', 'Precipitation Total', 'Temperature Average']
existing_numeric_columns = [col for col in numeric_columns if col in df.columns]  # Keep only existing columns

for col in existing_numeric_columns:# Convert columns to numeric
    df[col] = pd.to_numeric(df[col], errors='coerce') 

df = df.dropna(subset=existing_numeric_columns)

# Timestamp - easier plotting
df.set_index('timestamp', inplace=True)

# Line Chart - Daily Maximum and Minimum Temperatures
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Temperature Maximum'], label='Max Temperature', color='blue')
plt.plot(df.index, df['Temperature Minimum'], label='Min Temperature', color='orange')
locator = MonthLocator()
formatter = DateFormatter("%b")
plt.yticks(range(-10, 41, 4))
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(formatter)
plt.xticks(rotation=45)
plt.grid(visible=True, linestyle="--", alpha=1)
plt.title("Daily Maximum and Minimum Temperatures")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.tight_layout()
plt.show()
