#to explore your current working directory. You can also do this natively in Python using the library os, which consists of miscellaneous operating system interfaces.
#The first line of the following code imports the library os, the second line stores the name of the current directory in a string called wd and the third outputs the contents of the directory in a list to the shell.

import os
wd = os.getcwd()
os.listdir(wd)