# Virtual Enviroment Setup

This document contains notes about how to setup a virtual enviroment on Windows and Mac (Unix based systems).  

For a more deep description read the following on Python docs.  

* [12. Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

## Windows

Creating a virtual enviroment called **tutorial-env**

````
    python -m venv tutorial-env
````
Activating the enviroment

**cmd**

````
    C:\> tutorial-env\Scripts\activate.bat
````
**Git Bash**
````
   source tutorial-env/Scripts/activate
````


**Power shell**  
_This is by default not possible_

## Mac

Creating a virtual enviroment called **tutorial-env**
````
    python -m venv tutorial-env
````
Activating the enviroment
````
    source tutorial-env/bin/activate
````

