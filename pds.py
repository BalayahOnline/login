from tkinter import*
from tkinter import ttk
from tkinter import messagebox

splash_root = Tk()
splash_root.geometry("600x150")
splash_root.title('ZK JEESTO')
splash_root.configure(bg='#2d4c63')

splash_labe2 = Label(splash_root, text="ZK/Management/Systen", bg='#2d4c63' , fg='WHITE',font=('Wide Latin',18,'bold')) 
splash_labe2.pack()
splash_labe2.place(x=45,y=10)
splash_label = Label(splash_root, text="", font=18,bg='white' ,width='600')
splash_label.pack(fill=Y)
splash_label.place(x=0,y=100)

def main():

    splash_root.destroy()
    lg_from=Tk()
    lg_from.title('LOGIN FORM')
    lg_from.configure(bg="#4d4d4d")
    lg_from.geometry('560x380+300+200')
    lg_from.resizable(False,False)
    fr=Frame(lg_from,width=230,height=390,bg='#ebedec')
    fr.place(x=0,y=0)
    la=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la.place(x=14,y=0)
    la1=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la1.place(x=0,y=25)
    la2=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la2.place(x=14,y=50)
    la3=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la3.place(x=0,y=75)
    la4=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la4.place(x=14,y=100)
    la5=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la5.place(x=0,y=125)

    la6=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la6.place(x=14,y=150)
    la7=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la7.place(x=0,y=175)
    la8=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la8.place(x=14,y=200)
    la9=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la9.place(x=0,y=225)
    la10=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la10.place(x=14,y=250)
    la11=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la11.place(x=0,y=275)
    la12=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la12.place(x=14,y=300)
    la13=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la13.place(x=0,y=325)
    la14=Label(fr,text='',bg="#4d4d4d", width=30,height=0)
    la14.place(x=14,y=350)

    

    ###--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    frame=Frame(lg_from,width=300,height=350,bg='#ebedec')
    frame.place(x=250,y=20)
    heading=Label(frame,text='sign in',fg='black',bg='#ebedec',font=('Wide Latin',15,'bold'))
    heading.place(x=90,y=10)

    ###text boxka usernameka ----------------------------------------------------------------------------------------------------------------------------------------------
    def on_enter(u):
        usern.delete(0, 'end')
    def on_leave(u):
        name=usern.get()
        if name=='':
            usern.insert(0,'username')
        
    usern= Entry(frame,width=28,fg='#969595',border=0,bg='#f7faf9',font=('arial',12))
    usern.place(x=20,y=80)
    usern.insert(0,'username')
    usern.bind('<FocusIn>',on_enter)
    usern.bind('<FocusOut>',on_leave)

    Frame(frame,width=255,height=2,bg='black').place(x=20,y=100)

    ###text boxka passworka -----------------------------------------------------------------------------------------------------------------------------------------------

    def on_enter(p):
        code.delete(0, 'end')
    def on_leave(p):
        name=code.get()
        if name=='':
            code.insert(0,'password')
        

    code=Entry(frame,width=28,fg='#969595',border=0,bg='#f7faf9',show='*',font=('arial',12))
    code.place(x=20,y=150)
    code.insert(0,'********')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
        
    Frame(frame,width=255,height=2,bg='black').place(x=20,y=170)
### qaybta amar siinta text boxyad------------------------------------------------------------------------------------------------------------------------------------

    def hash():
        user=usern.get()
        pas=code.get()
        
        if user=="" and pas=="" :
            messagebox.showinfo(title="info",message="please fill the empty text boxs")
            
        elif user=="":
            messagebox.showinfo(title="info",message="please enter the username")
        elif pas=="":
            messagebox.showinfo(title="info",message="please enter the password")
        elif user=="admin" and pas=="admin":
            messagebox.showinfo(title="info",message="correct account")
            dash=Tk()
            dash.geometry('900x600')
            dash.resizable(False,False)
            dash.configure(bg='black')
            fr1=Frame(dash,relief=RIDGE,bd=2,bg='white')
            fr1.place(x=2,y=2,width=895,height=50)
            frB=Frame(dash,relief=RIDGE,bd=2,bg='white')
            frB.place(x=254,y=54,width=643,height=544)
            fr2=Frame(dash,relief=RIDGE,bd=2,bg='white')
            fr2.place(x=2,y=54,width=250,height=544)
            dhb1=Button(fr2,text="Home",command=quit,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=0,width=250,height=40)
            dhb2=Button(fr2,text="SRUDENT",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=50,width=250,height=40)
            dhb3=Button(fr2,text="CLASS",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=100,width=250,height=40)
            dhb4=Button(fr2,text="SUBJECT",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=150,width=250,height=40)
            dhb5=Button(fr2,text="EXAM",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=200,width=250,height=40)
            dhb6=Button(fr2,text="ATTANDANCE",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=250,width=250,height=40)
            dhb7=Button(fr2,text="TEACHERS",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=400,width=250,height=40)
            dhb8=Button(fr2,text="SALARY",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=450,width=250,height=40)
            dhb9=Button(fr2,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=500,width=250,height=40)
            l1heading = Label(fr1, text="ZK/Management/Systen", bg='white' , fg='black',font=('Wide Latin',18,'bold')) 
            l1heading.place(x=300,y=10)


            dhb11=Button(frB,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=10,y=10,width=200,height=200)
            dhb12=Button(frB,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=10,y=305,width=200,height=200)
            dhb13=Button(frB,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=220,y=10,width=200,height=200)
            dhb14=Button(frB,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=220,y=305,width=200,height=200)
            dhb15=Button(frB,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=430,y=10,width=200,height=200)
            dhb16=Button(frB,text="ADMINISTRATION",relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=430,y=305,width=200,height=200)





            lg_from.destroy()
            def openstudentform():
                dash.destroy()
                windows=Tk()
                windows.geometry("660x300")
                windows.resizable(width=False,height=False)
                windows.configure(bg="gray")
                windows.title("registration form")

                #qaybta variables-ka
                firstname=StringVar()
                lastname=StringVar()
                address=IntVar()

                #qaybta labels-ka
                toplab=Label(windows,text="welcome to registration form",font=("Arail",18,"bold")
                               ,fg="white",bg="blue")
                toplab.pack(side=TOP,fill=X)
                bolab=Label(windows,text="developed evening class",font=("Arail",13,"bold")
                               ,fg="white",bg="green")
                bolab.pack(side=BOTTOM,fill=X)
                bl1=Label(windows,text="firstname:",font=("Arail",12,"bold"))
                bl1.place(x=10,y=70)
                bl2=Label(windows,text="lastname:",font=("Arail",12,"bold")).place(x=10,y=105)
                bl3=Label(windows,text="Address:",font=("Arail",12,"bold")).place(x=10,y=140)

                #qaybta textboxs-ka hhda
                tx1=Entry(windows,textvariable=firstname).place(x=120,y=70,width=160,height=25)
                tx2=Entry(windows,textvariable=lastname).place(x=120,y=105,width=160,height=25)
                tx3=Entry(windows,textvariable=address).place(x=120,y=140,width=160,height=25)

                #qaybta functions-ka
                def hom():
                    ff=firstname.get()
                    ln=lastname.get()
                    ad=address.get()
                    if ff=="" and ln=="" and ad==0:
                        messagebox.showinfo("info","meel banaan lama ogola")
                        
                    elif ff=="":
                        messagebox.showinfo("information","please enter firstname")
                    elif ln=="":
                        messagebox.showinfo(title="info",message="please enter lastname")
                    elif ad==0:
                        messagebox.showinfo(title="info",message="please enter address")
                    #elif ff=="ict" and ln=="alpha":
                        
                    else:
                        import sqlite3
                        con=sqlite3.connect("sevc.db")
                        cur=con.cursor()
                        cur.execute("create table if not exists registt(firstname TEXT, lastname TEXT, address INTEGER)")
                        cur.execute("insert into registt values('%s','%s','%s')"%(firstname.get(),lastname.get(),address.get()))
                        cur.close()
                        con.commit()
                        con.close()
                        messagebox.showinfo("info","this person successfuly saved")
                        windows.destroy()
                        
                    
                        #messagebox.showinfo("info","")

                        
                        #messagebox.showinfo("info","")

                #qaybta buttons-ka
                b1=Button(windows,command=hom,text="Save",relief=RIDGE,cursor="hand2",bd=8,font=("Arail",18,"bold"),bg="yellow",anchor="center").place(x=10,y=200,width=100,height=45)
                b2=Button(windows,text="Cancel",relief=SUNKEN,bd=7,cursor="circle",command=quit,font=("Arail",18,"bold"),bg="red",fg="white").place(x=160,y=200,width=100,height=45)

            

            dhb2=Button(fr2,text="SRUDENT",command=openstudentform,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=50,width=250,height=40)
        else:
            messagebox.showerror(title='error',message="incorrecr")
            usern.delete(0,'end')
            
            
        def openstudentfors():
            dash.destroy()
            windowss=Tk()
            windowss.geometry("660x300")
            windowss.resizable(width=False,height=False)
            windowss.configure(bg="gray")
            windowss.title("class form")
        dhb3=Button(fr2,text="CLASS",command=openstudentfors,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=100,width=250,height=40)
        def openstudentforss():
                dash.destroy()
                windowss=Tk()
                windowss.geometry("660x300")
                windowss.resizable(width=False,height=False)
                windowss.configure(bg="gray")
                windowss.title("sunject form")
        dhb4=Button(fr2,text="SUBJECT",command=openstudentforss,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=150,width=250,height=40)
                
        def openstudentforsss():
                dash.destroy()
                windowss=Tk()
                windowss.geometry("660x300")
                windowss.resizable(width=False,height=False)
                windowss.configure(bg="gray")
                windowss.title("exam form")
        dhb5=Button(fr2,text="EXAM",command=openstudentforsss,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=200,width=250,height=40)
               
        def openstudentforssss():
                dash.destroy()
                windowss=Tk()
                windowss.geometry("660x300")
                windowss.resizable(width=False,height=False)
                windowss.configure(bg="gray")
                windowss.title("attandance form")
        dhb6=Button(fr2,text="ATTANDANCE",command=openstudentforssss,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=250,width=250,height=40)
               
        def openstudentforsssss():
                dash.destroy()
                windowss=Tk()
                windowss.geometry("660x300")
                windowss.resizable(width=False,height=False)
                windowss.configure(bg="gray")
                windowss.title("teachers form")

        dhb7=Button(fr2,text="TEACHERS",command=openstudentforsssss,relief=SUNKEN,bd=2,cursor="circle",font=("Arail",10,"bold"),bg="#1f2942",fg="#7f828a").place(x=0,y=400,width=250,height=40)
    ###buttonka log in ----------------------------------------------------------------------------------------------------------------------------------------------------

    Button(frame,width=36,pady=7,text='Log in',bg='blue',fg='white',border=0,cursor='hand2',command=hash).place(x=20,y=210)


    ###buttonka forget passwordka -----------------------------------------------------------------------------------------------------------------------------------------

    Button(frame,width=13,pady=7,text='forget password',bg='white',fg='black',border=0,cursor='dotbox',font=('arial',9)).place(x=20,y=280)


    sing_up=Button
splash_root.after(1500, main)
def openNewWindow():
     
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
              text ="This is a new window").pack()

mainloop()

