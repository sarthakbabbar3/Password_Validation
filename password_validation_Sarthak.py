# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:14:58 2019

@author: sarth
"""

#Validity of password

#using regular expression library
import re

def password_check(password):
    
    #Minimum length: 6
    if(len(password)<6):
        print(password,"Failure Password must be at least 6 characters long.")
    
    #Maximum length: 12
    elif(len(password)>12):
        print(password,"Failure Password must be at max 12 characters long.")
        
    #At least 1 letter in [a-z]
    elif(re.search(r"[a-z]", password) is None):
        print(password,"Failure Password must contain at least one letter from a-z.")
        
    #At least 1 letter in [0-9]
    elif(re.search(r"[0-9]", password) is None):
        print(password,"Failure Password must contain at least one letter from 0-9.")
        
    #At least 1 letter in [A-Z]
    elif(re.search(r"[A-Z]", password) is None):
        print(password,"Failure Password must contain at least one letter from A-Z.")
        
    #At least 1 letter in [*$_#=@]
    elif(re.search(r"[*$_#=@]", password) is None):
        print(password,"Failure Password must contain at least one letter from *$_#=@.")
    
    #cannot contain %!)(
    elif(re.search(r"[%!)(]", password) is not None):
        print(password,"Failure Password cannot contain %!)(.")
    
    
    #If it doesnt match any other condition, our password is a Success
    else:
        print(password,"Success")
    
    
    
#Accept comma seperated input
password_list = input("Enter comma separated passwords :").split(",")

#Check each password for conditions
for i in password_list:
    password_check(i)
    
       

    
    
        
    