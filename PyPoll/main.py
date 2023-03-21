#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# File to Load

# Read the modified Budget_Data csv into Pandas DataFrame
pypoll_df = pd.read_csv('election_data.csv')
pypoll_df.head()


# # The total number of votes cast

# In[3]:


total_num_votes_df = len(pypoll_df["Ballot ID"].unique())
print(f'Total number of votes: {total_num_votes_df}')


# # A complete list of candidates who received votes

# In[4]:


total_candidate_df=pypoll_df["Candidate"].value_counts()
print(f'Total votes per candidate:\n{total_candidate_df}')


# # The percentage of votes each candidate won

# In[5]:


percent_votes_candidate=(total_candidate_df/total_num_votes_df)*100
print(f'Total votes per candidate:\n{percent_votes_candidate}')


# # The winner of the election based on popular vote.

# In[6]:


winner_df=percent_votes_candidate.idxmax()
print (f'Winner is: {winner_df}')


# In[7]:


#full assignment in one code
assignment_pypoll = f'Total number of votes: {total_num_votes_df}\n\nComplete candidates who received votes: \n\n{total_candidate_df}\n\nCandidates vote percentage:\n\n {percent_votes_candidate}\n\nWinner of the elections: {winner_df}'


print (assignment_pypoll)


# In[8]:


with open('assignment.txt','w') as file:
    file.write(assignment_pypoll)


# In[ ]:




