1. Why are functions advantageous to have in your programs?
===========================================================

Functions reduce the need for duplicate code. This makes programs
shorter, easier to read, and easier to update. A function call is what
moves the program execution into the function, and the function call
evaluates to the function’s return value.

2. When does the code in a function run: when it’s specified or when it’s called?
=================================================================================

The code inside a function is executed when the function is called

3. What statement creates a function?
=====================================

The “def” keyword is a statement for defining a function in Python. You
start a function with the def keyword, specify a name followed by a
colon (:) sign. The “def” call creates the function object and assigns
it to the name given. You can further re-assign the same function object
to other names.

4. What is the difference between a function and a function call?
=================================================================

Using a function to do a particular task any point in program is called
as function call. So the difference between the function and function
call is, A function is procedure to achieve a particular result while
function call is using this function to achive that task

5. How many global scopes are there in a Python program? How many local scopes?
===============================================================================

When you use an unqualified name inside a function, Python searches
three scopes—the local (L), then the global (G), and then the built-in
(B)—and stops at the first place the name is found

6. What happens to variables in a local scope when the function call returns?
=============================================================================

let say the variable y only exists while the function is being executed
— we call this its lifetime. When the execution of the function
terminates (returns), the local variables are destroyed

7. What is the concept of a return value? Is it possible to have a return value in an expression?
=================================================================================================

A return is a value that a function returns to the calling script or
function when it completes its task. A return value can be any one of
the four variable types: handle, integer, object, or string. The type of
value your function returns depends largely on the task it performs.

A return statement is used to end the execution of the function call and
“returns” the result (value of the expression following the return
keyword) to the caller. … If the return statement is without any
expression, then the special value None is returned. Note: Return
statement can not be used outside the function

8. If a function does not have a return statement, what is the return value of a call to that function?
=======================================================================================================

If there is no return statement in the function code, the function ends,
when the control flow reaches the end of the function body and the value
None will be returned.

9. How do you make a function variable refer to the global variable?
====================================================================

If you want to refer to a global variable in a function, you can use the
global keyword to declare which variables are global.

10. What is the data type of None?
==================================

None is used to define a null value. It is not the same as an empty
string, False, or a zero. It is a data type of the class NoneType
object. Assigning a value of None to a variable is one way to reset it
to its original, empty state.

11. What does the sentence import areallyourpetsnamederic do?
=============================================================

.. code:: ipython3

    #import is used to call the module
    import.areallyourpetsnamederic()
    


::


      File "<ipython-input-9-bea236f84247>", line 1
        import.areallyourpetsnamederic()
              ^
    SyntaxError: invalid syntax
    


12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
===============================================================================================

spam.bacon()

13. What can you do to save a programme from crashing if it encounters an error?
================================================================================

Prevents program from crashing if an error occurs. If an error occurs in
a program, we don’t want the program to unexpectedly crash on the user.
Instead, error handling can be used to notify the user of why the error
occurred and gracefully exit the process that caused the error

14. What is the purpose of the try clause? What is the purpose of the except clause?
====================================================================================

The try block is used to check some code for errors i.e the code inside
the try block will execute when there is no error in the program.
Whereas the code inside the except block will execute whenever the
program encounters some error in the preceding try block.
