from math import *
def makesin():
    for i in range(360):
        yield sin(radians(i))
k = "sinList=["+",".join(list(str(i) for i in makesin()))+"]"
file=open("a.txt","w")
file.write(k)
file.close()
