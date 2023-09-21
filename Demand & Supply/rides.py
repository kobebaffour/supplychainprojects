# %%
# import libraries

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('rides.csv')
print(data.head())

# %%
print(data.isnull().sum())

# %% [markdown]
# The dataset has 54 null values in the Rides Completed column. 

# %%
# Drop Null values

data = data.dropna()

# %%
demand = data["Riders Active Per Hour"]
supply = data["Drivers Active Per Hour"]

figure = px.scatter(data, x = "Drivers Active Per Hour",
                    y = "Riders Active Per Hour", trendline="ols", 
                    title="Demand and Supply Analysis")
figure.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)",
)
figure.show()

# %% [markdown]
# There is a constant relationship between the number of drivers active per hour and the number of riders active per hour.
# 
# A constant relationship between the number of drivers active per hour and the number of riders active per hour means that for every X number of drivers, there is a consistent and predictable Y number of riders, and this ratio remains constant over time.

# %% [markdown]
# The elasticity of demand for rides concerning the number of active drivers per hour:

# %%
# Calculate elasticity
avg_demand = data['Riders Active Per Hour'].mean()
avg_supply = data['Drivers Active Per Hour'].mean()
pct_change_demand = (max(data['Riders Active Per Hour']) - min(data['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(data['Drivers Active Per Hour']) - min(data['Drivers Active Per Hour'])) / avg_supply * 100
elasticity = pct_change_demand / pct_change_supply

print("Elasticity of demand with respect to the number of active drivers per hour: {:.2f}".format(elasticity))

# %% [markdown]
# It signifies a moderately responsive relationship between the demand for rides and the number of active drivers per hour. Specifically, this means that a 1% increase in the number of active drivers per hour would lead to a 0.82% decrease in the demand for rides, while a 1% decrease in the number of active drivers per hour would lead to a 0.82% increase in the demand for rides.
# 
# This level of elasticity suggests that the demand for rides is somewhat sensitive to changes in the number of active drivers per hour.

# %% [markdown]
# Add a new column in the dataset by calculating the supply ratio:

# %%
# Calculate the supply ratio for each level of driver activity

data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']
print(data.head())

# %%
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], 
                         y=data['Supply Ratio'], mode='markers'))
fig.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active Per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
)
fig.show()

# %% [markdown]
# The above graph shows the ratio of the number of drivers active per hour and the number of rides completed in an hour.

# %% [markdown]
# ### Summary
# 
# Demand and Supply analysis means analyzing the relationship between the quantity demanded and the quantity supplied. It helps businesses understand the factors influencing consumer demand to maximize profits.


