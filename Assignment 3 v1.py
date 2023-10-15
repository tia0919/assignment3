#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Create data frame with csv file
df = pd.read_csv('Recipes-All Recipes.csv')
for index, row in df.iterrows():
    
        
    df = df.reset_index()
    

    df = df[[ 'Name','Ease of Prep', 'Type', 'Prep Time', 'Ingredients']]


# In[3]:


df=df.fillna(0)
df


# In[4]:


target_food_id = df.iloc[2]  # Find the similarities of Lasagna using cosine similarity
print(target_food_id)


# In[17]:


from sklearn.metrics.pairwise import cosine_similarity
cosine_similarities = cosine_similarity(df.iloc[2][numeric_columns].values.reshape(1, -1), df.drop(2)[numeric_columns])

numeric_columns = ['Prep Time']
# Calculate cosine similarities
cosine_similarities = cosine_similarity(df[df['Name'] == 'Lasagna'][numeric_columns], df[numeric_columns])

# Get the indices of the top 10 similar foods
top_indices = cosine_similarities.argsort()[0][::-1][:10]

# Get the details of the top 10 similar foods
top_similar_foods = df.iloc[top_indices]
print(top_similar_foods)


# In[18]:


from sklearn.metrics.pairwise import euclidean_distances #Find the similarity using euclidean distance
numeric_columns = ['Prep Time']

# Calculate Euclidean distances
euclidean_distances = euclidean_distances(df[df['Name'] == 'Lasagna'][numeric_columns], df[numeric_columns])

# Get the indices of the top 10 similar foods
top_indices = euclidean_distances.argsort()[0][:10]

# Get the details of the top 10 similar foods
top_similar_foods = df.iloc[top_indices]
print(top_similar_foods)


# In[19]:


from sklearn.metrics.pairwise import manhattan_distances #Find the similarity using manhattan distance
numeric_columns = ['Prep Time']
# Calculate Manhattan distances
manhattan_distances = manhattan_distances(df[df['Name'] == 'Lasagna'][numeric_columns], df[numeric_columns])

# Get the indices of the top 10 similar foods based on Manhattan distance
top_indices = manhattan_distances.argsort()[0][:10]

# Get the details of the top 10 similar foods
top_similar_foods = df.iloc[top_indices]
print(top_similar_foods)


# In[ ]:




