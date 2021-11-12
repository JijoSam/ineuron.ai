#!/usr/bin/env python
# coding: utf-8

# # 1. What does an empty dictionary's code look like?

# In[ ]:


like an empty curly braces{}


# # 2. What is the value of a dictionary value with the key 'foo'; and the value 42?

# In[4]:


dict = {'foo': 42}


# In[8]:


dict ['foo']


# # 3. What is the most significant distinction between a dictionary and a list?

# In[ ]:


A list is an ordered sequence of objects, whereas dictionaries are unordered sets. 
However, the main difference is that items in dictionaries are accessed via keys and not via their position


# # 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# In[10]:


spam = {'bar': 100}


# In[12]:


spam['foo']  #we get KeyError error.


# # 5 and 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# In[ ]:


There is no difference. The in operator checks whether a value exists as a key in the dictionary.


# # 7. What is a shortcut for the following code?
# if 'color' not in spam:
# 
# spam['color'] = 'black'

# In[ ]:


spam.setdefault('color', 'black')


# # 8. How do you 'pretty print' dictionary values using which module and function?

# In[ ]:


pprint.pprint()

