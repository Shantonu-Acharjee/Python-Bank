import os
import random
photoList = os.listdir('Photo/')

a = 0
b = 10
c = []


while True:
    
    n = random.randint(1,len(photoList))
    randomPhoto = photoList[n-1]
    
    if randomPhoto in c:
        continue
    
    c.append(randomPhoto)
    a = a+1
    if(a == b):
        break

print(c)