from pickle import load,dump
from menu import *

# file=open('menu.bin','rb')

# d=load(file)[0]
# print(type(d.menu_items))
# for i in d.menu_items:
#     print(i)
#     print(i.name,i.tag,i.price,i.availability)

# file.close()

# file=open('menu.bin','wb')
# dump(d,file)
# file.close()

# file=open('menuoftheday.bin','rb')

# d=load(file)[0]
# i=d.get_menu()
# print(i.name,i.availability,i.tag)

# file.close()

# file=open('pending.bin','rb')
# d=load(file)
# for i in d:
#     print(i.token_)
#     for j in i.order_list:
#         print(j[0].name,j[1])
# file.close()


# with open('bill.bin','rb') as file:
#     req_list=[]
#     d=load(file)
#     print(d)
