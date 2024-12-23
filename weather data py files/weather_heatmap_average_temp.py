#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:36:05 2024

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
# Heatmap - Monthly Average Temperatures
if 'Temperature Maximum' in df.columns and 'Temperature Minimum' in df.columns:
    df['Month'] = df.index.month
    monthly_avg_temp = df.groupby('Month')[['Temperature Maximum', 'Temperature Minimum']].mean()
    plt.figure(figsize=(8, 6))
    sns.heatmap(monthly_avg_temp, annot=True, cmap="coolwarm", fmt=".1f")
    plt.title("Monthly Average Temperatures")
    plt.xlabel("Temperature Type")
    plt.ylabel("Month")
    plt.tight_layout()
    plt.show()
