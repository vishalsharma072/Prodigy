#!/usr/bin/env python
# coding: utf-8

# # PASSWORD COMPLEXITY CHECKER

# We will check the strenth of the password in three feedback format(Weak/Average/Strong).
# 
# Conditions for Strong Password:
# 1.. It contains atleast one lowercase English character.
# 2.. It contains atleast one uppercase English character.
# 3.. It contains atleast one special character.This special character are:!@#.
# 4.. It contains atleast one digit.
# 5.. its length is atleast 8.
# 6.. Example: Vishal@123
# 
# 
# Conditions fo Average Password:
# 1.. If length is>6 and all the above conditions do not meet(like any two meets.
# 2.. Example: Xeptouqw12
# 
# 
# Conditions for week Password: 
# 1.. if the length is less than 6.
# 2.. Example: 123ws
# 

# In[2]:


def check_password_strength(password):
    '''
    Program to check the strength of input password
    Parameter:
    password(str): input password
    
    return:
    output(str): week or average or strong
    '''
    special_chars  = list('!@#$%^*)&(')
    isdigit_there  = any(char.isdigit() for char in password)
    isupper_there  = any(char.isupper() for char in password)
    isupper_there  = any(char.isdigit() for char in password)
    check_lower    = any(char.islower() for char in password)
    
    all_true = all([isdigit_there, isupper_there, isupper_there,check_lower])
    if len(password)<6:
        return "WEAK"
    elif len(password)>=8 and all_true :
        return "STRONG"
    else:
        return "AVERAGE"


# In[6]:


input_password = input("Create Password : ")
strength       = check_password_strength(input_password)
print("")
print("your Password is {} !!".format(strength))


# In[ ]:




