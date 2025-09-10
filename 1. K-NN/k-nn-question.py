import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
data = {
    'Movie title': [
        'California Man',
        'He\'s Not Really into Dudes',
        'Beautiful Woman',
        'Kevin Longblade',
        'Robo Slayer 3000',
        'Amped II',
        '?'
    ],
    '# of kicks': [3, 2, 1, 101, 99, 98, 18],
    '# of hugs': [104, 100, 81, 10, 5, 2, 90],
    'Movie Type': ['Romance', 'Romance', 'Romance', 'Action', 'Action', 'Action', 'Unknown']
}

# Create DataFrame
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(8.4, 6))

# Group by movie genre and plot separate scatter plots
romance_mask = df['Movie Type'] == 'Romance'
action_mask = df['Movie Type'] == 'Action'
unknown_mask = df['Movie Type'] == 'Unknown'

plt.scatter(
    df.loc[romance_mask, '# of kicks'],
    df.loc[romance_mask, '# of hugs'],
    color='blue',
    label='Romance'
)
