# Mac Python Alias

> In order to type ```python``` instead of ```python3``` every time you want to run a python script from the commandline you will need to do the following

## Open your .bash_profile file

````
    cd  
    open .bash_profile
````

## Or open your .zshrc file
````
    cd  
    open .zshrc
````
If these file do not exist, create them in your root directory.  

## Copy / paste this into the file:
````
    alias python='python3'
    alias pip='pip3'
````

Save the file and exit.
Close and open your terminal.
Type

````
python --version
python 3.7.2
````

&copy; clbo@kea.dk 04-02-2019
