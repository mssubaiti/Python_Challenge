#!/usr/bin/env python
# coding: utf-8

# In[182]:


import pandas as pd


# In[183]:


# File to Load

# Read the modified Budget_Data csv into Pandas DataFrame
pybank_df = pd.read_csv('Resources/budget_data.csv', index_col=False)
pybank_df.head()


# # The total number of months included in the dataset

# In[184]:


num_months_df = len(pybank_df["Date"].unique())
print(f'Total number of months: {num_months_df}')


# # The net total amount of "Profit/Losses" over the entire period

# In[185]:


total_profitloss_df =pybank_df["Profit/Losses"].sum()
print(f'Total amount of Profit/Losses: ${total_profitloss_df}')


# # The changes in "Profit/Losses" over the entire period, and then the average of those changes

# In[186]:


#changes in profit/losses

profloss_change_df = pybank_df['Profit/Losses'].diff()

#Average of the changes

avg_change_df=profloss_change_df.mean()
print(f'Average of changes in Profit/Losses:${avg_change_df}')


# # The greatest increase in profits (date and amount) over the entire period

# In[187]:


greatest_incprof_df= profloss_change_df.idxmax()

greatest_inc_date_df=pybank_df.loc[greatest_incprof_df,'Date']
greatest_inc_date_df


# In[188]:


greatest_inc_amount_df=profloss_change_df[greatest_incprof_df]
print(f"The Greatest increase in profits is:${greatest_inc_amount_df}")


# # The greatest decrease in profits (date and amount) over the entire period

# In[189]:


greatest_decprof_df= profloss_change_df.idxmin()

greatest_dec_date_df=pybank_df.loc[greatest_decprof_df,'Date']
greatest_dec_date_df


# In[190]:


greatest_dec_amount_df=profloss_change_df[greatest_decprof_df]
print(f"The greatest decrease in profits is:$ {greatest_dec_amount_df}")


# In[191]:


summary_df = pd.DataFrame({"Sum of Months": [num_months_df],
                         "Net Total Profit/Losses":[total_profitloss_df],
                         "Average Change":[avg_change_df],
                         "Greatest increase in profits (Month)":[greatest_inc_date_df],
                         "Greatest increase in profits amount":[greatest_inc_amount_df],
                         "Greatest decrease in profits (month)":[greatest_dec_date_df],
                         "Greatest decrease in profits amount":[greatest_dec_amount_df]}).reset_index(drop=True)

summary_df


# In[192]:


#Mapping the values - providing $ for the profits and losses

summary_df["Net Total Profit/Losses"] = summary_df["Net Total Profit/Losses"].map("${:,.2f}".format)
summary_df["Average Change"] = summary_df["Average Change"].map("${:,.2f}".format)
summary_df["Greatest increase in profits amount"] = summary_df["Greatest increase in profits amount"].map("${:,.2f}".format)
summary_df["Greatest decrease in profits amount"] = summary_df["Greatest decrease in profits amount"].map("${:,.2f}".format)


# In[193]:


summary_df.reset_index(drop=True)
display(summary_df)


# # Print the analysis to the terminal and export a text file with the results

# In[194]:


#full assignment in one code

analysis_pybank= f'Total Months: {num_months_df}\nAverage change: ${avg_change_df}\nGreatest Increase in Profits Date: {greatest_inc_date_df}\nGreatest Increase in Profits Amount: ${greatest_inc_amount_df}\nGreatest Decrease in Profits Date: {greatest_dec_date_df}\nGreatest Decrease in Profits Amount: ${greatest_dec_amount_df}'


print (analysis_pybank)


# In[195]:


with open('analysis.txt','w') as file:
    file.write(analysis_pybank)

