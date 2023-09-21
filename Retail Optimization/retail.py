# %%
# import libraries

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("retail_price.csv")
print(data.head())

# %%
print(data.isnull().sum())

# %%
print(data.describe())

# %% [markdown]
# Distribution of the prices of the products

# %%
fig = px.histogram(data,
                   x = "total_price",
                   nbins = 20,
                   title = "Distribution of Total Price")

fig.show()

# %% [markdown]
# Distribution of the unit prices using a box plot

# %%
fig = px.box(data,
             y = "unit_price",
             title = "Box Plot of Unit Price")

fig.show()

# %% [markdown]
# Relationship between quantity and total prices

# %%
fig = px.scatter(data,
                 x = "qty",
                 y = "total_price",
                 title = "Quantity vs Total Price", trendline = "ols")

fig.show()

# %% [markdown]
# Thus, the relationship between quantity and total prices is linear. It indicates that the price structure is based on a fixed unit price, where the total price is calculated by multiplying the quantity by the unit price.

# %% [markdown]
# The average total prices by product categories:

# %%
fig = px.bar(data, x = "product_category_name",
             y = "total_price",
             title = "Average Total Price by Product Category")

fig.show()

# %% [markdown]
# The distribution of total prices by weekday using a box plot:

# %%
fig =  px.box(data, x = "weekday",
              y = "total_price",
              title = "Box Plot of Total Price by Weekday")

fig.show()

# %% [markdown]
# The distribution of total prices by holiday using a box plot:

# %%
fig = px.box(data, x = "holiday",
             y = "total_price",
             title = "Box Plot of Total Price by Holiday")

fig.show()

# %% [markdown]
# The correlation between the numerical features with each other:

# %%
# Select numeric columns
numeric_columns = data.select_dtypes(include=['number'])

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

# Now you can create a heatmap of the correlation matrix using Plotly
import plotly.graph_objects as go

fig = go.Figure(go.Heatmap(
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    z=correlation_matrix.values,))

fig.update_layout(title="Correlation Heatmap of Numerical Features")
fig.show()


# %% [markdown]
# Analyzing competitors’ pricing strategies is essential in optimizing retail prices. Monitoring and benchmarking against competitors’ prices can help identify opportunities to price competitively, either by pricing below or above the competition, depending on the retailer’s positioning and strategy.

# %% [markdown]
# The average competitor price difference by product category:

# %%
data['comp_price_diff'] = data['unit_price'] - data['comp_1'] 

avg_price_diff_by_category = data.groupby('product_category_name')['comp_price_diff'].mean().reset_index()

fig = px.bar(avg_price_diff_by_category, 
             x='product_category_name', 
             y='comp_price_diff', 
             title='Average Competitor Price Difference by Product Category')
fig.update_layout(
    xaxis_title='Product Category',
    yaxis_title='Average Competitor Price Difference'
)
fig.show()

# %% [markdown]
# ### Retail Price Optimization Model with Machine Learning

# %%
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

X = data[['qty', 'unit_price', 'comp_1', 
          'product_score', 'comp_price_diff']]
y = data['total_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2,
                                                    random_state=42)

# Train a linear regression model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# %% [markdown]
# Let’s make predictions and have a look at the predicted retail prices and the actual retail prices:

# %%
y_pred = model.predict(X_test)

fig = go.Figure()
fig.add_trace(go.Scatter(x=y_test, y=y_pred, mode='markers', 
                         marker=dict(color='blue'), 
                         name='Predicted vs. Actual Retail Price'))
fig.add_trace(go.Scatter(x=[min(y_test), max(y_test)], y=[min(y_test), max(y_test)], 
                         mode='lines', 
                         marker=dict(color='red'), 
                         name='Ideal Prediction'))
fig.update_layout(
    title='Predicted vs. Actual Retail Price',
    xaxis_title='Actual Retail Price',
    yaxis_title='Predicted Retail Price'
)
fig.show()

# %% [markdown]
# ### Summary
# The ultimate aim of optimizing retail prices is to charge a price that helps you make the most money and attracts enough customers to buy your products. It involves using data and pricing strategies to find the right price that maximizes your sales and profits while keeping customers happy.


