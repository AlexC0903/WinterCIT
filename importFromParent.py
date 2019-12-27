
import sys
sys.path.insert(0, sys.path[0].split("\path\from\the\most\parent\folder\to\current\folder")[0])

# sys.path : all path python interpreter looks for code, variable which contains array
# sys.path.insert(0, element) : inserts element at index 0 of original array
# * if you use append instead, new element will be the last element, and might cause issue if there is another file in another path with same name
# sys.path[0] : current directory
# split :  splits string and returns array with string fragments


import par2.c


par2.c.cc()
