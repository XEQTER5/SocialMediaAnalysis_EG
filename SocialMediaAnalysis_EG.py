import pandas as pd

df = pd.read_excel("/content/sample_data/social_data.xlsx")
df.head()

df['Eng/Imp'] = df['Total Engagements'] / df['Total Impressions']
df['Eng/Imp'].fillna(-1, inplace=True)
df.loc[df['Eng/Imp'] > 1, 'Eng/Imp'] = -1

df.head()

df['Account'] = df['Account'].str.strip()

# Save the cleaned names back to the 'Account' column
df.to_excel("/content/sample_data/social_data_cleaned.xlsx", index=False)

# Exclude values equal to -1
cleaned_df = df[df['Eng/Imp'] != -1]

cleaned_df.head()

#mean, meadian and mode

mean = cleaned_df['Eng/Imp'].mean()

median = cleaned_df['Eng/Imp'].median()

mode = cleaned_df['Eng/Imp'].mode().values[0]

print("Mean:", mean, "\n")
print("Median:", median, "\n")
print("Mode:", mode)

#Question 1 : Typical Engagement rate and Likelihood of Engagement Rate

likelihood_15_percent = (cleaned_df['Eng/Imp'] >= 0.15).mean() * 100

print("Typical Engagement Rate:", mean , "\n")
print("Likelihood of achieving a 15% Engagement Rate:", likelihood_15_percent, "%")

#Question 2: Which day or time is best for any post.

engagement_by_day = cleaned_df.groupby(cleaned_df['Published Date'].dt.day_name())['Eng/Imp'].mean()


engagement_by_hour = cleaned_df.groupby(cleaned_df['Published Date'].dt.hour)['Eng/Imp'].mean()

print("Engagement Rate by Day of the Week: \n")
print(engagement_by_day)
print()
print("Engagement Rate by Hour of the Day:\n")
print(engagement_by_hour)

#To find out best day for any posts
max_engagement_day = engagement_by_day.idxmax()

#To find out best time for any post
max_engagement_hour = engagement_by_hour.idxmax()

print("Greatest engagement rate of a day in a week  : \n")
print(max_engagement_day)
print()
print("Greatest engagement rate from 24 hour :\n")
print(max_engagement_hour)

# Group by game title and calculate the mean engagement rate
engagement_by_title_account = cleaned_df.groupby(['Account', 'Account Type'])['Eng/Imp'].mean()

# Sort the engagement rates in descending order
sort_engagement = engagement_by_title_account.sort_values(ascending=False)

sorted_engagement = sort_engagement.sort_index(level='Account')

# Print the game titles, account types, and their corresponding engagement rates
print("Engagement Rates by Game Title and Account Type:")
print(sorted_engagement)

# Group by game title, account type, and media type, and calculate the mean engagement rate
engagement_by_title_account_media = cleaned_df.groupby(['Account', 'Account Type', 'Media Type'])['Eng/Imp'].mean()

print(engagement_by_title_account_media)

# Sort the engagement rates in descending order
sorted_engagement = engagement_by_title_account_media.sort_values(ascending=False)

# Find the media type that performs the best according to each game title
best_media_by_title = sorted_engagement.groupby(level='Account').idxmax()

# Print the result
print("Best Media Type by Account:")
print(best_media_by_title)

engagement_by_account_campaign = cleaned_df.groupby(['Account', 'Campaign Name'])['Eng/Imp'].mean()

print(engagement_by_account_campaign)

# Find the best performing campaign for each account
best_campaign_by_account = engagement_by_account_campaign.groupby('Account').idxmax()
best_campaign_by_account = best_campaign_by_account.reset_index().rename(columns={'Eng/Imp': 'Best Campaign'})

print("Best Performing Campaign for Each Account:")
print(best_campaign_by_account)



import pandas as pd
import matplotlib.pyplot as plt

# Rest of your code...

# Visualizing Engagement Rate by Day of the Week
engagement_by_day.plot(kind='bar', color='blue')
plt.title('Engagement Rate by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Engagement Rate')
plt.show()

# Visualizing Engagement Rate by Hour of the Day
engagement_by_hour.plot(kind='bar', color='green')
plt.title('Engagement Rate by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Engagement Rate')
plt.show()