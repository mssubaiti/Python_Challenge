#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


# File to Load

# Read the modified Budget_Data csv into Pandas DataFrame
pybank_df = pd.read_csv('budget_data.csv')
pybank_df.head()


# # The total number of months included in the dataset

# In[3]:


num_months_df = len(pybank_df["Date"].unique()) -1
print(f'Total number of months: {num_months_df}')


# # The net total amount of "Profit/Losses" over the entire period

# In[5]:


total_profitloss_df =pybank_df["Profit/Losses"].sum()-1
print(f'Total amount of Profit/Losses: {total_profitloss_df}')


# # The changes in "Profit/Losses" over the entire period, and then the average of those changes

# In[6]:


#changes in profit/losses

profloss_change_df = pybank_df['Profit/Losses'].diff()

#Average of the changes

avg_change_df=profloss_change_df.mean()
print(f'Average of changes in Profit/Losses:{avg_change_df}')


# In[13]:


greatest_incprof_df= profloss_change_df.idxmax()
print(f'Greatest increase in profits:{greatest_incprof_df}')


# In[14]:


greatest_inc_date_df=pybank_df.loc[greatest_incprof_df,'Date']
greatest_inc_date_df


# In[8]:


greatest_inc_amount_df=profloss_change_df[greatest_incprof_df]
greatest_inc_amount_df


# # The greatest decrease in profits (date and amount) over the entire period

# In[9]:


greatest_decprof_df= profloss_change_df.idxmin()
print(f'Greatest decrease in profits:{greatest_decprof_df}')


# In[10]:


greatest_dec_date_df=pybank_df.loc[greatest_decprof_df,'Date']

greatest_dec_date_df


# In[11]:


greatest_dec_amount_df=profloss_change_df[greatest_decprof_df]
greatest_dec_amount_df


# # Print the analysis to the terminal and export a text file with the results

# In[15]:


#full assignment in one code
assignment = f'Total Months: {num_months_df}\nAverage change: {avg_change_df}\nGreatest Increase in Profits Date: {greatest_inc_date_df}\nGreatest Increase in Profits Amount {greatest_inc_amount_df}\nGreatest Decrease in Profits Date: {greatest_dec_date_df}\nGreatest Decrease in Profits Amount {greatest_dec_amount_df}'


print (assignment)


# In[ ]:


with open('assignment.txt','w') as file:
    file.write(assignment)

