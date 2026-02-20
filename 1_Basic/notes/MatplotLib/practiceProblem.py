import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
import numpy as np

dataset= load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date']=pd.to_datetime(df['job_posted_date'])

job_salary=df.groupby('job_title_short')['salary_year_avg'].median().sort_values()

job_salary.plot(kind='barh')
plt.ylabel('')
plt.xlabel('Salary ($USD)')
plt.title("Median Salary By Job Title")
plt.show()