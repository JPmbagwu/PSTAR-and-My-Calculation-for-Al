#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:22:22 2024

@author: johnpaulmbagwu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
M0_c = 938.272  # MeV/c^2 (rest mass of proton)
z = 1  # Charge of proton

# Function to calculate the beta value
def beta(T):
    b = (1 - (1 / ((T/M0_c) + 1))**2)**(1/2)
    return b

# Function to calculate the mass stopping power
def dedx(T, I, Z_A):
    be = beta(T)
    SP = 0.3071 * Z_A * z**2 * (1/be**2) * (13.8373 + np.log(be**2 / (1 - be**2)) - be**2 - np.log(I))
    return SP

# Read the TXT data file containing information about Aluminum Oxide
df = pd.read_csv('Aluminum.txt', delimiter=' ')

# Extract the stopping power and energy columns from the dataframe
stopping_power = df['TotalStp.Pow']
energy = df['KineticEnergy']

# Calculate the stopping power values using the dedx function
SP_values = dedx(energy, 166, 13/26.98)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting both calculated and experimental stopping power
plt.plot(energy, stopping_power, label='My Calculation')
plt.plot(energy, SP_values, label='PSTAR Data', linestyle='--')

plt.title('Aluminum')
plt.xlabel('Energy (MeV)')
plt.ylabel('Stopping Power (MeV/(g/cm^2))')

# Set the x and y-axis scales to logarithmic for better visualization
plt.xscale('log')
plt.yscale('log')

# Set the x-axis and y-axis limits for better visibility of data points
plt.xlim(1e-2, 1e4)

plt.grid(True)
plt.legend()

plt.show()
