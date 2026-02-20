# PANDAS:Pandas is a powerful, open-source Python library for data manipulation and analysis, offering fast, flexible data structures like DataFrames (similar to spreadsheets or SQL tables) for handling structured data, time series, and matrices. It excels at cleaning, transforming, analyzing, and visualizing data, making it a fundamental tool for data science, enabling tasks like reading/writing various file formats, handling missing data, merging datasets, and performing complex group-by operations. 
import pandas as pd
# df=pd.read_csv('C:\\Users\\HP\\python\\notes\\Pandas\\kanikaa.csv')
# print(df)
# we have loaded data using pd.read_csv ("csv file path") this will print csv file data on terminal in place of.read_csv we can also use .read_excel
# print(type(df))
# this csv file outputs a data frame 
# data frame:A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. It's like a table in a relational database or a spreadsheet.These data frame are a type of dictionaries and can be accessed like dict 
# lets access the tables columns like we access dictionaries
# print(df['City'])
# print(df.City) #both are the ways to access columns and both ways povide exactly same answers
# now what if we need to access a particular index
# print(df.City[1])
# print(df['City'][1])
# Loading a dataset in Pandas refers to the process of importing data from an external source into a Pandas DataFrame
# loading data from datasets after installing datasets on our system we will import datasets
from datasets import load_dataset

dataset= load_dataset('lukebarousse/data_jobs') #this link is from hugging face we have loaded dataset from this srclink its store in cache file of hp folder we have downloaded it from luke's file

# print(dataset['train'])
# print(type(dataset['train'])) #this will give type as dataset but we want it as dataframe so if we remove type and run a method on this data set, write .to_ after dataset bracket then it will show what we could do to it like
df = dataset['train'].to_pandas() #this to_pandas will transform it into dataframe

# Now we will learn how to inspect data in pandas
# df.info()
# print(df['job_title']) #this will give info for specific column

# INSPECTING
print(df.head()) #this will give 1st 5 rows value
print(df.head(10)) #this will give 1st 10 rows value

df.tail() #gives last 5 rows tail(10) gives last 10 rows

print(df['job_title_short'].head(10)) #this will give this column's starting 10 entries

# Now if we need to look at multiple different coloumns altogether so for this i need to provide the data frame a list of columne titles
print(df[['job_title_short', 'job_location']])

# now if we need to access the 100th row of this data then using head will give all 100 value but it will give like 0,1,2,3.......96,97,98,99 like this between data will be missing so if i need to view 90 along with this i can't do that with this method, so we can use a property of dataframe which is somewhat similar to method, it is iloc[] and that stands for integer location and we can use integers to call out things like the index no. of the row and also that of the column
print(df.iloc[90]) #this will show 90th row data
print(df.iloc[90:100]) #this will show data from 90th row to 99th row we have used slicing method here

print(df.iloc[90:100,0:2]) #in this the second arguments is for columne it will give 0,1 index columne headings for these rows
print(df[['job_title_short', 'job_location']].iloc[90:100]) #this is another way better than uper one bcz in that we need to count the columns and in this we can directly access them through their names

print(df.describe()) #describe() pandas DataFrame ka summary tool hai. Ye numerical columns ke liye automatically calculate karta hai count,mean,std or bhi kuch values

print(df.job_title_short.unique()) #.unique() pandas ka method hai jo kisi column ke andar saari unique (non-repeating) values nikaal deta hai.

# now if we want to inspect our data frame specifically for certain job titles so we can use the comparison operator to actually filter for this 
print(df.job_title_short=='Data Analyst') #this line will give whole data frame column with true false value as true which have data analyst for their job_title_short and false for all those which don't have value == DA this can be usd to filter a data frame but to get names of field with data analyst only we will give it a as a condition
print(df[df.job_title_short == 'Data Analyst'])

# now along with job_title_short == data analyst we also want to see DA with salary>10000 so we will write
print(df[(df.job_title_short == 'Data Analyst') & (df.salary_year_avg > 100000)])
# in this if we ever want to use or operator we will write |(pipe symbol)
print(df[(df.job_title_short == 'Data Analyst') | (df.salary_year_avg > 100000)])

# now if we want all numerical values returned back i.e no NaN values so for this
print(df.salary_year_avg.notna())
print(df[(df.job_title_short == 'Data Analyst') & (df.salary_year_avg.notna())])

# CLEANING
# There's a few diff columns we need to clean up but we're jst going to focus on one for right now specificalyy running .info() method and we can see all the different columns and all the diff data types but right now we can see the job posted date is an object 
print(df.info())
print(df.job_posted_date[0]) # when we run this then we can see the answer might be in string i.e between '' this can be cnfrmed by running type on this
print(type(df.job_posted_date[0]))
# now we need to convert this to date time so for this we will use pandas' .todatetime function-This function converts a scalar, array-like, Series or DataFrame/dict-like to a pandas datetime object.
print(pd.to_datetime(df.job_posted_date))
# After running this we can see the dtype:datetime so it is basically converted in this cell but if we inspect the dataframe itself again using info() we will see the type is still object, so we will reassign that job posted date columnto itself once its converted to a date time 
df['job_posted_date']=pd.to_datetime(df.job_posted_date)
df.info()
# so with this column of job posted date we now have access to a new property dt which is date time and its a date time property and then it allows us to go even further with other properties that are available in order to convert it to maybe from date time now to a date or even things like month and then yearr
print(df.job_posted_date.dt.month) #since this .method is a property and not a method so no need to use parenthesis
# now after running this we will run .info() again but we will not see any month value saved inside of here we only have that job_posted_date we want this value inside of our data frame and associated with each one of those rows so we're going to do similar to what we did earlier (assigning) but we need to create a new column 
df['job_posted_month'] = df.job_posted_date.dt.month
df.info()

# now i want to organize my data from first job posting at the begining of the year all the way to the lst posting at the end of yr for this we will use the data frame the method .sort_values, we can also do things like select whether we want to do this ascending or descending the default is ascending set to true
df.sort_values('job_posted_date') #now doing this and again printing df might not chnge original df but will do sorting for this line so we need to kind of reassign for this there are two ways first is df=df.sort_values('job_posted_date') another smart way is to use inplace
df.sort_values('job_posted_date',inplace=True) #note that the first value is by vallue i.e by='job_posted_date but its okk if we not write by
print(df)

# now I want to analyse only the salary yearly data, we have yearly salary data and also hourly salary data so i wnt to remove salary hour avgand then two I want to get rid of any row that don't have values in it so we will use drop method in it we need to specify the labels or basically the columns for this 
df.drop(labels='salary_hour_avg', axis=1, inplace=True) #label:Index or column labels to drop, axis:Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).
df.info()

# now we need to get our data frame down to those 20,000 rows that have only salary data so we need to remove all those null values or nan values which conveniently data frame has this method of dropna
df.dropna(subset=['salary_year_avg'], inplace=True)
df.info()

# ANALYZING: analyzing.py