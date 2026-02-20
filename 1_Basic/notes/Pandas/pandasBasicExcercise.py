import pandas as pd
from datasets import load_dataset

# Loading Data set
dataset= load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# cleanup
df['job_posted_date']=pd.to_datetime(df.job_posted_date)

df['job_country'].value_counts().head(20)
# if after finding top 20 countries you didn't fnd your country in it and you wnt to make sure if its available or not we can use .isin method  
df['job_country'].isin(['Brazil']) #this alone will give each column with true false value so to jst know that does our country exists we will use .any() on this
df['job_country'].isin(['Brazil']).any()

# Now we will go ahead and create a new data frame with only our country of choice filtered for with that job data
# So I will be going to call this new data frame india_jobs
india_jobs = df[df['job_country'] == 'India']
print(india_jobs)
# now we need to perform a group by aggregation in order to analyse it for things like nedian min etc
india_jobs = india_jobs[india_jobs['salary_year_avg'].notna()]
print(india_jobs.groupby('job_title_short')['salary_year_avg'].count()) #agr ek ek strng bhi hai brackets mai to bhi unhe list bna kr likh skte hai it will print more beautifully
# note that the salary_year_avg wala bracket is not necessary uske bina we can calculate sare columns ka count together but ye saare aggs ke ssath nhi chl skta jaise min ke saath error dedega cz string ka min not able to calculate
print(india_jobs.groupby('job_title_short').count())

print(india_jobs.groupby('job_title_short')['salary_year_avg'].count())


print(india_jobs.groupby('job_title_short')['salary_year_avg'].agg(['median', 'min', 'max', 'count']).sort_values(by='median', ascending=False))