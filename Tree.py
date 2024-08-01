from tkinter import *
from tkinter import ttk
from tkinter import font

class Tree:

    def __init__(self,window,row=2,column=2):

        self.window=window
        self.row=row
        self.col=column
        self._tree = ttk.Treeview(window, column=['c{}'.format(i+1) for i in range(column)],show='headings', height=row)
        style=ttk.Style()
        style.theme_use('default')
        style.configure("Treeview.Heading", font=font.Font(family='Ailza Bright Demo',weight='bold',size=25,underline=1))
        style.configure("Treeview", font=font.Font(family='Ailza Bright Demo',weight='bold',size=25,underline=1))
        style.configure('Treeview',
                        background='white',
                        foreground='black',
                        fieldbackground='white'
                        )
        style.map('Treeview',background=[('selected','grey')])
        self._tree.tag_configure('oddrow',background='white')
        self._tree.tag_configure('evenrow',background='light blue')

        self._rowcount=0
        self._colcount=0

    def delete(self):
        for i in self._tree.get_children():
            self._tree.delete(i)
        self._colcount=0
        
        
    def create_heading(self,seq : isinstance(str ,int)):
        self._tree.column("#{}".format(self._rowcount+1), width=110,anchor=CENTER) 
        self._tree.heading("#{}".format(self._rowcount+1), text="{}".format(seq))
        self._rowcount+=1

    def create_headings(self,seq : isinstance(list,tuple)):
        for i in range(len(seq)):
            self._tree.column("#{}".format(self._rowcount+1), width=110,anchor=CENTER)
            self._tree.heading("#{}".format(self._rowcount+1), text="{}".format(seq[i]))
            self._rowcount+=1

    def add_data(self,data):
        if self._colcount%2==0:
            self._tree.insert('','end',text='{}'.format(self._colcount+1),values=data,tags=('evenrow',))
        else:
            self._tree.insert('','end',text='{}'.format(self._colcount+1),values=data,tags=('oddrow',))
        self._colcount+=1

    def get_tree(self):
        return self._tree
                
    def add_datas(self,datas):
        for i in range(len(datas)):
            if self._colcount%2==0:
                self._tree.insert('','end',text='{}'.format(self._colcount+1),values=datas[i],tags=('evenrow',))
            else:
                self._tree.insert('','end',text='{}'.format(self._colcount+1),values=datas[i],tags=('oddrow',))
            self._colcount+=1
        
