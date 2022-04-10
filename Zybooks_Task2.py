
xcoef1 = int(input())
ycoef1 = int(input())
const1 = int(input())

xcoef2 = int(input())
ycoef2 = int(input())
const2 = int(input())

mylist = []
for x in range(-10, 11):
   for y in range(-10,11):
      if (x*xcoef1 + y*ycoef1 == const1) and (x*xcoef2 + y*ycoef2 == const2):
         mylist.append(x)
         mylist.append(y)

if len(mylist)>0:
   print(f'{mylist[0]} {mylist[1]}')
else:
   print('No solution')