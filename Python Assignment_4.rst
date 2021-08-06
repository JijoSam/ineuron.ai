1. What exactly is []?
======================

[] is an empty list.

2. In a list of values stored in a variable called spam, how would you assign the value ‘hello’ as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
==========================================================================================================================================================

.. code:: ipython3

    spam = [2, 4, 6, 8, 10]
    
    spam.insert(2,'hello')
    
    print(list(spam))


.. parsed-literal::

    [2, 4, 'hello', 6, 8, 10]
    

3.What is the value of spam[int(int(‘3’ \* 2) / 11)]?
=====================================================

.. code:: ipython3

    spam= [int(int('3' * 2) / 11)]
    spam




.. parsed-literal::

    [3]



4. What is the value of spam[-1]?
=================================

.. code:: ipython3

    spam= ['a','b','c','d]
    spam[-1]




.. parsed-literal::

    'd'



5. What is the value of spam[:2]?
=================================

.. code:: ipython3

    spam= ['a','b','c','d']
    spam[:2]




.. parsed-literal::

    ['a', 'b']



6. What is the value of bacon.index(‘cat’)?
===========================================

Let's pretend bacon has the list [3.14, ‘cat’, 11, ‘cat’, True] for the
next three questions.

.. code:: ipython3

    bacon = [3.14, 'cat', 11, 'cat', True]
    
    bacon.index('cat')




.. parsed-literal::

    1



7. How does bacon.append(99) change the look of the list value in bacon?
========================================================================

.. code:: ipython3

    bacon = [3.14, 'cat', 11, 'cat', True]
    
    bacon.append(99)
    
    bacon




.. parsed-literal::

    [3.14, 'cat', 11, 'cat', True, 99]



8. How does bacon.remove(‘cat’) change the look of the list in bacon?
=====================================================================

.. code:: ipython3

    bacon = [3.14, 'cat', 11, 'cat', True]
    
    bacon.remove('cat')
    
    bacon




.. parsed-literal::

    [3.14, 11, 'cat', True]



9. What are the list concatenation and list replication operators?
==================================================================

The operator for list concatenation is +, while the operator for
replication is \*. (This is the same as for strings.)

10. What is difference between the list methods append() and insert()?
======================================================================

The difference is that with append, you just add a new entry at the end
of the list. With insert(position, new_entry) you can create a new entry
exactly in the position you want. The append method adds a new item to
the end of a list.

11. What are the two methods for removing items from a list?
============================================================

There are three ways in which you can Remove items from List:

a) Using the remove() method. —> remove , removes the first matching
   value, not a specific index:

b) Using the list object’s pop() method. —> pop removes the item at a
   specific index and returns it.

c) Using the del operator. —> del, removes the item at a specific index:

12. Describe how list values and string values are identical.
=============================================================

The values that make up a list are called its elements. Lists are
similar to strings, which are ordered collections of characters, except
that the elements of a list can have any type and for any one list, the
items can be of different types

One simple difference between strings and lists is that lists can any
type of data i.e. integers, characters, strings etc, while strings can
only hold a set of characters.

13. What's the difference between tuples and lists?
===================================================

Tuple is also a sequence data type that can contain elements of
different data types, but these are immutable in nature. In other words,
a tuple is a collection of Python objects separated by commas

14. How do you type a tuple value that only contains the integer 42?
====================================================================

.. code:: ipython3

    this_tuple = (42,)
    print (this_tuple)


.. parsed-literal::

    (42,)
    

15. How do you get a list value's tuple form? How do you get a tuple value's list form?
=======================================================================================

List comprehension along with zip() function is used to convert the
tuples to list and create a list of tuples. Python iter() function is
used to iterate an element of an object at a time. The ‘number’ would
specify the number of elements to be clubbed into a single tuple to form
a list.

16.Variables that “contain” list values are not necessarily lists themselves. Instead, what do they contain?
============================================================================================================

Variables will contain references to list values rather than list values
themselves. But for strings and integer values, variables simply contain
the string or integer value. Python uses references whenever variables
must store values of mutable data types, such as lists or dictionaries.

17. How do you distinguish between copy.copy() and copy.deepcopy()?
===================================================================

A shallow copy constructs a new compound object and then (to the extent
possible) inserts references into it to the objects found in the
original.

A deep copy constructs a new compound object and then, recursively,
inserts copies into it of the objects found in the original.
