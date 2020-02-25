# os_exercise.py
# Do the following task using the os module

#1. create a folder and name the folder 'os_exercises.'                                                  
#2. In that folder create a file. Name the file 'exercise.py'                                                                            
#3. get input from the console and write it to the file.                                                 
#4. repeat step 2 and 3 (name the file something else).                                                  
#5. read the content of the files and and print to console the content of the file with the largest amount of unique words.



# import the os module
import os

# detect the current working directory and print it
#path = os.getcwd()
#print ("The current working directory is %s" % path)

#os.makedirs("code_from_today/tuesday/os_exercises")


for i in range(1,4):

    t = input('Please write some code')
    f = open(f"exercise_{i}.py", "w")
    
    f.write(t)                   # writing to the file
    f.close()                    # closing the file - mandatory 


for i in range(1,4):    # opnening the file again
    f = open(f'exercise_{i}.py')
    t = f.read()
    t = t.split()    # splint on blank spaces 
    s = set(t)      # making t a set
    unique_words = len(s)
    print(unique_words)


    # another way : print(len(set(open(f'exercise_{i}.py'.read().spit())))
    




