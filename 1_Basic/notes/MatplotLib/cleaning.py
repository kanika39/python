import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
import numpy as np

dataset= load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date']=pd.to_datetime(df['job_posted_date'])

job_counts = df.job_title_short.value_counts()

plt.bar(job_counts.index, job_counts)
plt.title("Postings of Job Title ")# .title function set a title for axes this title is applied to this plot only if we plot any other plot then it will not title this
plt.ylabel('Count of job postings') #this y label label the y axis
plt.xticks(rotation=45, ha='right')# this will format the x axis labels on this graph to 45 degrees, ha= horizontal alignment this will align those words
plt.show()

# in matplotlib documentation thers a cheatsheet given ehich tells which part of plot is called what and how can we find documentation for them we can take help from there

# now we can also do this plotting through pandas even in easier way or less complicatedly
job_counts.plot(kind='bar') #here kind is which kind of plot you want we can do that formatting here also as
# job_counts.plot(kind='line')
plt.ylabel('Count of job postings')
plt.xlabel('')
plt.title("Postings of Job Title ")
plt.xticks(rotation=45, ha='right')
plt.show()
# but in this pandas plot we can see the y label is shifted down the job titles i.e job_title_short is below DA,DS etc so we need to remove this so we will use xlabel

# this was all about series now we will see how we can plot a dataframe- now in this case with the plot method we're going to provide x and y parameters becoz our data frame has multiple diff columns in it it needs to know what to use. so for this we will plot salary over the yrs
df.plot(x='job_posted_date', y='salary_year_avg', kind='line')
plt.show()