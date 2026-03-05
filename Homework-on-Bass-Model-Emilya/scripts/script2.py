# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import bass_model

# Loading the dataset
file_path = 'data/statistic_id1399076_volume-of-thedrone-market-worldwide-2018-2030.xlsx'
df = pd.read_excel(file_path, sheet_name='Data', header=None, skiprows=5)

# Selecting the columns containing year and market volume
df = df[[1, 2]]
df.columns = ['Year', 'Volume']

# Converting the volume column to numeric values and removing missing data
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
df = df.dropna()

# Creating time periods and extracting observed volume values
t_data = np.arange(1, len(df) + 1)
N_data = df['Volume'].values

# Defining Bass model parameters for the forecast
p, q, M = 0.012, 0.18, 12_000_000

# Generating predicted adopters using the Bass model
N_pred = bass_model(t_data, p, q, M)

# Calculating cumulative adoption over time
cumulative_N = np.cumsum(N_pred)

# Creating the forecast plot
plt.figure(figsize=(10,6))

# Plotting predicted annual adopters as bars
plt.bar(t_data, N_pred, color='orange', alpha=0.7, label='Predicted Annual Adopters')

# Plotting cumulative adopters as a line
plt.plot(t_data, cumulative_N, color='blue', marker='o', label='Cumulative Adopters')

# Adding labels and title to the plot
plt.xlabel('Years from 2018')
plt.ylabel('Units (in millions)')
plt.title('Predicted Adoption Path of Antigravity A1 Drone')

# Adding legend and grid for better readability
plt.legend()
plt.grid(True)

# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig('img/image2.png', dpi=300)

# Displaying the plot
plt.show()

# Creating a table with historical and predicted values
forecast_table = pd.DataFrame({
    'Year': df['Year'].values,
    'Historical_Volume': N_data,
    'Bass_Predicted': N_pred.round(2),
    'Cumulative_Predicted': cumulative_N.round(2)
})

# Saving the forecast table to a CSV file
forecast_table.to_csv('data/antigravityA1_forecast.csv', index=False)

print("Forecast table saved to data/antigravityA1_forecast.csv")