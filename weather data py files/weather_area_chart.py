#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:18:01 2024

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


# Area Chart - Cumulative Rainfall
if 'Precipitation Total' in df.columns:
    df['Cumulative Rainfall'] = df['Precipitation Total'].cumsum()
    plt.figure(figsize=(12, 6))
    plt.fill_between(df.index, df['Cumulative Rainfall'], color='pink', alpha=1)
    plt.title("Cumulative Rainfall Over the Year")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Rainfall (mm)")
    plt.tight_layout()
    plt.show()
