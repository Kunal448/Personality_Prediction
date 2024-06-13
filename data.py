import pandas as pd
import numpy as np

# Define the possible values for each column
features = {
    'movie_preferences' : ['Action', 'Comedy', 'Mystery', 'Science Fiction'],
    'social_media_activity' : ['Lifestyle', 'Food', 'Fashion', 'Fitness', 'Games'],
    'reading_habits' : ['Novels', 'Short Stories','Comics'],
    'favorite_leisure_activities' : ['Drawing', 'Reading', 'Sports', 'Gaming'],
    'music_taste' : ['Rap', 'Jazz', 'Classical', 'EDM'], 
    'fashion_style' : ['Casual', 'Classic', 'Vintage', 'Sporty'],
    'travel_preferences' : ['Adventure', 'Road Trips', 'Solo Travel', 'Family Holidays'],
    'personality_behaviour' : ['Complex', 'Versatile']
}

# Generate random data for each column
data = {
    'movie_preferences': np.random.choice(features['movie_preferences'], size=10000),
    'social_media_activity': np.random.choice(features['social_media_activity'], size=10000, p=[0.3, 0.1, 0.3, 0.2, 0.1]),
    'reading_habits': np.random.choice(features['reading_habits'], size=10000, p=[0.2, 0.4, 0.4]),
    'favorite_leisure_activities': np.random.choice(features['favorite_leisure_activities'], size=10000, p=[0.3, 0.2, 0.3, 0.2]),
    'music_taste': np.random.choice(features['music_taste'], size=10000, p=[0.25, 0.25, 0.25, 0.25]),
    'fashion_style': np.random.choice(features['fashion_style'], size=10000, p=[0.3, 0.2, 0.3, 0.2]),
    'travel_preferences': np.random.choice(features['travel_preferences'], size=10000, p=[0.2, 0.3, 0.3, 0.2]),
    'personality_behaviour': np.random.choice(features['personality_behaviour'], size=10000, p=[0.7, 0.3])
}

# Create DataFrame
df = pd.DataFrame(data)

df.to_csv("Personality.csv", index=False)
