# NUMPY
# NumPy, short for Numerical Python, is a fundamental open-source library in Python for scientific computing.
# It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays efficiently.
# numpy reduces time complexity for any numerical prblm like
import random
import timeit #this calculates the avg time a cmnd takes to execute the function
import numpy as np
import statistics

# salary=[random.randint(5000,100000) for _ in range(10_000_000)]

# print(timeit.timeit(lambda: statistics.median(salary), number=5)) #this number=10 tells timeit to run this function 10 times and then tell avg time

# print(timeit.timeit(lambda: np.median(salary), number=5))

# here np takes 0.7 sec and statistics take 3.7sec that means np reduces the time of mathematical operations

# Some basic operation 

# ARRRAY DEF: np.array
# my_array=np.array([1,2,3,4])
# print(my_array.mean())

# job_titles=np.array(['Data Analyst','Data Science','Data Engineer','Machine Learning Engineer','AI engineer'])
# base_salaries=np.array([60000,80000,75000,90000,np.nan])
# bonus_rates=np.array([.05,.1,.08,.12,np.nan])

# total_salaries=base_salaries * (1+bonus_rates)
# print(total_salaries)

# print(np.mean(total_salaries))
# print(np.nanmean(total_salaries))

# now if we have one more job title like ai engineer and we don't know its base salary and bonus rate so we can't add 0 for ai cz it will affect its mean for this situation there is a term in numpy 'NONE' but if we use none here it will through error while calculating total salaries cause it can't be added so here we use np.nan that means not a number. it is specifically used for numerical values now if we use normal np.mean wit nan so it will give nan as answer for nan we use np.nanmean()
# print(type(np.nan)) #since its type is float so it can get add in total_salaries
# print(type(None))

# numpy has more of this kind of operations but we will not dive deep into this