import pickle
#Importing necessary modules
from datetime import datetime
import os
from pickle import load,dump
from menu import *

#To find whether teh preference to be given to the order or not
def timediff(a,b):
    c = datetime.strptime(a, "%H:%M:%S")
    d = datetime.strptime(b, "%H:%M:%S")
    difference = c - d
    seconds = difference.total_seconds()    
    minutes = seconds / 60
    if minutes <2:
        return True
    return False


def order_list(time=None):
    
    result={}  # name key and value list of [ availability_qty , price]
    with open('menu.bin','rb') as f:
        ll=pickle.load(f)
        ll=ll[0]
        ll=ll.menu_items
    b=[]
    l=[]
    d=[]
    for i in ll:
        if i.tag=='b':
            b.append(i)
        elif i.tag=='l':
            l.append(i)
        elif i.tag=='d':
            d.append(i)
    if time in range(0,12):
        lst=b
    elif time in range(12,18):
        lst=l
    elif time in range(18,24):
        lst=d
    for i in lst:
        result[i.name]=[i.availability,i.price,i.tag]
    
    return result

def day_order_list():
    result={}
    with open('menuoftheday.bin','rb') as f:
        ll=pickle.load(f)
        ll=ll[0]
        ll=ll.get_menu()
    result[ll.name]=[ll.availability,ll.price,ll.tag]
    return result

