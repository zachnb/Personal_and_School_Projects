# -*- coding: utf-8 -*-
"""gdp_comparison.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zlH4b7kRu5gYveeXithAqOJVju58PhmZ
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
data = pd.read_csv('/content/sample_data/gapminder_gdp_asia.csv', index_col='country')

# Extract the year from the column names. We want to strip the gdppercap_ text
# for better clarity on the plot. The strip method only works on strings,
# so we must do this before converting the years to integers.
years = data.columns.str.strip('gdpPercap_')

# Convert the year values to integers, since they represent numerical values.
data.columns = years.astype(int)

# Plot the GDP of China and India from 1952 to 2007. We transpose the data
# in order to plot multiple lines of data
data.loc[['China', 'India'], :].T.plot()

# Label the axes
plt.xlabel('Year')
plt.ylabel('GDP per capita')

# Add a title
plt.title('GDP Comparison of China and India (1952-2007)')

# Add a legend
plt.legend(loc='lower right')

# Show the plot
plt.show()

# Load the data from the CSV file into a DataFrame.
data_all = pd.read_csv('/content/sample_data/gapminder_all.csv', index_col='country')

# Plot the correlation between GDP and life expectancy for 2007.
data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
              s=data_all['pop_2007']/1e6)

# Set title for the plot.
plt.title('Correlation between GDP and Life Expectancy in 2007')

# Set x and y axis labels.
plt.xlabel('GDP per Capita (2007)')
plt.ylabel('Life Expectancy (2007)')

# Show the plot.
plt.show()
