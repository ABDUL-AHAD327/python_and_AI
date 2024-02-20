import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Data Loading
# Load the dataset into Pandas DataFrame
df = pd.read_csv("c:\Users\hp\OneDrive\Desktop\semester 6\AI Lab\dataset.csv")

# Check for missing values and handle them appropriately
# For simplicity, let's drop rows with missing values
df = df.dropna()

# Step 2: Social Network Analysis
# Use NetworkX to create a graph representation of the social network
G = nx.from_pandas_edgelist(df, 'source', 'target')

# Step 3: Attribute Analysis
# Explore the distribution of age among individuals in the network using visualizations
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Age in the Social Network')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Perform simple linear regression to analyze the relationship between the number of connections and age
X = df[['age']]
y = df['connections']

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Visualize the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='skyblue')
plt.plot(X, model.predict(X), color='red', linewidth=2)
plt.title('Linear Regression: Age vs. Number of Connections')
plt.xlabel('Age')
plt.ylabel('Number of Connections')
plt.show()

# Step 4: Insights
# Given a new age of 30 years, use your trained model to predict its connections
new_age = [[30]]
predicted_connections = model.predict(new_age)

print(f"Predicted connections for a new age of 30 years: {predicted_connections[0]}")
