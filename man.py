from tkinter import *
from PIL  import ImageTk,Image
from tkinter import font
from tkinter import ttk
from datetime import datetime
from Tree import Tree
from order import *
from order import *
from tkinter.messagebox import *
from menu import *

wind=Tk()
wind.geometry(f'750x550+{350}+{100}')
wind.resizable(False,False)
wind.iconbitmap('icon.ico')
wind.title('Apollo Sindoori')
can=Canvas(wind,width=750,height=550)
can.pack()
img=Image.open('main1.jpg')
resized=img.resize((750,550))
final_img=ImageTk.PhotoImage(resized)
can.create_image(0,0,image=final_img,anchor='nw')




def menu_display():
    
    def table(food):
        req_data=mechanism.retrieve_data(food[0])

        bill.delete()
        if (req_data is None):
            pass
        elif  len(req_data)>=4 :
            bill.get_tree().config(height=4)
            bill.add_datas(req_data)
        else:
            bill.get_tree().config(height=len(req_data))
            bill.add_datas(req_data)
        
        can1.create_window(150,150,window=bill.get_tree(),anchor='nw')

    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)
    breakfast=Button(wind,text='Breakfast',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:table('breakfast'))
    lunch=Button(wind,text='Lunch',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:table('lunch'))
    dinner=Button(wind,text='Dinner',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:table('dinner'))
    menu_of_the_day=Button(wind,text='Menu of\nthe day',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:table('menu') )
    bill=Tree(wind)
    bill.get_tree().config(column=['c{}'.format(i+1) for i in range(3)],show='headings')
    bill.create_headings(['Food Items','Available Qty.','Cost/no'])
    back=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=lambda:can1.destroy())
    can1.create_window(265,290,window=back,anchor='nw')
    can1.create_window(10,50,window=breakfast,anchor='nw')
    can1.create_window(180,50,window=lunch,anchor='nw')
    can1.create_window(350,50,window=dinner,anchor='nw')
    can1.create_window(520,50,window=menu_of_the_day,anchor='nw')

def menu_update():

    def common(action):
        com_can.delete(ALL)

        can1.create_window(5,110,window=com_can,anchor='nw')
        com_can.create_image(0,0,image=final_img,anchor='nw')
  
        def add(time):

            if action=='add':

                def add_details():
                    if time in ['lunch','breakfast','dinner']:
                        mechanism.additem([item.get(),int(quty.get()),float(cost.get())],code.get())
                    elif time in ['mod']:
                        mechanism.additem([item.get(),int(quty.get()),float(cost.get())],'mod')
                    showinfo('Adding Items','Food item is added successfully')
                    code.delete(0,END)
                    item.delete(0,END)
                    quty.delete(0,END)
                    cost.delete(0,END)
                
                com_can.create_text(220,70,text='Enter the tag: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
                com_can.create_text(220,110,text='Enter the name: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
                com_can.create_text(230,150,text='Enter the quantity: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
                com_can.create_text(230,190,text='Enter the cost/no: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')

                code=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                item=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                quty=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                cost=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                
                com_can.create_window(310,50,window=code,anchor='nw')
                com_can.create_window(310,90,window=item,anchor='nw')
                com_can.create_window(310,130,window=quty,anchor='nw')
                com_can.create_window(310,170,window=cost,anchor='nw')

                add_detail=Button(wind,text='Add Details',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='Light Green',foreground='white',command=add_details)
                com_can.create_window(450,170,window=add_detail,anchor='nw')
                
            elif action=='delete':
                def delete_action():
                    response=askokcancel('Delete Item','Do you want to delete it?')
                    if response==1:
                        for selected_item in table.selection():
                            
                            item = table.item(selected_item)
                            record = item['values']
                            table.delete(selected_item)
                            table.configure(height=table['height']-1)
                            print('Record',record[0])
                            if time in ['lunch','breakfast','dinner']:
                                mechanism.delitem(record[0])
                            elif time in ['mod']:
                                mechanism.del_mod()
                            
                req_data=mechanism.retrieve_data(time[0])
                bill.delete()
                if len(req_data)>=4:
                    bill.get_tree().config(height=4)
                else:
                    bill.get_tree().config(height=len(req_data))
                bill.add_datas(req_data)
                    
                    
                table=bill.get_tree()
                com_can.create_window(170,30,window=table,anchor='nw')
                com_can.create_text(290,210,text='Please select one to delete',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),fill='navyblue')
                delete_button=Button(wind,text='Delete',state=DISABLED,width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=delete_action)
                com_can.create_window(420,190,window=delete_button,anchor='nw')
                table.bind('<<TreeviewSelect>>',lambda e: delete_button.configure(state=NORMAL))
                
            elif action=='update':   
                    
                def update_action():
                    
                    def update1():
                        response=askokcancel('Update Item','Do you want to update it?')
                        if response==1:
                            item.config(state=NORMAL)     
                            food=item.get()
                            if time in ['lunch','breakfast','dinner']:
                                mechanism.updateitem(food,float(quty.get()),float(cost.get()))
                            elif time in ['mod']:
                                 mechanism.update_mod(food,float(quty.get()),float(cost.get()))
                                

                    
                    can2=Canvas(wind,bg='white',width=430,height=230)
                    com_can.create_window(150,10,window=can2,anchor='nw')
                    data=table.item(table.selection())['values']
                    
                    
                    can2.create_text(190,30,text='Update',font=font.Font(family='Ailza Bright Demo',weight='bold',underline=1,size=15),fill='navyblue')
                    can2.create_text(120,90,text='Name: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
                    can2.create_text(120,130,text='Quantity: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')
                    can2.create_text(120,170,text='Cost/no: ',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fill='navyblue')

                    item=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                    quty=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                    cost=Entry(wind,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
                    upd_button=Button(wind,text='Update',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                                      background='DodgerBlue3',foreground='white',command=update1)
                    back_button=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),
                                       background='DodgerBlue3',foreground='white',command=lambda: can2.destroy())
                    
                    item.insert(0,data[0])
                    item.config(state=DISABLED)
                    quty.insert(0,data[1])
                    cost.insert(0,data[2])
                    
                    can2.create_window(200,70,window=item,anchor='nw')
                    can2.create_window(200,110,window=quty,anchor='nw')
                    can2.create_window(200,150,window=cost,anchor='nw')
                    can2.create_window(250,190,window=upd_button,anchor='nw')
                    can2.create_window(80,190,window=back_button,anchor='nw')
                
                req_data=mechanism.retrieve_data(time[0])
                bill.delete()
                if len(req_data)>=4:
                    bill.get_tree().config(height=4)
                else:
                    bill.get_tree().config(height=len(req_data))
                bill.add_datas(req_data)
                table=bill.get_tree()
                com_can.create_window(170,30,window=table,anchor='nw')
                com_can.create_text(290,210,text='Please select one to update',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),fill='navyblue')
                update_button=Button(wind,text='Update',state=DISABLED,width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=update_action)
                com_can.create_window(420,190,window=update_button,anchor='nw')
                table.bind('<<TreeviewSelect>>',lambda e: update_button.configure(state=NORMAL))
                
        breakfast=Button(wind,text='Breakfast',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:add('breakfast'))
        lunch=Button(wind,text='Lunch',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:add('lunch'))
        dinner=Button(wind,text='Dinner',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:add('dinner'))
        menu_of_the_day=Button(wind,text='menu_of_the_day',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:add('mod') )
        
        can1.create_window(10,130,window=breakfast,anchor='nw')
        can1.create_window(10,190,window=lunch,anchor='nw')
        can1.create_window(10,250,window=dinner,anchor='nw')
        can1.create_window(10,310,window=menu_of_the_day,anchor='nw')
        
        
    
    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)
    can_img=Image.open('update.jpg')
    resize_can=can_img.resize((610,250))
    final_img=ImageTk.PhotoImage(resize_can)
    com_can=Canvas(width=610,height=250)
    com_can.final_img=final_img
    
    add_item=Button(wind,text='Add Item',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:common('add'))
    delete_item=Button(wind,text='Delete Item',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:common('delete'))
    update_item=Button(wind,text='Update Item',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda:common('update'))
    back=Button(wind,text='Back',width=10,bd=0,relief=FLAT,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=lambda: can1.destroy())
    bill=Tree(wind)
    
    bill.get_tree().config(column=['c{}'.format(i+1) for i in range(3)],show='headings')
    bill.create_headings(['Food Items','Available Qty.','Cost/no'])
    can1.create_window(10,50,window=add_item,anchor='nw')
    can1.create_window(180,50,window=delete_item,anchor='nw')
    can1.create_window(350,50,window=update_item,anchor='nw')
    can1.create_window(520,50,window=back,anchor='nw')
    return

def pending_order():
    '''import pendingorder'''
    def get_details():
        global tree2,require
        value=table.item(table.selection())['values']
        order_no=value[0]
        file1=open('pending.bin','rb')
        read=load(file1) 
        file1.close()
        food=[]
        for i in read:
            if i.token_no==order_no:
                for j in i.order_list:
                    food.append([j[0].name,j[1]])
        print(food)
        if len(food)<3:
            tree2=Tree(wind,len(food),2)
        else:
            tree2=Tree(wind,3,2)
        tree2.create_headings(['Food Item','Quantity'])
        tree2.add_datas(food)
        can1.create_window(110,240,window=tree2.get_tree(),anchor='nw')
    
    def delete_order():
        try: 
            tree2.get_tree().destroy()
        except:
            pass
        value=table.item(table.selection())['values']
        tree.get_tree().delete(tree.get_tree().selection())
        order_no=value[0]
        Pending_order().remove(order_no)
        


    file1=open('pending.bin','rb')
    read=load(file1) 
    file1.close()
    token=[]
    food={}
    for i in read:
        food[i.name]=[]
        token.append(i.token_no)
        for j in i.order_list:
            food[i.name].append([j[0].name,j[1]])

    
    can1 =Canvas(wind,bg='white',width=650,height=370)
    can.create_window(40,155,anchor='nw',window=can1)
    img1=Image.open('update.jpg')
    resise=img1.resize((650,370))
    res_img1=ImageTk.PhotoImage(resise)
    can1.res_img1=res_img1
    can1.create_image(0,0,anchor='nw',image=res_img1)
    back_button=Button(wind,text='Back',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=lambda: can1.destroy())
    can1.create_window(470,320,window=back_button,anchor='nw')
    if len(read)==0:
        can1.create_text(340,175,text='No Orders',font=font.Font(family='Ailza Bright Demo',underline=1,size=18,weight='bold'),fill='navyblue')
        return
    if len(read)>3:
        tree=Tree(wind,2,1)
    else:
        tree=Tree(wind,len(read),1)
    req_datas=[]
    for i in range(len(token)):
        req_datas.append([token[i]])
    print(req_datas)
    print(food)
    tree.create_headings(['Token No.'])
    tree.add_datas(req_datas)
    table=tree.get_tree()
    can1.create_text(340,30,text='Pending Orders',font=font.Font(family='Ailza Bright Demo',underline=1,size=18,weight='bold'),fill='navyblue')
    can1.create_window(110,80,window=table,anchor='nw')
    get_button=Button(wind,text='Display Menu',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=get_details)
    can1.create_window(470,80,window=get_button,anchor='nw')
    delete_button=Button(wind,text='Delete Order',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=delete_order)
    can1.create_window(470,260,window=delete_button,anchor='nw')


def logout():
    wind.destroy()
    import intro
    

mechanism=Mechanism()

can.create_text(287,10,text='Apollo Sindoori',anchor='nw',fill='navyblue',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25,underline=1),)
can.create_text(290,10,text='Apollo Sindoori',anchor='nw',fill='white',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25),)

can.create_text(370,250,text='What are you looking for?? ',font=font.Font(family='Ailza Bright Demo',size=18,weight='bold'),fill='navyblue')

menu_button =Button(wind,text='Display Menu',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=menu_display)
can.create_window(310,290,window=menu_button,anchor='nw')

menu_button =Button(wind,text='Customise Menu',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=menu_update)
can.create_window(310,350,window=menu_button,anchor='nw')

order=Button(wind,text='Pending Order',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=pending_order)
can.create_window(310,410,window=order,anchor='nw')

logout=Button(wind,text='Logout',width=8,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=logout)
can.create_window(610,70,window=logout,anchor='nw')


wind.mainloop()


