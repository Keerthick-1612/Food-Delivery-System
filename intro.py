from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from tkinter.messagebox import *



wind=Tk()
wind.geometry(f'700x600')
wind.resizable(width=False,height=False)
wind.title('Apollo Sindoori')
wind.iconbitmap('icon.ico')



def cust():
    wind.destroy()
    import front
  
  
    
def man():
    wind3=Toplevel()
    wind3.geometry(f'600x349+{280}+{50}')
    wind3.resizable(False,False)
    wind3.iconbitmap('icon.ico')



    def _login():
        file=open('user.txt')
        cred=file.readline().split(',')
        if name_entry.get()==cred[0] and pass_entry.get()==cred[1]:
            wind.destroy()
            import man
        else:
            showwarning('Login Error','Invalid Login Credentials')
            return
        
        
    def new():
        wind3.destroy()
        wind4=Toplevel()
        wind4.geometry(f'600x349+{280}+{50}')
        wind4.resizable(False,False)
        wind4.iconbitmap('icon.ico')
        can3=Canvas(wind4,width=600,height=349)
        can3.pack()
        
        
        def signup():
            file=open('user.txt','w')
            string=user_entry.get()+','+password.get()+','+name_entry.get()+','+ph_entry.get()
            file.writelines(string)
            file.close()
            wind.destroy()
            import man

        password=StringVar()
                    
        img3=ImageTk.PhotoImage(Image.open('Bill1.jpg'))    
        can3.create_image(0,0,image=img3,anchor='nw')
        can3.create_text(290,90,text='Sign Up ',fill='navyblue',font=font.Font(family='Ailza Bright Demo',underline=1,weight='bold',size=15))
        can3.create_text(250,140,text='Enter the Name: ',fill='navyblue',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        can3.create_text(250,180,text='Enter the Phone number: ',fill='navyblue',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        can3.create_text(250,220,text='Enter the username: ',fill='navyblue',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        can3.create_text(250,260,text='Enter the password: ',fill='navyblue',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        
        name_entry=Entry(wind4,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        ph_entry=Entry(wind4,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        user_entry=Entry(wind4,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        password_entry=Entry(wind4,width=10,textvariable=password,relief=SUNKEN,show ='●',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
        sign_up=Button(wind4,text='Signup',command=signup,width=10,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white')
        eye=Button(wind4,image=final_eye,background='black',command=lambda: see(password_entry))
        
        
        can3.create_window(350,130,window=name_entry,anchor='nw')
        can3.create_window(350,170,window=ph_entry,anchor='nw')
        can3.create_window(350,210,window=user_entry,anchor='nw')
        can3.create_window(350,250,window=password_entry,anchor='nw')
        can3.create_window(350,300,window=sign_up,anchor='nw')
        can3.create_window(465,250,window=eye,anchor='nw')
        
        wind4.mainloop()
        
    def see(entry):
        if entry['show']=="●":
            entry['show']=''
        elif entry['show']=='':
            entry['show']="●"


                
    can3=Canvas(wind3,width=600,height=349)
    can3.pack()
    
    img3=ImageTk.PhotoImage(Image.open('Bill1.jpg'))    
    can3.create_image(0,0,image=img3,anchor='nw')
    
    eye_img=Image.open('eye.png')
    resize_eye=eye_img.resize((20,20))
    final_eye=ImageTk.PhotoImage(resize_eye)
    
    password=StringVar()
    
    can3.create_text(290,150,text='Login Credentials ',fill='navyblue',font=font.Font(family='Ailza Bright Demo',underline=1,weight='bold',size=15))
    
    can3.create_text(250,200,text='Enter the username: ',fill='navyblue',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    can3.create_text(250,240,text='Enter the password: ',fill='navyblue',font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    name_entry=Entry(wind3,width=10,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    pass_entry=Entry(wind3,width=10,show='●',textvariable=password,relief=SUNKEN,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15))
    eye_button=Button(wind3,background='black',image=final_eye,command=lambda: see(pass_entry))
    
    login=Button(wind3,text='Login',width=10,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=_login)
    new_user=Button(wind3,text='New Login',width=13,font=font.Font(family='Bahnschrift Light SemiCondensed',weight='bold',size=15),background='DodgerBlue3',foreground='white',command=new)
    can3.create_window(350,190,window=name_entry,anchor='nw')
    can3.create_window(350,230,window=pass_entry,anchor='nw')
    can3.create_window(350,300,window=login,anchor='nw')
    can3.create_window(100,300,window=new_user,anchor='nw')
    can3.create_window(465,232,window=eye_button,anchor='nw')
    
    wind3.mainloop()



can=Canvas(wind,width=700,height=600)
can.pack()
img=Image.open('5789625.jpg')    
resized=img.resize((700,600))
final_img=ImageTk.PhotoImage(resized)

can.create_image(0,0,image=final_img,anchor='nw')
can.create_text(350,120,text='Apollo Sindoori',font=font.Font(family='Ailza Bright Demo',size=35,slant='italic',weight='bold'),fill='yellow')
can.create_text(350,220,text='Welcome',font=font.Font(family='Ailza Bright Demo',size=35,weight='bold'),fill='Skyblue')
wind.bind('<Return>',lambda e:wind.destroy())
a=can.create_text(350,340,text='Let me know who you are...',font=font.Font(family='Ailza Bright Demo',size=18,slant='italic',weight='bold'),fill='sky blue')
cust=Button(wind,text='Customer',padx=25,width=8,highlightthickness=0,bd=0,font=font.Font(family='Ailza Bright Demo',size=12,weight='bold'),command=cust)
manag=Button(wind,text='Manager',padx=25,width=8,highlightthickness=0,bd=0,font=font.Font(family='Ailza Bright Demo',size=12,weight='bold'),command=man)
can.create_window(200,350,window=manag,anchor='nw')
can.create_window(390,350,window=cust,anchor='nw')

wind.mainloop()

