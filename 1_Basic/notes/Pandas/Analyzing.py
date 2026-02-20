import pandas as pd
from datasets import load_dataset

# Loading Data set
dataset= load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# cleanup
df['job_posted_date']=pd.to_datetime(df.job_posted_date)

print(df.describe()) #now this will give job pasted date column also since we converted it into datetime from str
# anytime we start any analysis .describe is the method we going to use 1st along wid info
print(df.count())
# print(df.median()) now this alone wil throw error as it needs numerical columns only to calculate median so column need to be specified to calculate median
print(df['salary_year_avg'].median())
print(df['salary_year_avg'].min()) 
print(df['salary_year_avg'].idxmin()) #this gives the index value of min salary and we will store that index into a variable
min_salary = df['salary_year_avg'].idxmin()
print(df.iloc[min_salary])
# now we use unique to get an array of all the unique values of the column but it actually doesn't provide much value, I want to fnd out wht are the values or the unique value counts of each of these so instead i will use .value_counts
print(df['job_title_short'].value_counts())

# now till now we were working on individual columns like finding min of a column or value count of a column etc. now what if we need to calculate minimum salary of a particular job_title_short so for this we use groupby method synax will be: df.groupby('columns to group')['column to aggregate'].your agg method 
# like we want each short title min year salary so
print(df.groupby('job_title_short')['salary_year_avg'].min())

# diff methods that we can perform are: .count(),.sum(), .min(),.idxmin(),.max(),.idxmax(),.mean(),.median()
# now getting more deeper we want the grouping country wise so
print(df.groupby(['job_title_short','job_country'])['salary_year_avg'].min())

# now lets say we want to perform aggregations(min,max etc) on multiple columns
print(df.groupby('job_title_short')[['salary_year_avg','salary_hour_avg']].min())

# now if we want to perform multiple aggregations so for this agg method is used
print(df.groupby('job_title_short')['salary_year_avg'].agg(['min','max']))