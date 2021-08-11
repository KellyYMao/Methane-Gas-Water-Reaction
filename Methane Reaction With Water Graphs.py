#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Imports
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

data_to_load = "Resources/CH4_H2O.csv"

# Creating data frame from csv file
CH4_H2O_data_df = pd.read_csv(data_to_load)
CH4_H2O_data_df


# In[141]:


# Finding the mean water vapor pressure for P_CH4 = 0

# Makes the dataframe only including data from rows where P_CH4 = 0
CH4_H2O_data_df_0 = CH4_H2O_data_df[CH4_H2O_data_df["MFC C Actual (sccm)"] == 0]

# 0-25400.1s + 133510.1s-149560.1s (inclusive) these are the intervals when P_CH4 = 0 

# Finding the water vapor pressure when P_CH4 = 0
# Saturated Water Vapor Calculations
RH_percent = np.array(CH4_H2O_data_df_0["RH%"].tolist())
T = np.array(CH4_H2O_data_df_0["RH sensor temperature (C)"].tolist())
Tc = 647.096
k = np.array(1-(T/Tc))
a1 = -7.85951783
a2 = 1.84408259
a3 = -11.7866497
a4 =  22.6807411
a5 = -15.9618719
a6 = 1.80122502
e = 2.718
Pc = 22.064
saturated_water_pressure = np.array(Pc * (e**((Tc/(T+273))*(a1*k+a2*(k**1.5)+a3*(k**3)+a4*(k**3.5)+a5*(k**4)+a6*(k**7.5)))))

# Graph for Water Vapor Pressure vs. Time for 0-25400.1s
RH_percent = np.array(CH4_H2O_data_df_0["RH%"].tolist())
T = np.array(CH4_H2O_data_df_0["RH sensor temperature (C)"].tolist())
time = np.array(CH4_H2O_data_df_0["Elapsed time (s)"].tolist())
water_vapor_pressure = np.array(RH_percent * (saturated_water_pressure/100))
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "orange")
plt.title("Water vapor pressure change overtime when P_CH4 = 0")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(0, 25400.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=0_version(interval1).png")
plt.show()


# Graph for Water Vapor Pressure vs. Time for 133510.1-149560.1s
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "magenta")
plt.title("Water vapor pressure change overtime when P_CH4 = 0")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(133510.1, 149560.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=0_version(interval2).png")
plt.show()


# In[170]:


# Finding the mean Water Vapor Pressure 

CH4_H2O_data_df_0["water_vapor_pressure"] = water_vapor_pressure
CH4_H2O_data_df_0_improved = CH4_H2O_data_df_0.loc[(CH4_H2O_data_df_0["Elapsed time (s)"] >= 20000) & (CH4_H2O_data_df_0["Elapsed time (s)"] <= 25000)  ] # Just taking data the end of the first interval
# Second interval is during cool down, causing some fluctuations and decrease in pressure so it was ignored 
water_vapor_pressure_values_0 = CH4_H2O_data_df_0_improved["water_vapor_pressure"]
CH4_0_average = water_vapor_pressure_values_0.mean()
CH4_0_std = water_vapor_pressure_values_0.std()
print(CH4_0_average)
print(CH4_0_std)


# In[90]:


# Finding the mean water vapor pressure for P_CH4 = 0.02

CH4_H2O_data_df_4 = CH4_H2O_data_df[CH4_H2O_data_df["MFC C Actual (sccm)"] == 4]

# Makes the dataframe only including data from rows where P_CH4 = 0.02


#PCH_4 = 4 : 25410.1-47000.1s 


# Finding the water vapor pressure when P_CH4 = 0.02
# Saturated Water Vapor Calculations
RH_percent = np.array(CH4_H2O_data_df_4["RH%"].tolist())
T = np.array(CH4_H2O_data_df_4["RH sensor temperature (C)"].tolist())
Tc = 647.096
k = np.array(1-(T/Tc))
a1 = -7.85951783
a2 = 1.84408259
a3 = -11.7866497
a4 =  22.6807411
a5 = -15.9618719
a6 = 1.80122502
e = 2.718
Pc = 22.064
saturated_water_pressure = np.array(Pc * (e**((Tc/(T+273))*(a1*k+a2*(k**1.5)+a3*(k**3)+a4*(k**3.5)+a5*(k**4)+a6*(k**7.5)))))

# Graph for Water Vapor Pressure vs. Time for 25410.1-47000.1s 
RH_percent = np.array(CH4_H2O_data_df_4["RH%"].tolist())
T = np.array(CH4_H2O_data_df_4["RH sensor temperature (C)"].tolist())
time = np.array(CH4_H2O_data_df_4["Elapsed time (s)"].tolist())
water_vapor_pressure = np.array(RH_percent * (saturated_water_pressure/100))
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "orange")
plt.title("Water vapor pressure change overtime when P_CH4 = 4")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(25410.1, 47000.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=4_version.png")
plt.show()


# In[124]:


# Finding the mean Water Vapor Pressure 

CH4_H2O_data_df_4["water_vapor_pressure"] = water_vapor_pressure

CH4_H2O_data_df_4_improved = CH4_H2O_data_df_4.loc[(CH4_H2O_data_df_4["water_vapor_pressure"]) >= 0.0000023] #filtering out outlier values
water_vapor_pressure_values_4 = CH4_H2O_data_df_4_improved["water_vapor_pressure"]
CH4_4_average = water_vapor_pressure_values_4.mean()
CH4_4_std = water_vapor_pressure_values_4.std()

print(CH4_4_average)
print(CH4_4_std)


# In[128]:


# Finding the mean water vapor pressure for P_CH4 = 0.05

CH4_H2O_data_df_10 = CH4_H2O_data_df[CH4_H2O_data_df["MFC C Actual (sccm)"] == 10]
# Makes the dataframe only including data from rows where P_CH4 = 0.05


#PCH_4 = 10: 47010.1-68600.1 s + 90210.1s-111800.1s


# Finding the water vapor pressure when P_CH4 = 0.02
# Saturated Water Vapor Calculations
RH_percent = np.array(CH4_H2O_data_df_10["RH%"].tolist())
T = np.array(CH4_H2O_data_df_10["RH sensor temperature (C)"].tolist())
Tc = 647.096
k = np.array(1-(T/Tc))
a1 = -7.85951783
a2 = 1.84408259
a3 = -11.7866497
a4 =  22.6807411
a5 = -15.9618719
a6 = 1.80122502
e = 2.718
Pc = 22.064
saturated_water_pressure = np.array(Pc * (e**((Tc/(T+273))*(a1*k+a2*(k**1.5)+a3*(k**3)+a4*(k**3.5)+a5*(k**4)+a6*(k**7.5)))))

# Graph for Water Vapor Pressure vs. Time for 47010.1-68600.1s
RH_percent = np.array(CH4_H2O_data_df_10["RH%"].tolist())
T = np.array(CH4_H2O_data_df_10["RH sensor temperature (C)"].tolist())
time = np.array(CH4_H2O_data_df_10["Elapsed time (s)"].tolist())
water_vapor_pressure = np.array(RH_percent * (saturated_water_pressure/100))
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "orange")
plt.title("Water vapor pressure change overtime when P_CH4 = 10")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(47010.1, 68600.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=10_version(interval1).png")
plt.show()

# Graph for Water Vapor Pressure vs. Time for 90210.1s-111800.1s
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "magenta")
plt.title("Water vapor pressure change overtime when P_CH4 = 10")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(90210.1, 111800.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=10_version(interval2).png")
plt.show()


# In[138]:


# Finding the mean Water Vapor Pressure 

CH4_H2O_data_df_10["water_vapor_pressure"] = water_vapor_pressure

CH4_H2O_data_df_10_improved = CH4_H2O_data_df_10.loc[(CH4_H2O_data_df_10["water_vapor_pressure"]) >= 0.00000231] #filtering out outlier values
water_vapor_pressure_values_10 = CH4_H2O_data_df_10_improved["water_vapor_pressure"]
CH4_10_average = water_vapor_pressure_values_10.mean()
CH4_10_std = water_vapor_pressure_values_10.std()
print(CH4_10_average)
print(CH4_10_std)


# In[73]:


# Finding the mean water vapor pressure for P_CH4 = 0.05

CH4_H2O_data_df_20 = CH4_H2O_data_df[CH4_H2O_data_df["MFC C Actual (sccm)"] == 20]
# Makes the dataframe only including data from rows where P_CH4 = 0.1

#PCH_4 = 20: 68610.1s - 90200.1s + 111810.1s-133400.1s

# Finding the water vapor pressure when P_CH4 = 0.02
# Saturated Water Vapor Calculations
RH_percent = np.array(CH4_H2O_data_df_20["RH%"].tolist())
T = np.array(CH4_H2O_data_df_20["RH sensor temperature (C)"].tolist())
Tc = 647.096
k = np.array(1-(T/Tc))
a1 = -7.85951783
a2 = 1.84408259
a3 = -11.7866497
a4 =  22.6807411
a5 = -15.9618719
a6 = 1.80122502
e = 2.718
Pc = 22.064
saturated_water_pressure = np.array(Pc * (e**((Tc/(T+273))*(a1*k+a2*(k**1.5)+a3*(k**3)+a4*(k**3.5)+a5*(k**4)+a6*(k**7.5)))))

# Graph for Water Vapor Pressure vs. Time for 47010.1-68600.1s
RH_percent = np.array(CH4_H2O_data_df_20["RH%"].tolist())
T = np.array(CH4_H2O_data_df_20["RH sensor temperature (C)"].tolist())
time = np.array(CH4_H2O_data_df_20["Elapsed time (s)"].tolist())
water_vapor_pressure = np.array(RH_percent * (saturated_water_pressure/100))
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "orange")
plt.title("Water vapor pressure change overtime when P_CH4 = 20")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(68610.1, 90200.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=20_version(interval1).png")
plt.show()

# Graph for Water Vapor Pressure vs. Time for 90210.1s-111800.1s
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "magenta")
plt.title("Water vapor pressure change overtime when P_CH4 = 20")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Pressure (atm)")
plt.xlim(111810.1, 133400.1)
plt.legend()
plt.savefig("Graphs/H2O_pressure_change_overtime_P_CH4=20_version(interval2).png")
plt.show()


# In[74]:


# Finding the mean Water Vapor Pressure 

CH4_H2O_data_df_20["water_vapor_pressure"] = water_vapor_pressure
water_vapor_pressure_values_20 = CH4_H2O_data_df_20["water_vapor_pressure"]
CH4_20_average = water_vapor_pressure_values_20.mean()
CH4_20_std = water_vapor_pressure_values_20.std()
print(CH4_20_average)
print(CH4_20_std)


# In[180]:


# boxplot graphs with the water pressures at different partial pressures of CH4

box_plots = {'P_CH4 = 0': water_vapor_pressure_values_0, 'P_CH4 = 0.02': water_vapor_pressure_values_4, 
            'P_CH4 = 0.05': water_vapor_pressure_values_10, 'P_CH4 = 0.1': water_vapor_pressure_values_20,}

y = [CH4_0_average, CH4_4_average, CH4_10_average, CH4_20_average]
fig, ax = plt.subplots()
ax.boxplot(box_plots.values())
x_location=ax.get_xticks()
ax.plot(x_location, y, 'b-')
ax.set_xticklabels(box_plots.keys())


# In[177]:


# graph with points
y = [CH4_0_average, CH4_4_average, CH4_10_average, CH4_20_average]
x = ["P_CH4 = 0", "P_CH4 = 0.02", "P_CH4 = 0.05", "P_CH4 = 0.1" ]
err = [CH4_0_std, CH4_4_std, CH4_10_std, CH4_20_std]

plt.scatter(x, y)
plt.errorbar(x, y, yerr = err) # add linestyle = "None" for no line
plt.show()


# In[198]:


# New Dataframe with average values

array_summary = np.array([["{0:.10f}".format(CH4_0_average), CH4_0_std], ["{0:.10f}".format(CH4_4_average), CH4_4_std], ["{0:.10f}".format(CH4_10_average), CH4_10_std],
                        ["{0:.10f}".format(CH4_20_average), CH4_20_std]])

index = ["P_CH4 = 0", "P_CH4 = 0.02", "P_CH4 = 0.05",
                "P_CH4 = 0.1"]

column = ["average water vapor pressure (atm)", "standard deviation (atm)"]
  
dataframe = pd.DataFrame(data = array_summary, 
                  index = index, 
                  columns = column)

dataframe.to_csv("Methane_Summary", sep='\t')
print(dataframe)

