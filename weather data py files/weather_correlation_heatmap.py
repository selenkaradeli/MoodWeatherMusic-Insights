#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 18:54:16 2024

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

# Correlation Heatmap - Weather Variables
weather_vars = ['Temperature Maximum', 'Temperature Minimum', 'Precipitation Total', 'Temperature Average']
available_vars = [var for var in weather_vars if var in df.columns]
if len(available_vars) > 1:
    corr_matrix = df[available_vars].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="viridis", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()