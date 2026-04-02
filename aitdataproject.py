# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 14:26:29 2025

@author: aliya
"""
#import libraries 

import pandas as pd # needed for data fram creation
import matplotlib.pyplot as plt #needed for making graphs
import numpy as np # needed for numeric library
import os # needed for OS interface

# display and set working/data directory
os.getcwd()
os.chdir('C:/Users/aliya/OneDrive/Documents/University/AIT/datasets')
os.getcwd()

# uploading the dataset for this project
emission = pd.read_csv("SupplyChainGHGEmissionFactors_v1.3.0_NAICS_CO2e_USD2022.csv")

emission.columns = emission.columns.str.strip() 


petroleum_emission = emission[emission['2017 NAICS Title'].str.contains("petroleum|crude|natural gas|refiner|pipeline|oil and gas|drilling|gasoline", case=False, na=False)]


petroleum_sorted = petroleum_emission.sort_values("Supply Chain Emission Factors without Margins", ascending=False)

petroleum_sorted[['2017 NAICS Title', 
                  'Supply Chain Emission Factors without Margins']].head(15)

plt.figure(figsize=(10,10))
plt.barh(petroleum_sorted['2017 NAICS Title'],
         petroleum_sorted['Supply Chain Emission Factors without Margins'])
plt.xlabel("Carbon dioxide emitted per $1 (without margins)")
plt.title("Greenhouse gas emission per $1 across petroleum-related industries")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

petroleum_mean = petroleum_emission['Supply Chain Emission Factors without Margins'].mean()
other_mean = emission[emission.index.isin(petroleum_emission.index) == False]['Supply Chain Emission Factors without Margins'].mean()

compare = pd.DataFrame({
    'Category': ['Petroleum Industries', 'All Other Industries'],
    'Mean_CO2_per_$1': [petroleum_mean, other_mean]
})
compare

plt.figure(figsize=(6,5))
plt.bar(comparison['Category'], comparison['Mean_CO2_per_$1'])
plt.ylabel("Average CO₂e per $1")
plt.title("Comparison of Emissions per $1: Petroleum vs Other Industries")
plt.show()