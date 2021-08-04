#!/usr/bin/env python
# coding: utf-8

# # 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.

# In[ ]:


*          # multiplication operator
'hello'    #string
-87.8      #float
-          #subtraction operator
(#division, operator)
+          # addition operator
6          #integer


# # 2. What is the difference between string and variable?

# In[ ]:


String may contain letters, numbers and other characters. it is written by using double inverted commas(" "). 


Variable is something which stores data into it per se str, int, float, etc


# # 3. Describe three different data types.

# In[ ]:


Integers – This value is represented by int class. It contains positive or negative whole numbers (without fraction or decimal). In Python there is no limit to how long an integer value can be.

Float – This value is represented by float class. It is a real number with floating point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation. 
 
Complex Numbers – Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j. For example – 2+3j 


# # 4.What is an expression made up of? What do all expressions do?

# In[ ]:


An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.


# # 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# In[ ]:


An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.

A statement is an instruction that the Python interpreter can execute. We have only seen the assignment statement so far. Some other kinds of statements that we’ll see shortly are while statements, for statements, if statements, and import statements.


# # 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# 
# bacon + 1

# In[5]:


bacon = 22

x= bacon + 1

print (x)


# # 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 
# 
# 'spam' * 3

# In[16]:


'spam' + 'spamspam'

'spam' * 3


# # 8.Why is eggs a valid variable name while 100 is invalid?

# In[ ]:


Because variable names cannot begin with a number.


# # 9.What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[ ]:


The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions 


# # 10.Why does this expression cause an error? How can you fix it?
# 
# 'I have eaten' + 99 +  'burritos'

# In[ ]:


'I have eaten' + 99 +  'burritos'  # if we execute this it causes type error which means that execution can only only concatenate str (not "int") to str


# In[22]:


'I have eaten' + str(99) +  ' burritos.'    #strong typing concept

