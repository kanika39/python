# matplotlib: Just like pandas is the go-to source when cleaning up and analysing data, matplotlib is the go-to source whenever we're visualising data. Matplotlib is a Python library used to create graphs and visualizations from data. In simple words, it helps you see your data in the form of charts instead of only numbers. we can read or fnd more abt it in matplotlib documentation

# `matplotlib.pyplot` is a state-based interface to matplotlib. It provides an implicit, MATLAB-like, way of plotting. It also opens figures on your screen, and acts as the figure GUI manager.

import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
import numpy as np

# x = np.arange(0,5,0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

# Loading Data set
dataset= load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# cleanup
df['job_posted_date']=pd.to_datetime(df['job_posted_date'])

# we are going to strt with a simple eg first
# x=[1,2,3,4]
# y=[1,2,3,4]
# to plot this we will use the plot function
# plt.plot(x,y)
# plt.show()

# goal is to plot job post things over time
df.job_posted_date.head() #this gives date along with time
# lets go ahead and plot the date values from the entire data frame and we're going to just plot it against each other so we're going to get a straight line 
# plt.plot(df.job_posted_date,df.job_posted_date)

# now we need to modify this so we can perform some sort of aggregation in order to count how many job postings are hapening relative to job posted dates so
date_count=df.job_posted_date.value_counts()
date_count=date_count.sort_index() # plotting without sorting results in a messy plot, but after this sorting there is a mess too thats bcz there is a second diff also in time stamps so the aggeregation we are doing here is not correct we need to do something where we either agg it by day week month or even quarter so we agg it by month

df['job_posted_month']=df['job_posted_date'].dt.month
monthly_counts=df.job_posted_month.value_counts().sort_index()
print(monthly_counts)

print(date_count)#in this whatever gets print on left hand side for the series is actually the index these values on the right hand side are actually the core portion of the series its actually the date counts so we wil plot the graph as
# plt.plot(date_count.index , date_count)
plt.plot(monthly_counts.index , monthly_counts)#idhr y axis mai monthly_counts.values bhi likh skte hai it will give more robust amnt of info almost same he graph will be shown 
plt.show()
# now when we o/p type of date count or monthly count it will not give data frame or like that as o/p its type will be series lets understand now 
# Series vs Dataframe: so we've been primarily focusing on using data frames which are core component or objs inside of pandas but pandas also have this other obj called a series. A series is if you think back to numpy when we had a 1D array this is effectively what a series is. we can create a series by calling pandas and then running series on it and passing it a values of data

series=pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])# if we print this it will give index along with value but we can with this provide an argument of index so the index values like 0,1,2,.. will get replace by those index value list

# we can access series values as
print(series.index)
print(series.values)

# so a column of data within a dataframe is also a series thats why job_posted_date was also a series

# this was all about line charts moving to barcharts
# So for barcharts we will be plotting how many counts of diff job tiles we have and also for baar plotting we use .bar(x ,height)
job_counts=df.job_title_short.value_counts().sort_values(ascending=True)#.head(3)
# plt.bar(job_counts.index, job_counts) #this will also be messy coz job titles will be overlapping each other so we will use head method. but theares a second method also using .barh for horizontal bars .barh(x,width) so now we can remove that head also

plt.barh(job_counts.index, job_counts)
plt.show()

# matplotlib in horizontal barchart strt plotting from the bottom and then upward so we will add sorting method to it 

# now we need to do some cleanup like in previous one we have many prblms like messsiness or x axis can't display names etc so now we will make our plots more presentable
# refer to cleaning.py
