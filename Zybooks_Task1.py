
mydict = {'i':'!', 'a':'@', 'm':'M', 'B':'8','o':'.'}

val = input()
mylist = []

for char in val:
    if char in mydict:
        mylist.append(mydict[char])
    else:
        mylist.append(char)

mylist.append('q*s')
val = ''.join([word for word in mylist])

print(val)