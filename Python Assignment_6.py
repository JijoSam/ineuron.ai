#!/usr/bin/env python
# coding: utf-8

# # 1. What are escape characters, and how do you use them?

# In[ ]:


To insert characters that are illegal in a string, use an escape character. 
An escape character is a backslash \ followed by the character you want to insert.


# In[2]:


sentence = "This is \"Jijo Sam\" assignment"


# In[3]:


sentence


# # 2. What do the escape characters n and t stand for?

# In[9]:


'''''
\n	New Line  
\t	Tab
'''''
txt1 = "Hello\nWorld!"
print(txt1) 

print("\n")

txt2 = "Hello\tWorld!"
print(txt2) 


# # 3. What is the way to include backslash characters in a string?

# In[ ]:


To insert characters that are illegal in a string, use an escape character. 
An escape character is a backslash \ followed by the character you want to insert.  #----> refer Answer 1


# # 4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# In[11]:


string = "Howl's Moving Castle"


# In[13]:


string


# In[ ]:


Strings can begin and end with double quotes, just as they do with single quotes. 
One benefit of using double quotes is that the string can have a single quote character in it. 
Since the string begins with a double quote, 
Python knows that the single quote is part of the string and not marking the end of the string. 
   
    However, if you need to use both single quotes and double quotes in the string, 
    you’ll need to use escape characters.,
    Python knows that since the single quote in Howl\'s has a backslash, 
    it is not a single quote meant to end the string value.
    The escape characters \' and \" let you put single quotes and double quotes inside your strings, respectively.


# # 5. How do you write a string of newlines if you don't want to use the n character?

# In[18]:


print ("hello",end = "  ")
print ("Jijo", end="")


# # 6. What are the values of the given expressions?
# 
# 'Hello, world'[1]
# 
# 'Hello, world'[0:5]
# 
# 'Hello, world'[:5]
# 
# 'Hello, world'[3:]

# In[22]:


print('Hello, world'[1])

print('Hello, world'[0:5])

print('Hello, world'[:5])

print('Hello, world'[3:])


# # 7. What are the values of the following expressions?
# 
# 'Hello.upper()
# 
# 'Hell,.upper().isupper()
# 
# 'Hello.upper().lower()

# In[7]:


print('Hello'.upper())

print('Hello'.upper().isupper())

print('Hello'.upper().lower())


# # 8. What are the values of the following expressions?
# 
# 'Remember, remember, the fifth of July.'.split()
# 
# '-'.join('There can only one.'.split())
# 

# In[26]:


print('Remember, remember, the fifth of July.'.split())

print('-'.join('There can only one.'.split()))


# # 9. What are the methods for right-justifying, left-justifying, and centering a string?

# In[28]:


string1 = "This is Centre"
  
print (string1.center(40), "\n")

  
string2 = "This is left"
print (string2.ljust(40), "\n")


string3 = "This is right"
print (string3.rjust(40), "\n")


# # 10. What is the best way to remove whitespace characters from the start or end?

# In[ ]:


To remove whitespace characters from the beginning or from the end of a string only, you use the trimStart() or trimEnd() method

