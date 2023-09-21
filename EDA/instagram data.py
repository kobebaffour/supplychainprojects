# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("instagram data.csv", encoding = "latin-1")

# %%
print(data.head())

# %%
print(data.columns)

# %%
print(data.info())

# %%
print(data.describe())

# %%
print(data.isnull().sum())

# %%
# Distribution of Impressions

fig = px.histogram(data,
                   x = "Impressions",
                   nbins = 10,
                   title = "Distribution of Impressions")
fig.show()

# %%
# Impressions on each post over time

fig = px.line(data, x = data.index,
              y = "Impressions",
              title = "Impressions Over Time")
fig.show()

# %%
# Likes, Saves and Follows from each post over time

fig = go.Figure()

fig.add_trace(go.Scatter(x=data.index, y = data["Likes"], name = "Likes"))
fig.add_trace(go.Scatter(x=data.index, y = data["Saves"], name = "Saves"))
fig.add_trace(go.Scatter(x=data.index, y = data["Follows"], name = "Follows"))

fig.update_layout(title="Metrics Over Time",
                  xaxis_title = "Date",
                  yaxis_title = "Count")

fig.show()

# %%
# Distribution of reach from different sources

reach_sources = ["From Home", "From Hashtags", "From Explore", "From Other"]
reach_counts = [data[source].sum() for source in reach_sources]

colors = ['#FFB6C1', '#87CEFA', '#90EE90', '#FFDAB9']

fig = px.pie(data_frame=data, names=reach_sources, 
             values=reach_counts, 
             title='Reach from Different Sources',
             color_discrete_sequence=colors)
fig.show()

# %%
# Distribution of engagement

engagement_metrics = ['Saves', 'Comments', 'Shares', 'Likes']
engagement_counts = [data[metric].sum() for metric in engagement_metrics]

colors = ['#FFB6C1', '#87CEFA', '#90EE90', '#FFDAB9']

fig = px.pie(data_frame=data, names=engagement_metrics, 
             values=engagement_counts, 
             title='Engagement Sources',
             color_discrete_sequence=colors)
fig.show()

# %%
# Number of profile visists and follows

fig = px.scatter(data, 
                 x='Profile Visits', 
                 y='Follows', 
                 trendline = 'ols',
                 title='Profile Visits vs. Follows')
fig.show()

# %%
# Type of hashtags used in the posts using a wordcloud

from wordcloud import WordCloud

hashtags = ' '.join(data['Hashtags'].astype(str))
wordcloud = WordCloud().generate(hashtags)

fig = px.imshow(wordcloud, title='Hashtags Word Cloud')
fig.show()

# %%
# Exclude non-numeric columns from the DataFrame
numeric_data = data.select_dtypes(include=['number'])

# Calculate the correlation matrix for numeric columns
corr_matrix = numeric_data.corr()


# %%
# Exclude non-numeric columns from the DataFrame
numeric_data = data.select_dtypes(include=['number'])

# Calculate the correlation matrix for numeric columns
corr_matrix = numeric_data.corr()


# %%
import pandas as pd

# Assuming you have already loaded your DataFrame 'data'

# One-hot encode the 'Hashtags' column
hashtags_encoded = data['Hashtags'].str.get_dummies(sep=' ')

# Combine the one-hot encoded columns with the numeric columns
data_encoded = pd.concat([data.drop(['Hashtags', 'Caption'], axis=1), hashtags_encoded], axis=1)

# Calculate the correlation matrix
corr_matrix = data_encoded.corr()


# %%
# Select only the numeric columns from the DataFrame
numeric_data = data.select_dtypes(include=['int64'])

# Calculate the correlation matrix for the numeric columns
corr_matrix = numeric_data.corr()

# Creating and displaying the heatmap
fig = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                               x=corr_matrix.columns,
                               y=corr_matrix.index,
                               colorscale='RdBu',
                               zmin=-1,
                               zmax=1))

fig.update_layout(title='Correlation Matrix',
                  xaxis_title='Features',
                  yaxis_title='Features')

fig.show()


# %%
# Create a list to store all hashtags

all_hashtags = []

# Iterate through each row in the 'Hashtags' column
for row in data["Hashtags"]:
    hashtags = str(row).split()
    hashtags = [tag.strip() for tag in hashtags]
    all_hashtags.extend(hashtags)

# Create a pandas Dataframe to store the hashtag distribution
hashtag_distribution = pd.Series(all_hashtags).value_counts().reset_index()
hashtag_distribution.columns = ["Hashtag", "Count"]

fig = px.bar(hashtag_distribution, x = "Hashtag",
             y = "Count", title = "Distribution of Hashtags")
fig.show()
 
    

# %%
# Create a dictionary to store the likes and impressions for each hashtag
hashtag_likes = {}
hashtag_impressions = {}

# Iterate through each row in the dataset
for index, row in data.iterrows():
    hashtags = str(row['Hashtags']).split()
    for hashtag in hashtags:
        hashtag = hashtag.strip()
        if hashtag not in hashtag_likes:
            hashtag_likes[hashtag] = 0
            hashtag_impressions[hashtag] = 0
        hashtag_likes[hashtag] += row['Likes']
        hashtag_impressions[hashtag] += row['Impressions']

# Create a DataFrame for likes distribution
likes_distribution = pd.DataFrame(list(hashtag_likes.items()), columns=['Hashtag', 'Likes'])

# Create a DataFrame for impressions distribution
impressions_distribution = pd.DataFrame(list(hashtag_impressions.items()), columns=['Hashtag', 'Impressions'])

fig_likes = px.bar(likes_distribution, x='Hashtag', y='Likes', 
                   title='Likes Distribution for Each Hashtag')

fig_impressions = px.bar(impressions_distribution, x='Hashtag', 
                         y='Impressions', 
                         title='Impressions Distribution for Each Hashtag')

fig_likes.show()
fig_impressions.show()

# %% [markdown]
# ## Summary
# #### Exploratory data analysis (EDA) is a Data Science concept where we analyze a dataset to discover patterns, trends, and relationships within the data. It helps us better understand the information contained in the dataset and guides us in making informed decisions and formulating strategies to solve real business problems.


