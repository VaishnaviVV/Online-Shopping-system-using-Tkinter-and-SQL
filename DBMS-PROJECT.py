import cx_Oracle
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 

img  = Image.open("PIC1.png") 
#from tkinter.ttk import *
gui1= Tk()
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo).place(x=0,y=0,relwidth=1, relheight=1)

gui= Tk()
gui2=Tk()
gui3=Tk()
gui4=Tk()
gui5=Tk()
gui6=Tk()
gui7=Tk()
gui8=Tk()
gui9=Tk()
FG = 'black'
BG = 'pink'
GUI_BG = 'light blue'
GUI_BG1='light green'
GUI_BG2='pink'
con=cx_Oracle.connect('system/19BCE1497@localhost')
cur=con.cursor()
cur.execute("SELECT * FROM LOGIN")
for i in cur:
    print(i)
s="SELECT USERTYPE FROM LOGIN WHERE ENAB='ENABLED'"
cur.execute(s)
res=cur.fetchall()
print(res)
ct=0
ename=""
epass=""
ch=0
def loginfailed():
    messagebox.showinfo("error","login failed")
def admintk():
        gui2.configure(background=GUI_BG2)
        
        gui2.geometry("1000x1000")
        s="ADMIN - "+ename
        la1=Label(gui2, text=s,bg=GUI_BG2, font=('', 20))
        la1.grid(row=1,column=1)
        la2=Label(gui2, text="Options - Manage Product/User/Order/Moderator/Logout",bg=GUI_BG2, font=('', 22))
        la2.grid(row=3,column=1)
        #var1 = StrVar()
        var1 = IntVar()
        
        R1 = Radiobutton(gui2, text="MANAGE PRODUCT",bg=GUI_BG2, variable=var1, value=1,command=man_prod)
        R1.grid(row=5,column=1)

        R2 = Radiobutton(gui2, text="MANAGE USER", bg=GUI_BG2,variable=var1, value=2,command=man_user)
        R2.grid(row=6,column=1)

        R3 = Radiobutton(gui2, text="MANAGE ORDER",bg=GUI_BG2, variable=var1, value=3,command=man_orders)
        R3.grid(row=7,column=1)
        
        R4 = Radiobutton(gui2, text="MANAGE MODERATOR",bg=GUI_BG2, variable=var1, value=4,command=man_mod)
        R4.grid(row=8,column=1)
        gui2.mainloop()
        
        
def log_admin():
    gui3.geometry("100x100")
    p=messagebox.askquestion("confirm","do u want to edit products?")
    if p=="yes":
           #print("hi")
          
           #ad_username=input("Enter admin username")
           #ad_pwd=input("Enter admin pwd")
           ad_username=ename
           ad_pwd=epass
           d="SELECT USERNAME,USERPWD from LOGIN WHERE USERTYPE='ADMIN'"
           cur.execute(d)
           result=cur.fetchall()
           flag=0  
           print(result)                
           for j in result:
               if ad_username ==j[0] and ad_pwd ==j[1]:
                     flag=1
            
           if flag==1:       
                  messagebox.showinfo("login","admin logged in successfully")
                  admintk()
           else:
               loginfailed()
                 
    elif p=="no":
           loginfailed()
           
    #gui3.destroy()
    gui3.mainloop()    
    
def iiii():
    gui.destroy()
    gui2.destroy()
    gui3.destroy()
    gui1.destroy()
    gui4.destroy()
    gui5.destroy()
    gui6.destroy()
    gui7.destroy()
    gui8.destroy()
    gui9.destroy()
        
def login2():   
        FG = 'black'
        BG = 'pink'
        GUI_BG = 'violet'
        gui1.configure(background=GUI_BG)
        gui1.title("PyShop - Online Shopping")
        gui1.geometry("1300x1000")
        ppp=Label(gui1, text="Enter the user type who wants to login:Admin/User/Moderator", font=('', 22))
        ppp.grid(row=0,column=1)
        def sel():
            selection = "You selected the option " + str(var.get())
            la1.config(text = selection)

        def gygygy():
              print(str(var.get()))
              print(e1.get())
              print(e2.get())
              global ename,epass
              ename=e1.get()
              epass=e2.get()
              if str(var.get())=="1":
                       log_admin()
              if str(var.get())=="2":
                       log_moderator()
              if str(var.get())=="3":
                       log_user()
              #gui1.destroy()
             
        
        var = IntVar()
        R1 = Radiobutton(gui1, text="ADMIN", variable=var,anchor = W, value=1,command=sel)
        R1.grid(row=4,column=1)

        R2 = Radiobutton(gui1, text="MODERATOR", variable=var,anchor = W, value=2,command=sel)
        R2.grid(row=5,column=1)

        R3 = Radiobutton(gui1, text="USER", variable=var,anchor = W, value=3,command=sel)
        R3.grid(row=6,column=1)
        la1=Label(gui1, text="",bg=GUI_BG, font=('', 20))
        
        ppp1=Label(gui1, text="User Name", font=('', 20))
        ppp1.grid(row=8,column=2)
        
        e1 = Entry(gui1)
        e1.grid(row=8,column=3)
        ppp2=Label(gui1, text="Password", font=('', 20))
        ppp2.grid(row=10,column=2)
        
        e2 = Entry(gui1)
        e2.grid(row=10,column=3)
        
        addBtn11 = Button(gui1, text = " Sign in ",font=('', 12),command=gygygy)
        addBtn11.grid(row =14, column = 3)
        #ct+=1
        addBtn12 = Button(gui1, text = " Log out ",font=('', 12),command=iiii)
        addBtn12.grid(row =14, column = 2)
        gui1.mainloop()
        
    
def man_prod():
        gui6.configure(background=GUI_BG1)
        gui6.title("PyShop - Online Shopping")
        gui6.geometry("1300x1000")    
        ppp1=Label(gui6, text="Product Id ",bg=GUI_BG1, font=('', 20))
        ppp1.grid(row=4,column=2)
        e1 = Entry(gui6)
        e1.grid(row=4,column=4)
        
        ppp2=Label(gui6 , text="Product Name ",bg=GUI_BG1, font=('', 20))
        ppp2.grid(row=6,column=2)
        e2 = Entry(gui6)
        e2.grid(row=6,column=4)
        
        ppp3=Label(gui6, text="Product Description ",bg=GUI_BG1, font=('', 20))
        ppp3.grid(row=8,column=2)
        e3 = Entry(gui6)
        e3.grid(row=8,column=4)
        
        ppp4=Label(gui6, text="Price ",bg=GUI_BG1, font=('', 20))
        ppp4.grid(row=10,column=2)
        e4 = Entry(gui6)
        e4.grid(row=10,column=4)
        
        def addproduct():
            print("Add Product")
            ID=e1.get()
            NAME=e2.get()
            DESCRIPTION=e3.get()
            PRICE=e4.get()
            e="insert into product_details values("+ID+","+"'"+NAME+"',"+"'"+DESCRIPTION+"',"+"'"+PRICE+"')"
            cur.execute(e)
            #cur.execute("insert into PRODUCT_details values(&ID,'&NAME','&DESCRIPTION',&PRICE)")
            con.commit()
            cur.execute("SELECT * from product_details")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("Product List", sstr)

        def viewproduct():
            print("View")
            PID=e1.get()
            a="select * from product_details where ID="+PID
            cur.execute(a)
            con.commit()
            #cur.execute("select * from product_details")
            D=cur.fetchall();
            sstr=""
            print(len(D))
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("View Product Details", sstr)
        
        def delproduct():
            print("del product")
            PID=e1.get()
            f="DELETE from product_details where ID="+PID
            cur.execute(f)
            con.commit()
            cur.execute("SELECT * from product_details")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("Product Details- After Deletion", sstr)
                
                    
        addBtn12 = Button(gui6, text = "ADD PRODUCT",font=('', 12),command=addproduct)
        addBtn12.grid(row =18, column = 3)
        addBtn13 = Button(gui6, text = "VIEW PRODUCT",font=('', 12),command=viewproduct)
        addBtn13.grid(row =18, column = 4)
        addBtn14 = Button(gui6, text = "DELETE PRODUCT",font=('', 12),command=delproduct)
        addBtn14.grid(row =18, column = 5)
        gui6.mainloop()
        
def man_user():
    gui7.configure(background=GUI_BG1)
    gui7.title("PyShop - Online Shopping")
    gui7.geometry("1300x1000")
    ppp1=Label(gui7, text=" User Id ",bg=GUI_BG1, font=('', 20))
    ppp1.grid(row=4,column=2)
    e1 = Entry(gui7)
    e1.grid(row=4,column=4)
       
    ppp2=Label(gui7 , text=" User Name ",bg=GUI_BG1, font=('', 20))
    ppp2.grid(row=6,column=2)
    e2 = Entry(gui7)
    e2.grid(row=6,column=4)
        
    ppp3=Label(gui7, text=" User Emailid ",bg=GUI_BG1, font=('', 20))
    ppp3.grid(row=8,column=2)
    e3 = Entry(gui7)
    e3.grid(row=8,column=4)
        
    ppp4=Label(gui7, text=" Mobile Number ",bg=GUI_BG1, font=('', 20))
    ppp4.grid(row=10,column=2)
    e4 = Entry(gui7)
    e4.grid(row=10,column=4)
    def adduser():
            print("Add user")
            ID=e1.get()
            NAME=e2.get()
            EMAILID=e3.get()
            MOBNO=e4.get()
            e="insert into user_details1 values("+ID+","+"'"+NAME+"',"+"'"+EMAILID+"',"+"'"+MOBNO+"')"
            cur.execute(e)
            #cur.execute("insert into PRODUCT_details values(&ID,'&NAME','&DESCRIPTION',&PRICE)")
            con.commit()
            cur.execute("SELECT * from user_details1")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("user List", sstr)

    def viewuser():
            print("View")
            UID=e1.get()
            a="select * from user_details1 where user_id="+UID
            cur.execute(a)
            con.commit()
            #cur.execute("select * from product_details")
            D=cur.fetchall();
            sstr=""
            print("LEngth=====")
            print(len(D))
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("View user Details", sstr)
        
    def deluser():
            print("del user")
            UID=e1.get()
            f="DELETE from user_details1 where user_id="+UID
            cur.execute(f)
            con.commit()
            cur.execute("SELECT * from user_details1")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("user Details- After Deletion", sstr)
                
                    
    addBtn12 = Button(gui7, text = "  ADD USER ",font=('', 12),command=adduser)
    addBtn12.grid(row =18, column = 3)
    addBtn13 = Button(gui7, text = " VIEW USER  ",font=('', 12),command=viewuser)
    addBtn13.grid(row =18, column = 4)
    addBtn14 = Button(gui7, text = " DELETE USER  ",font=('', 12),command=deluser)
    addBtn14.grid(row =18,column = 5)
    gui7.mainloop()
def man_orders():
    gui8.configure(background=GUI_BG)
    gui8.title("PyShop - Online Shopping")
    gui8.geometry("1300x1000")
    ppp1=Label(gui8, text="Order Id ",bg=GUI_BG, font=('', 20))
    ppp1.grid(row=4,column=2)
    e1 = Entry(gui8)
    e1.grid(row=4,column=4)
       
    ppp2=Label(gui8 , text="Product Id ",bg=GUI_BG, font=('', 20))
    ppp2.grid(row=6,column=2)
    e2 = Entry(gui8)
    e2.grid(row=6,column=4)
        
    ppp3=Label(gui8, text="User Id ",bg=GUI_BG, font=('', 20))
    ppp3.grid(row=8,column=2)
    e3 = Entry(gui8)
    e3.grid(row=8,column=4)
        
    ppp4=Label(gui8, text="Address ",bg=GUI_BG, font=('', 20))
    ppp4.grid(row=10,column=2)
    e4 = Entry(gui8)
    e4.grid(row=10,column=4)
    def addorder():
            print("Add order")
            OID=e1.get()
            PID=e2.get()
            UID=e3.get()
            ADDRESS=e4.get()
            e="insert into product_orders values("+OID+","+PID+","+UID+","+"'"+ADDRESS+"')"
            cur.execute(e)
            #cur.execute("insert into PRODUCT_details values(&ID,'&NAME','&DESCRIPTION',&PRICE)")
            con.commit()
            cur.execute("SELECT * from product_orders")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("Order List", sstr)

    def vieworder():
            print("View")
            oID=e1.get()
            a="select * from product_orders where ID="+oID
            cur.execute(a)
            con.commit()
            #cur.execute("select * from product_details")
            D=cur.fetchall();
            sstr=""
            print("LEngth=====")
            print(len(D))
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("View order Details", sstr)
        
    def delorder():
            print("del order")
            oID=e1.get()
            f="DELETE from product_orders where ID="+oID
            cur.execute(f)
            con.commit()
            cur.execute("SELECT * from product_orders")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("order Details- After Deletion", sstr)
                
                    
    addBtn12 = Button(gui8, text = "ADD ORDER",font=('', 12),command=addorder)
    addBtn12.grid(row =18, column = 3)
    addBtn13 = Button(gui8, text = "VIEW ORDER",font=('', 12),command=vieworder)
    addBtn13.grid(row =18, column = 4)
    addBtn14 = Button(gui8, text = "DELETE ORDER",font=('', 12),command=delorder)
    addBtn14.grid(row =18, column = 5)
    gui8.mainloop()
def man_mod():
    gui9.configure(background=GUI_BG)
    gui9.title("PyShop - Online Shopping")
    gui9.geometry("1300x1000")
    ppp1=Label(gui9, text=" Moderator Id ",bg=GUI_BG, font=('', 20))
    ppp1.grid(row=4,column=2)
    e1 = Entry(gui9)
    e1.grid(row=4,column=4)
       
    ppp2=Label(gui9 , text="Moderator Name ",bg=GUI_BG, font=('', 20))
    ppp2.grid(row=6,column=2)
    e2 = Entry(gui9)
    e2.grid(row=6,column=4)
        
    ppp3=Label(gui9, text="Mod pwd ",bg=GUI_BG, font=('', 20))
    ppp3.grid(row=8,column=2)
    e3 = Entry(gui9)
    e3.grid(row=8,column=4)
        
    ppp4=Label(gui9, text="Status ",bg=GUI_BG, font=('', 20))
    ppp4.grid(row=10,column=2)
    e4 = Entry(gui9)
    e4.grid(row=10,column=4)
    def addmoderator():
            print("Add moderator")
            modid=e1.get()
            modname=e2.get()
            modpwd=e3.get()
            modstatus=e4.get()
            e="insert into login values("+modid+","+"'"+modname+"',"+"'"+modpwd+"','MODERATOR','"+modstatus+"')"
            cur.execute(e)
            #cur.execute("insert into PRODUCT_details values(&ID,'&NAME','&DESCRIPTION',&PRICE)")
            con.commit()
            cur.execute("SELECT * from login")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("Moderator List", sstr)

    def viewmoderator():
            print("View")
            mid=e1.get()
            a="select * from login where USERID="+mid
            cur.execute(a)
            con.commit()
            #cur.execute("select * from product_details")
            D=cur.fetchall();
            sstr=""
            print("LEngth=====")
            print(len(D))
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("View moderator Details", sstr)
        
    def delmoderator():
            print("del moderator")
            mid=e1.get()
            f="DELETE from login where USERID="+mid
            cur.execute(f)
            con.commit()
            cur.execute("SELECT * from login")
            D=cur.fetchall();
            sstr=""
            for i in D:
                sstr=sstr+str(i)+"\n"
                print(i)
            messagebox.showinfo("Moderator Details- After Deletion", sstr)
                
                    
    addBtn12 = Button(gui9, text = "ADD MODERATOR",font=('', 12),command=addmoderator)
    addBtn12.grid(row =18, column = 3)
    addBtn13 = Button(gui9, text = "VIEW MODERATOR",font=('', 12),command=viewmoderator)
    addBtn13.grid(row =18, column = 4)
    addBtn14 = Button(gui9, text = "DELETE MODERATOR",font=('', 12),command=delmoderator)
    addBtn14.grid(row =18, column = 5)
    gui9.mainloop()

def moderatortk():
        
        gui4.configure(background=GUI_BG)
        gui4.title("Moderator - Portal")
        gui4.geometry("1000x1000")
        s="MODERATOR - "+ename
        la1=Label(gui4, text=s,bg=GUI_BG, font=('', 20))
        la1.grid(row=1,column=1)
        la2=Label(gui4, text="Options - Manage Product/User/Order",bg=GUI_BG2, font=('', 20))
        la2.grid(row=2,column=1)
        #var1 = StrVar()
        var1 = IntVar()
        
        R1 = Radiobutton(gui4, text="MANAGE PRODUCT",bg=GUI_BG2, variable=var1, value=1,command=man_prod)
        R1.grid(row=3,column=1)

        R2 = Radiobutton(gui4, text="MANAGE USER", bg=GUI_BG2,variable=var1, value=2,command=man_user)
        R2.grid(row=4,column=1)

        R3 = Radiobutton(gui4, text="MANAGE ORDER",bg=GUI_BG2, variable=var1, value=3,command=man_orders)
        R3.grid(row=5,column=1)
        
        gui4.mainloop()
def log_moderator():
    gui5.geometry("100x100")
    p=messagebox.askquestion("confirm","do u want to edit products?")
    if p=="yes":
           ad_username=ename
           ad_pwd=epass
           d="SELECT USERNAME,USERPWD from LOGIN WHERE USERTYPE='MODERATOR'"
           cur.execute(d)
           result=cur.fetchall()
           flag=0  
           print(result)                
           for j in result:
               if ad_username ==j[0] and ad_pwd ==j[1]:
                     flag=1
            
           if flag==1:       
                  messagebox.showinfo("login","moderator logged in successfully")                                 
                  moderatortk()
                  
           else:
                loginfailed()
    elif p=="no":
           loginfailed()
    
    gui5.mainloop()    
def log_user():
    us_name= ename
    us_pass= epass
    print("user name is ",us_name)
    print("password is", us_pass)
    d="SELECT USERNAME,USERPWD from LOGIN WHERE USERTYPE='USER'"
    cur.execute(d)
    result=cur.fetchall()
    flag=0  
    print(result)                
    for j in result:
         
          print(j[0])
          print(j[1])
          if us_name==j[0] and us_pass ==j[1]:
                  flag=1
            
    if flag==1:       
        messagebox.showinfo("login","user logged in successfully")
        user_tk()
    else:
        loginfailed()
        
def user_tk():
    l=[]
    a=[]
    cur.execute("select name from product_details")
    s=cur.fetchall()
    for i in s:
          l.append(i[0])
    print(l)
    cur.execute("select price from product_details")
    p=cur.fetchall()
    for i in p:
          a.append((int)(i[0]))
    print(a)


    FG = 'black'
    BG = 'pink'
    GUI_BG = 'violet'
    gui.configure(background=GUI_BG)
    gui.title("PyShop - Online Shopping")
    gui.geometry("1000x1000")
# Code to add widgets will go here...
#column labels
    colLabel1 =Label(gui, text="Item Name", bg=GUI_BG, font=('', 20))
    colLabel1.grid(row = 1, column = 0)
    colLabel2 = Label(gui, text="Cost", bg=GUI_BG, font=('', 20))
    colLabel2.grid(row = 1, column = 1)
    colLabel3 = Label(gui, text="Quantity", bg=GUI_BG, font=('', 20), width=10)
    colLabel3.grid(row = 1, column = 2)
    colLabel4 = Label(gui, text="Click to Add to Cart", bg=GUI_BG, font=('', 20), width=15)
    colLabel4.grid(row = 1, column = 3)
    for i in range(len(a)):
          itemLabel = Label(gui, text=s[i], bg=GUI_BG, font=('', 15))
          itemLabel.grid(row = i+2, column = 0)
          costLabel = Label(gui, text=int(a[i]), bg=GUI_BG, font=('', 15))
          costLabel.grid(row = i+2, column = 1)
    q=[]
    for i in range(len(a)):
          q.append(Entry(gui))
          q[i].grid(row=2+i, column=2)
#add cart function    
    def add1():
         sstr=""
         for i in range(len(a)):
                  y=q[i].get()
                  if((y!='') and ((int)(q[i].get())>0)):
                         w="select * from product_details where name="+"'"+l[i]+"'"
                         cur.execute(w)
                         qq=cur.fetchall()
                         for i in qq:
                                sstr=sstr+str(i)+"\n"
                                print(i)
         messagebox.showinfo("CART", sstr)

#Command buttons ***** add command to add to cart list **** , command = self._addCart
    for i in range(len(a)):
        addBtn = Button(gui, text = "Add to Cart", fg=FG, bg=BG, font=('', 12))
        addBtn.grid(row = i+2, column = 3)
#Total
#otal= StringVar()
    totalLabel = Label(gui, text="TOTAL: ", bg=GUI_BG, font=('', 20))
    totalLabel.grid(row = 25, column = 1)
    def total1():
        t=0
        for i in range(len(a)):
              ss=q[i].get()
              if(ss!=''):
                     t=t+a[i]*(int)(q[i].get())
        if(t>6000):
            t=t*30/100;
            s="Total amount to be paid including discount of 30%,\n as you shopped for more than Rs 6000: "+ str(t)
        else:
            s="Total amount to be paid "+str(t)
        spacer.configure(text=s)
#Command buttons ***** add command to add to cart list **** , command = self._addCart
    addBtn11 = Button(gui, text = "Total Amount", fg=FG, bg=BG, font=('', 12),command=total1)
    addBtn11.grid(row =20, column = 2)
#view cart
    addBtn11 = Button(gui, text = "View Cart", fg=FG, bg=BG, font=('', 12),command=add1)
    addBtn11.grid(row =21, column = 2)


    spacer = Label(gui, text=" ", bg=GUI_BG, height='6',font=('', 20))
    spacer.grid(row = 25, column = 2)

login2()
gui1.mainloop()
gui.mainloop()
con.close()
