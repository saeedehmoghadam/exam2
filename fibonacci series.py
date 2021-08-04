import math

x = int(input("please type the number : "))

l = []

for i in range (x):

       if i==0 or i==1 :
           l.append(1)

       else :

           fibonacci= l[i - 1] + l[i - 2 ]
           l.append(fibonacci) 

print(l)


       

