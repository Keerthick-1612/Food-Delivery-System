from pickle import load,dump

file=open('food.bin','wb')
file1=open('breakfast.txt')
list1=file1.readlines()
d={}
for i in list1:
    if 'breakfast' not in d:
        d['breakfast']=[i]
    else:
        d['breakfast'].append(i)
dump(d,file)
file1.close()

file1=open('lunch.txt')

list1=file1.readlines()
d={}
for i in list1:
    if 'breakfast' not in d:
        d['breakfast']=[i]
    else:
        d['breakfast'].append(i)
dump(d,file)
file1.close()

file1=open('dinner.txt')

list1=file1.readlines()
d={}
for i in list1:
    if 'breakfast' not in d:
        d['breakfast']=[i]
    else:
        d['breakfast'].append(i)
dump(d,file)
file1.close()

file.close()
