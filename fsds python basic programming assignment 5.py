#!/usr/bin/env python
# coding: utf-8

# Answer 1:

# In[1]:


def lcm(a,b):
    '''
    Function which return the LCM of two number.
    '''
    high = a if a > b else b
    
    while True:
        if (high%a==0) and (high%b==0):
            break
        else:
            high += 1
            
    return high


# In[2]:


a = 45
b = 8

lcm(a, b)


# Answer 2:

# In[3]:


def hcf(a, b):
    
    low = a if a < b else b
    
    for i in range(1, low+1):
        if (a%i==0) and (b%i==0):
            hcf = i
            
    return hcf


# In[4]:


a = 22
b = 11

hcf(a, b)


# Answer 3:

# In[5]:


def conversion(num):
    print("Binary:      ", bin(num))
    print("Octal:       ", oct(num))
    print("Hexadecimal: ", hex(num))


# In[7]:


conversion(9)


# In[8]:


conversion(100)


# Answer 4:

# In[10]:


try:
    char = input("Enter a character: ")
    ASCII = ord(char)
    print("ASCII value of {} is {}".format(char, ASCII))
except Exception as e:
    print(e)


# Answer 4:

# In[1]:


try:
    
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        print("\nFor addition:       +")
        print("For subtraction:    -")
        print("For multiplicaton:  *")
        print("For division:       /")
        print("For Exit:            X")
        
        ch = input("\nEnter the choice for mathematical operations: ")
        
        
        if ch == '+':
            output = num1 + num2
        elif ch == '-':
            output = num1 - num2
        elif ch == '*':
            output = num1 * num2
        elif ch == '/':
            output = num1 / num2
        
        if ch == 'X' or ch == 'x':
            break
            
        print("\nResult: ", output)
        
        
            
except Exception as e:
    print(e)


# In[ ]:




