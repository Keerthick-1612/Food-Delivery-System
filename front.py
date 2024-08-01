from tkinter import *
from PIL  import ImageTk,Image
from tkinter import font
from tkinter import ttk
import time
from datetime import datetime
from Tree import Tree
from order import order_list
from order import *
from tkinter.messagebox import *




def logout():
    wind.destroy()
    import intro


def menu(_time):
            
    def add():
                
        final.configure(state=NORMAL)
        
        if final.get(0)=='NO ORDERS':
            final.delete(0)
        if list1.get(ANCHOR)=='' or quant.get()=='0':
            lab.after(5000,lab.configure(text=''))
        def remove():
            if final.get(ANCHOR)=='':
                lab.config(text='Please select the order to remove')
                return
            elif len(final.get(0,END))==1:
                final.delete(ANCHOR)
                remove.destroy()
                final.insert(0,'NO ORDERS')
                final.config(state=DISABLED)
                return
            
            final.delete(ANCHOR)

        def place():
            d=req_dict
            def proceed():
                #{'Burger': [20.0, 15.99, 'b'], 'dosa': [60.0, 50, 'b'], 'Barbeque': [25.0, 50.0, 'mod']} 
               # [[1, 'Barbeque', '50.0', '1', '50.0'], [2, 'Burger', '15.99', '1', '15.99']]
                l2=[i[1] for i in list2]
                for i in range(len(l2)):
                    z=d[l2[i]][2]
                    list2[i].append(z)

                # print('fddf',list2)
                name=name_entry.get()
                mechanism.bill (list2,name)

            
                

                

                

                wind2.destroy()
                
                wind3=Toplevel()
                wind3.geometry(f'600x349+{280}+{50}')
                wind3.resizable(False,False)
                wind3.iconbitmap('icon.ico')

                            
                can3=Canvas(wind3,width=600,height=349)
                can3.pack()
                
                img3=ImageTk.PhotoImage(Image.open('Bill1.jpg'))
                
                can3.create_image(0,0,image=img3,anchor='nw')
                
                img4=Image.open('Tick.png')
                resized=img4.resize((200,200))
                img5=ImageTk.PhotoImage(resized)
                can3.create_image(200,10,image=img5,anchor='nw')
                can3.create_text(280,230,text='Your Order is placed...',fill='navyblue',font=font.Font(family='Ailza Bright Demo',size=15,weight='bold'))
                back=Button(wind3,text='Back',padx=2,foreground='white',background='DodgerBlue3',font=font.Font(family='Ailza Bright Demo',size=12,weight='bold'),command=lambda: (wind3.destroy(),place_button.config(state=NORMAL)))
                can3.create_window(490,280,window=back,anchor='nw')
                wind3.mainloop()
                
                    

            place_button.configure(state=DISABLED)
            wind2=Toplevel()
            wind2.geometry(f'600x349+{280}+{50}')
            wind2.resizable(False,False)
            wind2.iconbitmap('icon.ico')
            #s.no, food,cost,qty,total
            can2=Canvas(wind2,width=600,height=349)
            can2.pack()
            img3=ImageTk.PhotoImage(Image.open('Bill1.jpg'))
            can2.create_image(0,0,image=img3,anchor='nw')
            
            list1=final.get(0,END)
            list2=[]
            for i in list1:
                a=i.split(' - ')
                list2.append(a)
            print(list2)   

            for i in range(len(list2)):
                total_cost=float(list2[i][-1])
                qu=int(list2[i][1])

                list2[i].insert(1,str(total_cost/qu))
                list2[i].insert(0,i+1)
            


            
            
            if len(list1)+1>5:
                tree=Tree(wind2,5,5)
            else:
                
                tree=Tree(wind2,len(list1),5)

      
                
            tree.create_headings(['S.NO','Food Item','Cost/item','Quantity','Total Cost'])
            tree.add_datas(list2)
            print("List2: ",list2)
            can2.create_text(180,50,text='Here is the finalised bill',anchor='nw',font=font.Font(family='Ailza Bright Demo',underline=1,size=17,weight='bold'),fill='Dodgerblue4')
            can2.create_window(35,100,anchor='nw',window=tree.get_tree())
            go_back=Button(wind2,text='Go back',font=font.Font(family='Ailza Bright Demo',size=10,weight='bold'),background='DodgerBlue1',foreground='white',command=lambda: (wind2.destroy(),place_button.config(state=NORMAL)))
            can2.create_window(165,280,window=go_back,anchor='nw')
            name_entry=Entry(wind2,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
            proceed_button=Button(wind2,text='Confirm',font=font.Font(family='Ailza Bright Demo',size=10,weight='bold'),background='DodgerBlue1',foreground='white',command=proceed)
            can2.create_window(450,280,window=proceed_button,anchor='nw')
            can2.create_window(370,238,window=name_entry,anchor='nw')
            can2.create_text(160,240,text='Enter your name: ',anchor='nw',font=font.Font(family='Ailza Bright Demo',size=12,weight='bold'),fill='navyblue')
            wind2.mainloop()



        qty=quant.get()
        food=list1.get(ANCHOR)
        remove=Button(wind,text='Remove',padx=30,width=3,bd=0,activeforeground='white',activebackground='Dodgerblue4',relief=FLAT,
                      font=font.Font(family='MV Boli',size=10,weight='bold'),bg='DodgerBlue3',fg='white',highlightcolor='black',command=remove)
        can.create_window(470,500,window=remove,anchor='nw')
        final.insert(0,'{} - {} - {}'.format(food,qty,str(float(cost.cget('text').split()[1])*int(quant.get()))))
        cost.configure(text='')
        quant.config(state=NORMAL)
        quant.delete(0,END)
        quant.insert(0,0)
        quant.config(state=DISABLED)
        place_button=Button(wind,text='Place your order',padx=30,width=6,bd=0,activeforeground='white',activebackground='Dodgerblue4',relief=FLAT,
                      font=font.Font(family='MV Boli',size=10,weight='bold'),bg='DodgerBlue3',fg='white',highlightcolor='black',command=place)
        can.create_window(570,500,window=place_button,anchor='nw')



    def event1(e):
        x=req_dict[list1.get(ANCHOR)][-1]
        if list1.get(ANCHOR)!='':
            cost.config(text='₹ {} /no'.format(req_dict[list1.get(ANCHOR)][-2]))
        quant.config(state=NORMAL)
        quant.delete(0,END)
        quant.insert(0,0)
        quant.config(state=DISABLED)
     
     
            
    def incdec(op):
        quant.config(state=NORMAL)
        
        a=int(quant.get())
        quant.delete(0,END)
        if op=='+':
            quant.insert(0,a+1)
        else:
            if a>0:
                quant.insert(0,a-1)
            else:
                quant.insert(0,0)
        quant.config(state=DISABLED)
    if _time=='food':
        now_time=datetime.now()
        req_=order_list(now_time.hour)
        req_dict.update(req_)
        req_dict1=req_
    elif _time=='all':
        req_=day_order_list()
        req_dict.update(req_)
        req_dict1=req_

    else:
        req_=order_list()
        req_dict.update(req_)
        req_dict1=req_
    
    
        
    req=list(req_dict1)
    # food.configure(text=tim.title())
    list1.delete(0,END)
    can.create_window(250,350,window=list1,anchor='nw')
    for i in req:
        list1.insert(END,i)
        
    add_button.configure(command=add)
    can.create_window(250,500,window=add_button,anchor='nw')
                
    quant=Entry(wind,width=3,font=font.Font(family='MV Boli',size=13,weight='bold'),disabledbackground='white',disabledforeground='DodgerBlue3')
    quant.insert(0,0)
    quant.config(state=DISABLED)
    up_arrow=Button(wind,text='↑',relief=GROOVE,bd=1,font=font.Font(family='MV Boli',size=5,weight='bold'),command=lambda: incdec('+'))
    down_arrow=Button(wind,text='↓',relief=GROOVE,bd=1,font=font.Font(family='MV Boli',size=5,weight='bold'),command=lambda: incdec('-'))
    
    can.create_window(490,400,window=quant,anchor='nw')
    can.create_window(443,418,window=up_arrow,anchor='nw')
    can.create_window(443,430,window=down_arrow,anchor='nw')
    can.create_text(415,410,text='Qty',font=font.Font(family='MV Boli',size=13,weight='bold'),fill='Dodgerblue4')
    can.create_window(395,420,window=quant,anchor='nw')
    can.create_text(390,330,text='Menu',font=font.Font(family='MV Boli',size=15,weight='bold'),fill='Dodgerblue4')
    can.create_window(470,350,window=final,anchor='nw')
    if final.get(0,END):
        pass
    else:
        final.insert(0,'NO ORDERS')
        final.configure(state=DISABLED)

    list1.bind('<<ListboxSelect>>',event1)



mechanism=Mechanism()
 
#Intro Page

wind=Tk()
wind.geometry(f'750x550+{280}+{25}')
wind.resizable(False,False)
wind.iconbitmap('icon.ico')

wind.title('Hotel')
can=Canvas(wind,width=750,height=550)
can.pack()
img=Image.open('main1.jpg')

resized=img.resize((750,550))
req_dict={}

final_img=ImageTk.PhotoImage(resized)
can.create_image(0,0,image=final_img,anchor='nw')
food=Button(wind,text='',padx=30,width=10,bd=0,activeforeground='white',activebackground='Dodgerblue4',relief=FLAT,
                  font=font.Font(family='MV Boli',size=15,weight='bold'),bg='DodgerBlue3',fg='white',command=lambda: menu('food'))
chat=Button(wind,text='Menu Of The Day',padx=30,width=10,bd=0,activeforeground='white',activebackground='Dodgerblue4',relief=FLAT,
                  font=font.Font(family='MV Boli',size=15,weight='bold'),bg='DodgerBlue3',fg='white',command=lambda: menu('all'))
if datetime.now().hour in range(0,12):
    food.configure(text='Breakfast')
    Time='b'
elif datetime.now().hour in range(12,18):
    food.configure(text='Lunch')
    Time='l'
elif datetime.now().hour in range(18,24):
    food.configure(text='Dinner')
    Time='d'
can.create_window(40,350,window=food,anchor='nw')
can.create_window(40,450,window=chat,anchor='nw')

can.create_text(287,10,text='Apollo Sindoori',anchor='nw',fill='navyblue',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25,underline=1),)
can.create_text(290,10,text='Apollo Sindoori',anchor='nw',fill='white',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25),)
can.create_text(255,150,text='Welcome Customer',anchor='nw',fill='blue',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25),)
can.create_text(258,150,text='Welcome Customer',anchor='nw',fill='white',font=font.Font(family='Ailza Bright Demo',weight='bold',size=25),)


# food.bind('<Enter>',lambda event: food.configure(bg='white',fg='black'))
# food.bind('<Leave>',lambda event: food.configure(bg='DodgerBlue3',fg='white'))

list1=Listbox(wind,bd=0,bg='white',fg='navyblue',width=12,height=4,font=font.Font(family='Ailza Bright Demo',size=12,weight='bold'))
add_button=Button(wind,text='Add',padx=30,width=5,bd=0,activeforeground='white',activebackground='Dodgerblue4',relief=FLAT,
                  font=font.Font(family='MV Boli',size=10,weight='bold'),bg='DodgerBlue3',fg='white',highlightcolor='black')

lab=Label(wind,text='Please select your order or quantity to add',fg='tomato3',bg='white',font=font.Font(weight='bold',size=12))
cost=Label(wind,text='',font=font.Font(family='Ailza Bright Demo',weight='bold',size=15),fg='navyblue',bg='white')
can.create_window(360,500,window=cost,anchor='nw')
final=Listbox(wind,bd=0,width=15,bg='white',fg='navyblue',height=4,relief=GROOVE,font=font.Font(family='Ailza Bright Demo',size=12,weight='bold'))
logout=Button(wind,text='Logout',width=8,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='tomato3',foreground='white',command=logout)
can.create_window(610,70,window=logout,anchor='nw')
wind.mainloop()

