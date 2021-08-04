1.What are the two values of the Boolean data type? How do you write them?
==========================================================================

.. code:: ipython3

    #There are only two boolean values. They are True and False . They start with caps and rest in lower case
    
    #example: 
    
    type(True)




.. parsed-literal::

    bool



2. What are the three different types of Boolean operators?
===========================================================

.. code:: ipython3

    The three basic boolean operators are: AND, OR, and NOT

3.Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
================================================================================================================================================

.. code:: ipython3

    True and True is True.
    True and False is False.
    False and True is False.
    False and False is False.
    
    True or True is True.
    True or False is True.
    False or True is True.
    False or False is False.
    
    not True is False.
    not False is True.

4. What are the values of the following expressions?
====================================================

(5> 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)

.. code:: ipython3

    x = (5> 4) and (3 == 5)
    
    y = not (5 > 4)
    
    z = (5 > 4) or (3 == 5)
    
    a = not ((5 > 4) or (3 == 5))
    
    b = (True and True) and (True == False)
    
    c = (not False) or (not True)
    
    print(x,y,z,a,b,c)


.. parsed-literal::

    False False True False False True
    

5. What are the six comparison operators?
=========================================

.. code:: ipython3

    There are six main comparison operators: 
        
    equal to (=), 
    not equal to (!=), 
    greater than (>), 
    greater than or equal to (>=), 
    less than (<), 
    less than or equal to (<=).

6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
================================================================================================================================

.. code:: ipython3

    Assignment Operator (=) :  assigns the value of right side expression’s or variable’s value to the left side variable.
        
    Equal To Operator (==): compares value of left and side expressions, return 1 if they are equal other will it will return 0.

.. code:: ipython3

    x = 2
    y = 3
    
    print(x,y)      # here 2 is assigned to x and 3 is assigned to y thus its a Assignment Operator (=)
    print(x==y)     # here the operator compares if the both values are similar or equal. In this case its false


.. parsed-literal::

    2 3
    False
    

7. Identify the three blocks in this code:
==========================================

spam = 0

if spam == 10:

print(‘eggs’)

if spam > 5:

print(‘bacon’)

else:

print(‘ham’)

print(‘spam’)

print(‘spam’)

.. code:: ipython3

    spam = 0
    
    if spam == 10:
        print('eggs')
    
    if spam > 5:
        print('bacon')
    
    else:
        print('ham')
        print('spam')
        print('spam')


.. parsed-literal::

    ham
    spam
    spam
    

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
======================================================================================================================================================

.. code:: ipython3

    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')   


.. parsed-literal::

    Greetings!
    

9.If your programme is stuck in an endless loop, what keys you’ll press?
========================================================================

.. code:: ipython3

    Control + C  or
    kernel restart or
    adding break command

10. How can you tell the difference between break and continue?
===============================================================

.. code:: ipython3

    
    Break leaves the loop completely and executes the statements after the loop. Whereas Continue leaves the current iteration and executes with the next value in the loop. break completely exits the loop. continue skips the statements after the continue statement and keeps looping.

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
=================================================================================================

.. code:: ipython3

    #They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0,10) explicitly tells the loop to start at 0 , and range (0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration.
    
    range(10)




.. parsed-literal::

    range(0, 10)



.. code:: ipython3

    range(0, 10)




.. parsed-literal::

    range(0, 10)



.. code:: ipython3

    range(0, 10, 1)




.. parsed-literal::

    range(0, 10)



12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
================================================================================================================================================================

.. code:: ipython3

    for i in range(1,11):
        print(i)


.. parsed-literal::

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

.. code:: ipython3

    notes = 10
    
    i=1
    
    while i <= notes:
        print(i)
        i+=1


.. parsed-literal::

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
===============================================================================================================

.. code:: ipython3

    This function can be called with spam.bacon()
