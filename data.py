from pickle import load,dump
def file_read(file_name):
    file=open(file_name+'.txt','rb')
    while True:
        try:
            d=load(file)
            if file_name.name in d:
                return d[file_name.name]
        except:
            return []
        
file=open('bill.bin','rb')
a=load(file)
print(a)
file.close()

file=open('bill.bin','wb')
dump({'2': [['Puttu', '2']]},file)
file.close()