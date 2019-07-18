#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:12:05 2019

@author: shiwanshu
"""
'''
Explanations:
There is a Stair, and you have to return the total number of ways in which a person can climb it. 
eg. if n = 2; --> (1,2),(2), so total 2, similarly for n = 3; it is 4 , for n=1 ; it is 1.
I have implemented this program, in such a way that it will take minimum amount of time. I have created a dictionary which stores the 
new values so when ever there is a second time searching for those value it can look up in o(n) time.  
'''
def staircase(n):
    num_dict = dict({})
    return staircase_dict(n,num_dict)
    pass
def staircase_dict(n,num_dict):
    if n ==1:
        output = 1
    elif n ==2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if n-1 in num_dict:
            first_num = num_dict[n-1]
        else:
            first_num = staircase_dict(n-1,num_dict)
            
        if n-2 in num_dict:
            second_num =  num_dict[n-2]
        else:
            second_num = staircase_dict(n-2,num_dict)
            
        if n-3 in num_dict:
            third_num = num_dict[n-3]
        else:
            third_num = staircase_dict(n-3,num_dict)
            
        output = first_num+second_num+third_num
        
    num_dict[n] = output
    return output
#staircase(4) 
    
def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")
            
test_case = [4, 7]
test_function(test_case)
test_case = [5, 13]
test_function(test_case)
test_case = [3, 4]
test_function(test_case)
test_case = [20, 121415]
test_function(test_case)
