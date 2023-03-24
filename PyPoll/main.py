#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd


# In[97]:


# File to Load

# Read the modified Budget_Data csv into Pandas DataFrame
pypoll_df = pd.read_csv('Resources/election_data.csv')
pypoll_df.head()


# # The total number of votes cast

# In[98]:


total_num_votes_df = len(pypoll_df["Ballot ID"].unique())
print(f'Total number of votes: {total_num_votes_df}')


# # A complete list of candidates who received votes

# In[99]:


group_df=pypoll_df.groupby("Candidate").count().loc[:,["Ballot ID"]].rename(columns={'Ballot ID':'Number of Votes'})
group_df


# In[102]:


#another way to get the candidate vote count, also helps with calculating the % later

total_candidate_df=pypoll_df["Candidate"].value_counts()
print(f'Total votes per candidate:\n{total_candidate_df}')


# # The percentage of votes each candidate won

# In[103]:


group_df["Vote Percentage"]=(total_candidate_df/total_num_votes_df)

group_df["Vote Percentage"] = (group_df["Vote Percentage"]*100).map("{:.1f}%".format)
group_df


# In[105]:


#Another way to get %

percent_votes_candidate=(total_candidate_df/total_num_votes_df)*100
print(f'Total votes per candidate:\n{percent_votes_candidate}')


# # The winner of the election based on popular vote.

# In[106]:


winner_df=percent_votes_candidate.idxmax()
print (f'Winner is: {winner_df}')


# # Analysis and txt File

# In[107]:


analysis_pypoll = f"Total number of votes: {total_num_votes_df}\n\nComplete candidates who received votes and percentage of each: \n\n{group_df}\n\nWinner of the elections: {winner_df}"

print(analysis_pypoll)


# In[108]:


with open('assignment.txt','w') as file:
    file.write(analysis_pypoll)


# In[ ]:




