import os
import time
print ("                   0%")
time.sleep(1)
print ("=====              25%")
time.sleep(2)
print ("=========          50%")
time.sleep(3)
print ("===============    75%")
time.sleep(4)
print ("===================100%")
os.system("clear")#or win cls
red = '\033[1;31m' 
f = open("data.txt" , "a")
print("if press 1 Run")
print("if press 2 Save data\n")
while 1:
    bs = input(red+"Enter<<")
    if bs == "1":
       for x in range(1):
          i = input("Name of a person + number: ")
          f.write("\n"+">>>name "+i+">>>number")
    elif bs == "2":
              time.sleep(2)
              print("Done Save!!")
              exit()
f.close()