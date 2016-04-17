from math import *
def makesin():
    for i in range(90):
        yield sin(radians(i))
k = "["+",".join(list(str(i) for i in makesin()))+"]"
file=open("a.txt","w")
file.write(k)
file.close()
