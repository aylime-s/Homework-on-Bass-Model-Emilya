# Importing required libraries
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from helper_functions import bass_model

# Loading the dataset
file_path = 'data/statistic_id1399076_volume-of-thedrone-market-worldwide-2018-2030.xlsx'
df = pd.read_excel(file_path, sheet_name='Data', header=None, skiprows=5)

# Selecting columns containing year and market volume
df = df[[1,2]]
df.columns = ['Year','Volume']

# Converting volume values to numeric and removing missing data
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
df = df.dropna()

# Printing the cleaned dataset
print("Clean dataset:")
print(df)

# Creating time index and extracting observed values
t_data = np.arange(len(df))
N_data = df['Volume'].values

# Defining the Bass curve used for parameter estimation
def bass_curve(t,p,q,M):
    return bass_model(t,p,q,M,N_data[0])

# Setting initial guesses for Bass parameters
initial_guess = [0.03,0.38,N_data[-1]*2]

# Estimating parameters using nonlinear curve fitting
params,_ = curve_fit(bass_curve,t_data,N_data,p0=initial_guess)

# Extracting estimated parameters
p_est,q_est,M_est = params

# Printing estimated parameters
print("\nEstimated Bass parameters")
print(f"p = {p_est:.4f}")
print(f"q = {q_est:.4f}")
print(f"M = {M_est:.2f}")

# Generating model predictions using estimated parameters
N_pred = bass_model(t_data,p_est,q_est,M_est,N_data[0])

# Creating the historical diffusion plot
plt.figure(figsize=(10,6))

# Plotting observed market data
plt.plot(df['Year'],N_data,'o',label='Observed market volume')

# Plotting Bass model fitted values
plt.plot(df['Year'],N_pred,'-',label='Bass model fit')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Drone market volume (millions)')
plt.title('Historical Drone Market Diffusion')

# Adding legend and grid
plt.legend()
plt.grid(True)

# Saving the plot to the img folder
plt.savefig('img/image1.png')

# Displaying the plot
plt.show()

# Creating a dataframe with estimated parameters
params_df = pd.DataFrame({
    "p":[p_est],
    "q":[q_est],
    "M":[M_est]
})

# Saving estimated parameters to a CSV file
params_df.to_csv("data/bass_parameters.csv",index=False)