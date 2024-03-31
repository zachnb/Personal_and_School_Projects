# -*- coding: utf-8 -*-
"""data_exploration

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X6OmJLe-YRIjOuaKyDc4SPTYcYhLnmKe
"""

"""
    File name: data_exploration.py
    Author: Zachary Brown
    Python Version 3.10.12
    Description: Reading and manipulating data from a csv 
    file using the pandas framework.
"""

import pandas as pd

"""Part I"""

# Read the data into a variable called data
data = pd.read_csv('6153237444115dat.csv', na_values=['*', '**', '***', '****',
                                                      '*****', '******'])

# Count the number of rows in the data
num_rows = len(data)
print("Number of rows in the data:", num_rows)

# Convert the data to a list and display the column names
column_names = ', '.join(data.columns.tolist())
print("Column names:", column_names)

# Display data types of the columns
datatypes = data.dtypes
print("Datatypes of the columns:")
print(datatypes)

# Calculate the mean temperature in Fahrenheit
mean_temp_fahrenheit = data['TEMP'].mean()
print("Mean Fahrenheit temperature:", mean_temp_fahrenheit)

# Calculate the standard deviation
std_dev_max_temp = data['MAX'].std()
print("Standard deviation of Maximum temperature:", std_dev_max_temp)

# Count the number of unqiue stations in the data
num_unique_stations = data['USAF'].nunique()
print("Number of unique stations:", num_unique_stations)

"""Part II"""

# Select columns and assign them into a new variable
selected = data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

# Remove all rows from selected that have NoData
selected = selected.dropna(subset=['TEMP'])

# Convert Fahrenheit temperatures into Celsius
selected['TEMP_Celsius'] = (selected['TEMP'] - 32) / 1.8
selected['MAX_Celsius'] = (selected['MAX'] - 32) / 1.8
selected['MIN_Celsius'] = (selected['MIN'] - 32) / 1.8

# Round the values in Celsius to have 1 decimal place
selected = selected.round({'TEMP_Celsius': 1, 'MAX_Celsius': 1, 'MIN_Celsius': 1})

# Save the updated data to a new CSV file
selected.to_csv('updated_data.csv', index=False)

# Display the updated data
print("Updated data with Fahrenheit temperatures converted to Celsius and rounded to 1 decimal place:")
print(selected)

"""Part III"""

# Divide the selection into separate datasets for different stations
kumpula = selected[selected['USAF'] == 29980]
rovaniemi = selected[selected['USAF'] == 28450]

# Save kumpula DataFrame into Kumpula_temps_May_Aug_2017.csv file (CSV format)
kumpula.to_csv('Kumpula_temps_May_Aug_2017.csv', index=False, float_format='%.1f', sep=',')

# Save rovaniemi DataFrame into Rovaniemi_temps_May_Aug_2017.csv file (CSV format)
rovaniemi.to_csv('Rovaniemi_temps_May_Aug_2017.csv', index=False, float_format='%.1f', sep=',')

# Display a message confirming the completion of the task
print("DataFrames saved successfully.")


"""Part IV (a)"""

# Load the data from the saved CSV files
kumpula = pd.read_csv('Kumpula_temps_May_Aug_2017.csv')
rovaniemi = pd.read_csv('Rovaniemi_temps_May_Aug_2017.csv')

# Calculate the median temperature in Celsius for each location
median_temp_kumpula = kumpula['TEMP'].median()
median_temp_rovaniemi = rovaniemi['TEMP'].median()

# Print the results
print("Median temperature in Celsius for Helsinki (Kumpula):", round(median_temp_kumpula, 1))
print("Median temperature in Celsius for Rovaniemi:", round(median_temp_rovaniemi, 1))

"""Part IV (b)"""

# Convert to datetime format
kumpula['YR--MODAHRMN'] = pd.to_datetime(kumpula['YR--MODAHRMN'], format='%Y%m%d%H%M')
rovaniemi['YR--MODAHRMN'] = pd.to_datetime(rovaniemi['YR--MODAHRMN'], format='%Y%m%d%H%M')

# Select data for May and June
kumpula_may = kumpula[kumpula['YR--MODAHRMN'].dt.month == 5]
rovaniemi_may = rovaniemi[rovaniemi['YR--MODAHRMN'].dt.month == 5]

kumpula_june = kumpula[kumpula['YR--MODAHRMN'].dt.month == 6]
rovaniemi_june = rovaniemi[rovaniemi['YR--MODAHRMN'].dt.month == 6]

# Calculate mean, min, and max temperatures for Kumpula and Rovaniemi in May and June
print("Kumpula Mean, Min, Max temperatures for May:")
print("Mean temperature:", round(kumpula_may['TEMP'].mean(), 1))
print("Minimum temperature:", round(kumpula_may['TEMP'].min(), 1))
print("Maximum temperature:", round(kumpula_may['TEMP'].max(), 1))

print("\nKumpula Mean, Min, Max temperatures for June:")
print("Mean temperature:", round(kumpula_june['TEMP'].mean(), 1))
print("Minimum temperature:", round(kumpula_june['TEMP'].min(), 1))
print("Maximum temperature:", round(kumpula_june['TEMP'].max(), 1))

print("\nRovaniemi Mean, Min, Max temperatures for May:")
print("Mean temperature:", round(rovaniemi_may['TEMP'].mean(), 1))
print("Minimum temperature:", round(rovaniemi_may['TEMP'].min(), 1))
print("Maximum temperature:", round(rovaniemi_may['TEMP'].max(), 1))

print("\nRovaniemi Mean, Min, Max temperatures for June:")
print("Mean temperature:", round(rovaniemi_june['TEMP'].mean(), 1))
print("Minimum temperature:", round(rovaniemi_june['TEMP'].min(), 1))
print("Maximum temperature:", round(rovaniemi_june['TEMP'].max(), 1))

from google.colab import drive
drive.mount('/content/drive')