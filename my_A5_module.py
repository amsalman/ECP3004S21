# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:41:09 2021

@author: Hadis
"""

#Hadi Salman
#Assignment 5
#2/28/2021

#Exercise 1 

def variance(x):
    list_len = len(x)
    print("length of the list ", list_len)
    sum_list = sum(x)
    average = sum_list/list_len
    # vriance :
    variance = sum((v-average) ** 2 for v in x)/list_len
    print("variance of the list: ", variance)
    
#Exercise 2

def co_variance(y,x):
    len_list_x = len(x)
    len_list_y = len(y)
    print("length of the lists: ", len_list_y,", ",len_list_x)
    if len_list_x == len_list_y:
        list_len = len_list_x
        average_x = sum(x)/list_len
        average_y = sum(y)/list_len
        # vriance :
        covariance = sum((x-average_x) * (y-average_y) for x,y in zip(x,y))/list_len
        print("covariance of two lists: ", covariance)
    else:
        print("list of different lengths encountered....")
        print("#### ERROR...! ####")

## usage     
x = [1, 2, 3, 4, 5, 6]
y = [6, 7, 3, 9, 10, 15]
variance(x)
co_variance(y,x)    

#Exercise 3,4,5

#x = np.array([3,9,3,4,5])

#y = np.array([17,40,14,16,15])

#n = np.size(x)

#x_mean = np.mean(x)

#y_mean = np.mean(y)

#x_mean,y_mean

#Sxy = np.sum(x*y)- n*x_mean*y_mean

#Sxx = np.sum(x*x)-n*x_mean*x_mean

#b1 = Sxy/Sxx

#b0 = y_mean-b1*x_mean

  print('slope b1 is', b1)

print('intercept b0 is', b0)

plt.scatter(x,y)

plt.xlabel('Independent variable X')

plt.ylabel('Dependent variable y')