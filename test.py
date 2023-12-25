import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read JSON files into pandas DataFrames
file1 = '/Users/colegulledge/Downloads/Spotify Account Data/StreamingHistory2.json'
file2 = '/Users/colegulledge/Downloads/Spotify Account Data/StreamingHistory1.json'
file3 = '/Users/colegulledge/Downloads/Spotify Account Data/StreamingHistory0.json'

df1 = pd.read_json(file1)
df2 = pd.read_json(file2)
df3 = pd.read_json(file3)

# Step 2: Merge DataFrames
df = pd.concat([df1, df2, df3])

# Step 3: Group by "Artist" and sum "ms played"
grouped_df = df.groupby('artistName')['msPlayed'].sum().reset_index()

# Step 4: Convert "ms played" to minutes
grouped_df['minutes played'] = grouped_df['msPlayed'] / (1000 * 60)

# Step 5: Sort by the sum of "ms played" in descending order
sorted_df = grouped_df.sort_values(by='msPlayed', ascending=False)

# Step 6: Select the top 15 artists
top_artists = sorted_df.head(15)

# Step 7: Plot a bar graph
# plt.figure(figsize=(10, 6))
# plt.bar(top_artists['artistName'], top_artists['minutes played'])
# plt.xlabel('Artist')
# plt.ylabel('Minutes Played')
# plt.title('Top 15 Artists by Total Minutes Played')
# plt.xticks(rotation=45, ha='right')
# plt.show()

# plt.figure(figsize=(10, 6))
# colors = sns.color_palette("viridis", len(top_artists))  # Use 'viridis' color palette
# plt.bar(top_artists['artistName'], top_artists['minutes played'], color=colors)
# plt.xlabel('Artist')
# plt.ylabel('Minutes Played')
# plt.title('Top 15 Artists by Total Minutes Played')
# plt.xticks(rotation=45, ha='right')
# plt.show()

df['Date'] = pd.to_datetime(df['endTime'])

# Group by month and sum 'ms played'
monthly_df = df.groupby(df['Date'].dt.to_period("D"))['msPlayed'].sum().reset_index()

# Convert 'ms played' to minutes
monthly_df['minutes played'] = monthly_df['msPlayed'] / (1000 * 60)

# Plot the total minutes played per month
plt.figure(figsize=(10, 6))
plt.fill_between(monthly_df['Date'].dt.strftime('%Y-%m'), monthly_df['minutes played'], color='skyblue', alpha=0.4)
plt.plot(monthly_df['Date'].dt.strftime('%Y-%m'), monthly_df['minutes played'], marker='o', linestyle='-', color='b')
# Enhance aesthetics
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Minutes Played', fontsize=14)
plt.title('Total Minutes Played per Month (Area under the Curve)', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
