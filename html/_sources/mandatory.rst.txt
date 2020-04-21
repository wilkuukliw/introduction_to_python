.. _mandatory:

Mandatory assignments
=====================

**1 Mandatory assignment that count as 2**

You should make and show (in class or to Claus) an exam presentation of your own choise.

* Hand in on fronter
* Show in class


.. todo::
   
   dictcomp
   Create a dictcomp with all unique words from the file sample.txt as keys and the count of every word as values. This is equevalent to the exercise you did in week 8, but now done with by th euse of a dict comp.

   List comp
   Create a listcomp that produces a list of Card objects containing all card in a deck. When printing out the list you should see the following.

   ['A♠', 'K♣', ... ] etc.


   @properties
   Create the library code for this client code output. As it is now, it is not pythonic. Some parts of the code would reveal that it is a Java programmer that have written the code. When you create the library code you should fix these mistakes and make it pythonic. This assignment is partly to test if you can read the error msg, and understand analyse the interpreter commands and make client code out of it. 

   >>> bar = Bar()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>  
   TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
   Traceback (most recent call last):
   Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    File "property_client.py", line 5, in __init__
      self.set_x(x)
    File "property_client.py", line 29, in set_x
      raise TypeError('x has to be an "int"')
    TypeError: x has to be an "int"
    >>> bar = Bar(12, 'There')
    >>> bar.y = 123
    >>> bar.set_x(1024)
    >>> bar.get_x()
    1024

    Arithmetic
    Create a program that reads two integers, 𝑎 and 𝑏, from the user. Your program should compute and display:
    The sum of 𝑎 and 𝑏
    The difference when 𝑏 is subtracted from 𝑎
    The product of 𝑎 and 𝑏
    The quotient when 𝑎 is divided by 𝑏
    The remainder when 𝑎 is divided by 𝑏
    The result of log10𝑎
    The result of 𝑎𝑏

    Height Units
    Many people think about their height in feet and inches, even in some countries that primarily use the metric system. Write a program that reads a number of feet from the user, followed by a number of inches. Once these values are read, your program should compute and display the equivalent number of centimeters.

    Hint: One foot is 12 inches. One inch is 2.54 centimeters. 


    Making Change
    Consider the software that runs on a self-checkout machine. One task that it must be able to perform is to determine how much change to provide when the shopper pays for a purchase with cash.

    Write a program that begins by reading a number of cents from the user as an integer. Then your program should compute and display the denominations of the coins that should be used to give that amount of change to the shopper. The change should be given using as few coins as possible. Assume that the machine is loaded with pennies, nickels, dimes, quarters, loonies and toonies.

    A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie because one side of the coin has a loon (a type of bird) on it. The two dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is derived from the combination of the number two and the name of the loonie. 


    Distance from upper corner to lower corner
    Write a program that take the height, length and depth of a room as input.
    The program should calculate



    Sort 3 Integers
    Create a program that reads three integers from the user and displays them in sorted order (from smallest to largest).
   You are NOT allowed to use any kind of sequenced datastructure (list, set etc.) and you are not allowed to import any modules.  


