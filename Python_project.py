from tkinter import *
import os,sqlite3
from tkinter import messagebox

root=Tk()

def desk1():
    r1=Tk()
    r1.title("Detail of hospitals")
    r1.minsize(200,200)
    r1.config(bg="red")
    
    l1=Label(r1,text="**INFORMATION OF HOSPITALS**\n",bg="red",fg="black",font="50").pack()
    l2=Label(r1,text="(If you know procced click (YES) otherwise (NO)) ",bg="red",font="50",fg="black").pack(side=TOP)
    b1=Button(r1,text="YES",fg="black",activebackground="red",bg="red",borderwidth=5,relief=GROOVE,font="50",command=desk2)
    b1.pack(side=LEFT)
    b2=Button(r1,text="NO",fg="black",activebackground="red",bg="red",borderwidth=5,relief=GROOVE,font="50",command=ex)
    b2.pack(side=RIGHT)
    
    r1.mainloop()
 
def desk2():
    r2=Tk()

    r2.title("Detail of hospitals")
    r2.minsize(300,300)
    r2.config(bg="red")
    
    l3=Label(r2,text="List of Hospitals Name in Mumbai:\n",bg="yellow",font=("times new roman",15,"bold"),fg="black").pack()

    
    
    var=IntVar()
    rd1=Radiobutton(r2,text="1.Seven Hills ",fg="black",bg="red",activebackground="red",font="50",variable=var,value=1,command=h1).place(x=5,y=60)

    rd2=Radiobutton(r2,text="2.Jeevan jyoti center ",fg="black",activebackground="red",bg="red",font="50",variable=var,value=2,command=h2).place(x=5,y=90)

    rd3=Radiobutton(r2,text="3.Josheph Health center ",fg="black",activebackground="red",bg="red",font="50",variable=var,value=3,command=h3).place(x=5,y=120)

    rd4=Radiobutton(r2,text="4.Blooms Health Hospital ",fg="black",activebackground="red",bg="red",font="50",variable=var,value=4,command=h4).place(x=5,y=150)

    rd5=Radiobutton(r2,text="5.Dreams of Health provision ",fg="black",activebackground="red",bg="red",font="50",variable=var,value=5,command=h5).place(x=5,y=180)
    
    
    b3=Button(r2,text="EXIT",fg="black",activebackground="red",bg="red",borderwidth=5,relief=GROOVE,font="50",command=ex).place(x=240,y=220)
    
    
    r2.mainloop()

def h1():
    r3=Tk()
    r3.config(bg="red")
    r3.title("Detail of hospitals")
    r3.minsize(350,350)    
    l4=Label(r3,text="Detaile of Seven Hills Hospital:\n",bg="red",font=("times new roman",10,"bold")).pack()
    l5=Label(r3,text="Add:Marol farm Road,beside marol bus depo. ",bg="red",fg="black").place(x=8,y=20)
    l6=Label(r3,text="Contact:022231342/0226654624",bg="red",fg="black").place(x=8,y=40)
    l7=Label(r3,text="Treatment:Heart,Cancer patients & more disease etc",bg="red",fg="black").place(x=8,y=60)
    l8=Label(r3,text="Its is second largest hospital of Asia",bg="red",fg="black").place(x=8,y=80)
    l9=Label(r3,text="There are many facilities are providing a unhealthy patients\n________________________________________________________________",bg="red",fg="black").place(x=0,y=100)
    label=Label(r3,text="Specialist of Diseases",fg="black",bg="red",font=("times new roman",10,"bold")).place(x=90,y=140)

    
    
    LABEL=Label(r3,text="1.Cardiologist ",bg="red",fg="black").place(x=10,y=160)
    LABEL1=Label(r3,text="2. Minor Surgion",bg="red",fg="black").place(x=110,y=160)
    LABEL2=Label(r3,text="3. Sycologist",bg="red",fg="black").place(x=230,y=160)
    LABEL3=Label(r3,text="4. Orthologist",bg="red",fg="black").place(x=10,y=190)


    button=Button(r3,text="Book Appointment",activebackground="red",bg="red",font=("times new roman",10),command=ap1,borderwidth=5,relief=GROOVE).place(x=40,y=250)
    button=Button(r3,text="Appointment Cancel",bg="red",activebackground="red",font=("times new roman",10),command=can1,borderwidth=5,relief=GROOVE).place(x=180,y=250)
    
    b4=Button(r3,text="BACK",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=desk2).place(x=8,y=300)
    b5=Button(r3,text="EXIT",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=ex).place(x=300,y=300)

    r3.mainloop()
    
def ap1():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x400")

    PatientName=StringVar()
    gen1=StringVar()
    EmailId=StringVar()
    c=StringVar()
    var1=StringVar()
    Contact=StringVar()
    

    def database():
        messagebox.showinfo("appointment","Your appointment are successfully Done.")
        name1=PatientName.get()
        gender=gen1.get()
        email=EmailId.get()
        contact=Contact.get()
        Specialist=c.get()
        sch=var1.get()
        conn=sqlite3.connect('appointment1.db')
        with conn:
             cursor=conn.cursor()
             cursor.execute('CREATE TABLE IF NOT EXISTS SEVEN(PatientName TEXT,gender TEXT,EmailId TEXT,Contact INT(10),Specialist TEXT,Scheduled TEXT)')
             cursor.execute('INSERT INTO SEVEN(PatientName,gender,EmailId,Contact,Specialist,Scheduled) VALUES(?,?,?,?,?,?)',(name1,gender,email,contact,Specialist,sch))
             conn.commit()
    
   
    lab0=Label(root1,text="Book Appointment",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=45)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=48)
 
    lab1=Label(root1,text="Gender          :",font=("times new roman",15),bg="red",fg="black")
    lab1.place(x=50,y=80)

    gen1=StringVar()
    r1=Radiobutton(root1,text="MALE",variable=gen1,value="MALE",font=("times new roman",10),bg="red",fg="black").place(x=180,y=83)

    r2=Radiobutton(root1,text="FEMALE",variable=gen1,value="FEMALE",font=("times new roman",10),bg="red",fg="black").place(x=260,y=83)

    r3=Radiobutton(root1,text="OTHER",variable=gen1,value="OTHER",font=("times new roman",10),bg="red",fg="black").place(x=360,y=83)
    
    lab2=Label(root1,text="Email Id        :",font=("times new roman",15),bg="red",fg="black")
    lab2.place(x=50,y=120)  

    EmailId=Entry(root1,width=30,borderwidth="2")
    EmailId.place(x=180,y=123)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=160)


    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=163)
   

    lab4=Label(root1,text="Specialist      :",font=("times new roman",15),bg="red",fg="black")
    lab4.place(x=50,y=200)

    list=["Select Option","Cardiologist","Minor surgion","Sycologist","Orthologist"]
    c=StringVar()
    droplist=OptionMenu(root1,c,*list)
    c.set("Select Option")
    droplist.config(bg="red")
    droplist.place(x=180,y=195)

    lab5=Label(root1,text="Scheduled     :",font=("times new roman",15),bg="red",fg="black")
    lab5.place(x=50,y=240)
    
    
    var1=StringVar()
    c1=Radiobutton(root1,text="10:00",variable=var1,value="10:00",bg="red").place(x=180,y=243)


    c2=Radiobutton(root1,text="10:30",variable=var1,value="10:30",bg="red").place(x=250,y=243)


    c3=Radiobutton(root1,text="11:00",variable=var1,value="11:00",bg="red").place(x=320,y=243)


    c4=Radiobutton(root1,text="11:30",variable=var1,value="11:30",bg="red").place(x=180,y=283)

    c5=Radiobutton(root1,text="12:00",variable=var1,value="12:00",bg="red").place(x=250,y=283)



    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,borderwidth="5",command=database).place(x=300,y=333)




    root1.mainloop()

def can1():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x250")

    del1=StringVar()
    
    def dele():
        dee=del1.get()
        connt=sqlite3.connect("appointment1.db")
        cursor=connt.cursor()
        cursor.execute("DELETE FROM SEVEN WHERE PatientName = ?",(dee))
        connt.commit()

    lab0=Label(root1,text="Appointment Cancel",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=80)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=83)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=120)

    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=125)

    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,command=dele,borderwidth="5").place(x=300,y=180)


    root1.mainloop()





def h2():
    r4=Tk()
    r4.config(bg="red")
    
    r4.title("Detail of hospitals")
    r4.minsize(350,350)
    la1=Label(r4,text="Detaile of Jeevan jyoti Hospital:\n",bg="red",font=("times new roman",10,"bold")).pack()
    la2=Label(r4,text="Add:Ghatkopar(East),opp. of railway station. ",bg="red",fg="black").place(x=8,y=20)
    la3=Label(r4,text="Contact:0222334356/022523546624",bg="red",fg="black").place(x=8,y=40)
    L00=Label(r4,text="Treatment:surgery,mine operation,MRI,CT scan & etc.",bg="red",fg="black").place(x=8,y=60)
    la4=Label(r4,text="Hospital facilities are good & more beneficial for patients.",bg="red",fg="black").place(x=8,y=80)         
    la5=Label(r4,text="Providing to much facilities are giving to the patients.             \n_________________________________________________________________",bg="red",fg="black").place(x=8,y=100)
    
    label00=Label(r4,text="Specialist of Diseases",fg="black",bg="red",font=("times new roman",10,"bold")).place(x=90,y=140)
    
    LABE=Label(r4,text="1.Pathologist ",bg="red",fg="black").place(x=10,y=160)
    LABE1=Label(r4,text="2. Plastic Surgion",bg="red",fg="black").place(x=110,y=160)
    LABE2=Label(r4,text="3. Vascular Surgion",bg="red",fg="black").place(x=230,y=160)
    LABE3=Label(r4,text="4. Radiologist",bg="red",fg="black").place(x=10,y=190)


    button=Button(r4,text="Book Appointment",activebackground="red",bg="red",font=("times new roman",10),command=ap2,borderwidth=5,relief=GROOVE).place(x=40,y=250)
    button=Button(r4,text="Appointment Cancel",bg="red",activebackground="red",font=("times new roman",10),command=can2,borderwidth=5,relief=GROOVE).place(x=180,y=250)

    b6=Button(r4,text="BACK",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=desk2).place(x=8,y=300)
    b7=Button(r4,text="EXIT",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=ex).place(x=300,y=300)
    r4.mainloop()
    
def ap2():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x400")

    PatientName=StringVar()
    gen1=StringVar()
    EmailId=StringVar()
    c=StringVar()
    var1=StringVar()
    Contact=StringVar()
    def database():
        messagebox.showinfo("appointment","Your appointment are successfully Done.")
        name1=PatientName.get()
        gender=gen1.get()
        email=EmailId.get()
        contact=Contact.get()
        Specialist=c.get()
        sch=var1.get()
        conn=sqlite3.connect('appointment1.db')
        with conn:
             cursor=conn.cursor()
             cursor.execute('CREATE TABLE IF NOT EXISTS JEEVAN(PatientName TEXT,gender TEXT,EmailId TEXT,Contact INT(10),Specialist TEXT,Scheduled TEXT)')
             cursor.execute('INSERT INTO JEEVAN(PatientName,gender,EmailId,Contact,Specialist,Scheduled) VALUES(?,?,?,?,?,?)',(name1,gender,email,contact,Specialist,sch))
             conn.commit()
    
 
    lab0=Label(root1,text="Book Appointment",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=45)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=48)
 
    lab1=Label(root1,text="Gender          :",font=("times new roman",15),bg="red",fg="black")
    lab1.place(x=50,y=80)

    gen1=StringVar()
    r1=Radiobutton(root1,text="MALE",variable=gen1,value="MALE",font=("times new roman",10),bg="red",fg="black").place(x=180,y=83)
    
    r2=Radiobutton(root1,text="FEMALE",variable=gen1,value="FEMALE",font=("times new roman",10),bg="red",fg="black").place(x=260,y=83)

    r3=Radiobutton(root1,text="OTHER",variable=gen1,value="OTHER",font=("times new roman",10),bg="red",fg="black").place(x=360,y=83)
    
    lab2=Label(root1,text="Email Id        :",font=("times new roman",15),bg="red",fg="black")
    lab2.place(x=50,y=120)  

    EmailId=Entry(root1,width=30,borderwidth="2")
    EmailId.place(x=180,y=123)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=160)


    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=163)
   

    lab4=Label(root1,text="Specialist      :",font=("times new roman",15),bg="red",fg="black")
    lab4.place(x=50,y=200)

    list=["Select Option","Pathologist","Plastic Surgion","Vascular Surgion","Radiologist"]
    c=StringVar()
    droplist=OptionMenu(root1,c,*list)
    c.set("Select Option")
    droplist.config(bg="red")
    droplist.place(x=180,y=195)

    lab5=Label(root1,text="Scheduled     :",font=("times new roman",15),bg="red",fg="black")
    lab5.place(x=50,y=240)
    

    var1=StringVar()
    c1=Radiobutton(root1,text="10:00",variable=var1,value="10:00",bg="red").place(x=180,y=243)


    c2=Radiobutton(root1,text="10:30",variable=var1,value="10:30",bg="red").place(x=250,y=243)


    c3=Radiobutton(root1,text="11:00",variable=var1,value="11:00",bg="red").place(x=320,y=243)

    
    c4=Radiobutton(root1,text="11:30",variable=var1,value="11:30",bg="red").place(x=180,y=283)


    c5=Radiobutton(root1,text="12:00",variable=var1,value="12:00",bg="red").place(x=250,y=283)



    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,borderwidth="5",command=database).place(x=300,y=333)


    root1.mainloop()


def can2():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x250")

    del1=StringVar()
    
    def dele():
        dee=del1.get()
        connt=sqlite3.connect("appointment1.db")
        cursor=connt.cursor()
        cursor.execute("DELETE FROM JEEVAN WHERE PatientName = ?",(dee))
        connt.commit()

    lab0=Label(root1,text="Appointment Cancel",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=80)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=83)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=120)

    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=125)

    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,command=dele,borderwidth="5").place(x=300,y=180)


    root1.mainloop()







def h3():
    r5=Tk()
    r5.config(bg="red")
   
    r5.title("Detail of hospitals")
    r5.minsize(350,350)
    la6=Label(r5,text="Detaile of Josheph Health Center:\n",bg="red",font=("times new roman",10,"bold")).pack()
    la7=Label(r5,text="Add:Bandra (east) front of marine line. ",bg="red",fg="black").place(x=8,y=20)
    la8=Label(r5,text="Contact:0222334356/022523546624",bg="red",fg="black").place(x=8,y=40)
    la008=Label(r5,text="Treatment:Heart,MRI,CTScan & Blood pressure more.",bg="red",fg="black").place(x=8,y=60)
    la9=Label(r5,text="Hospital facilities are provide luxary & stable os patients.",bg="red",fg="black").place(x=8,y=80)         
    la0=Label(r5,text="Providing to much effort of patients for free of diseases.         \n_________________________________________________________________",bg="red",fg="black").place(x=8,y=100)




    labe200=Label(r5,text="Specialist of Diseases",fg="black",bg="red",font=("times new roman",10,"bold")).place(x=90,y=140)
    
    LAB=Label(r5,text="1.Cardiologist ",bg="red",fg="black").place(x=10,y=160)
    LAB1=Label(r5,text="2. Pariodontist",bg="red",fg="black").place(x=110,y=160)
    LAB2=Label(r5,text="3. SpinalCord specialist ",bg="red",fg="black").place(x=220,y=160)
    LAB3=Label(r5,text="4. Major Surgion",bg="red",fg="black").place(x=10,y=190)


    button=Button(r5,text="Book Appointment",bg="red",activebackground="red",font=("times new roman",10),command=ap3,borderwidth=5,relief=GROOVE).place(x=40,y=250)
    button=Button(r5,text="Appointment Cancel",bg="red",activebackground="red",font=("times new roman",10),command=can3,borderwidth=5,relief=GROOVE).place(x=180,y=250)
    
    b8=Button(r5,text="BACK",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=desk2).place(x=8,y=300)
    b9=Button(r5,text="EXIT",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=ex).place(x=300,y=300)

    r5.mainloop()


def ap3():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x400")

    PatientName=StringVar()
    gen=StringVar()
    EmailId=StringVar()
    c=StringVar()
    var=StringVar()
    Contact=StringVar()

    def database():
        messagebox.showinfo("appointment","Your appointment are successfully Done.")
        name1=PatientName.get()
        gender=gen.get()
        email=EmailId.get()
        contact=Contact.get()
        Specialist=c.get()
        sch=var.get()
        conn=sqlite3.connect('appointment1.db')
        with conn:
             cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS JOSHEPH(PatientName TEXT,gender TEXT,EmailId TEXT,Contact INT(10),Specialist TEXT,Scheduled TEXT)')
        cursor.execute('INSERT INTO JOSHEPH(PatientName,gender,EmailId,Contact,Specialist,Scheduled) VALUES(?,?,?,?,?,?)',(name1,gender,email,contact,Specialist,sch))
        conn.commit()
    
   
    lab0=Label(root1,text="Book Appointment",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=45)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=48)
 
    lab1=Label(root1,text="Gender          :",font=("times new roman",15),bg="red",fg="black")
    lab1.place(x=50,y=80)

    gen=StringVar()
    r1=Radiobutton(root1,text="MALE",variable=gen,value="MALE",font=("times new roman",10),bg="red",fg="black").place(x=180,y=83)

    r2=Radiobutton(root1,text="FEMALE",variable=gen,value="FEMALE",font=("times new roman",10),bg="red",fg="black").place(x=260,y=83)

    r3=Radiobutton(root1,text="OTHER",variable=gen,value="OTHER",font=("times new roman",10),bg="red",fg="black").place(x=360,y=83)
    
    lab2=Label(root1,text="Email Id        :",font=("times new roman",15),bg="red",fg="black")
    lab2.place(x=50,y=120)  

    EmailId=Entry(root1,width=30,borderwidth="2")
    EmailId.place(x=180,y=123)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=160)


    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=163)
   

    lab4=Label(root1,text="Specialist      :",font=("times new roman",15),bg="red",fg="black")
    lab4.place(x=50,y=200)

    list=["Select Option","Cardiologist","Pariodontist","SpinalCord specialist"," Major Surgion"]
    c=StringVar()
    droplist=OptionMenu(root1,c,*list)
    c.set("Select Option")
    droplist.config(bg="red")
    droplist.place(x=180,y=195)

    lab5=Label(root1,text="Scheduled     :",font=("times new roman",15),bg="red",fg="black")
    lab5.place(x=50,y=240)

    var=StringVar()
    c1=Radiobutton(root1,text="10:00",variable=var,value="10:00",bg="red").place(x=180,y=243)


    c2=Radiobutton(root1,text="10:30",variable=var,value="10:30",bg="red").place(x=250,y=243)


    c3=Radiobutton(root1,text="11:00",variable=var,value="11:00",bg="red").place(x=320,y=243)


    c4=Radiobutton(root1,text="11:30",variable=var,value="11:30",bg="red").place(x=180,y=283)


    c5=Radiobutton(root1,text="12:00",variable=var,value="12:00",bg="red").place(x=250,y=283)



    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,borderwidth="5",command=database).place(x=300,y=333)




    root1.mainloop()


def can3():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x250")

    del1=StringVar()
    
    def dele():
        dee=del1.get()
        connt=sqlite3.connect("appointment1.db")
        cursor=connt.cursor()
        cursor.execute("DELETE FROM JOSHEPH WHERE PatientName = ?",(dee))
        connt.commit()

    lab0=Label(root1,text="Appointment Cancel",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=80)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=83)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=120)

    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=125)

    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,command=dele,borderwidth="5").place(x=300,y=180)


    root1.mainloop()






def h4():
    r6=Tk()
    r6.config(bg="red")
   
    r6.title("Detail of hospitals")
    r6.minsize(350,350)
    lab1=Label(r6,text="Detaile of Blooms Health Hospital:\n",bg="red",font=("times new roman",10,"bold")).pack()
    lab2=Label(r6,text="Add:Wadala(East) near by wadala post office. ",bg="red",fg="black").place(x=8,y=20)
    lab3=Label(r6,text="Contact:02226756356/0225233765624",bg="red",fg="black").place(x=8,y=40)
    lab4=Label(r6,text="hospital facilities & Discount are also available of all patients.",bg="red",fg="black").place(x=8,y=60)         
    lab5=Label(r6,text="some patients are free treatment but(terms & condition apply).",bg="red",fg="black").place(x=8,y=80)
    la3=Label(r6,text="Treatment: kidney operatio/heart operation/ect.                      \n________________________________________________________________",bg="red",fg="black").place(x=8,y=100)

    labe200=Label(r6,text="Specialist of Diseases",bg="red",fg="black",font=("times new roman",10,"bold")).place(x=90,y=140)
    
    LAB=Label(r6,text="1.Plastic sugion ",bg="red",fg="black").place(x=10,y=160)
    LAB1=Label(r6,text="2. Pulmonologist",bg="red",fg="black").place(x=110,y=160)
    LAB2=Label(r6,text="3. Sycologist ",bg="red",fg="black").place(x=230,y=160)
    LAB3=Label(r6,text="4. orthologist",bg="red",fg="black").place(x=10,y=190)


    button=Button(r6,text="Book Appointment",bg="red",activebackground="red",font=("times new roman",10),command=ap4,borderwidth=5,relief=GROOVE).place(x=40,y=250)
    button=Button(r6,text="Appointment Cancel",bg="red",activebackground="red",font=("times new roman",10),command=can4,borderwidth=5,relief=GROOVE).place(x=180,y=250)

    b10=Button(r6,text="BACK",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=desk2).place(x=8,y=300)
    b11=Button(r6,text="EXIT",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=ex).place(x=300,y=300)

    r6.mainloop()


def ap4():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x400")

    PatientName=StringVar()
    gen=StringVar()
    EmailId=StringVar()
    c=StringVar()
    var=StringVar()
    Contact=StringVar()

    def database():
        messagebox.showinfo("appointment","Your appointment are successfully Done.")
        name1=PatientName.get()
        gender=gen.get()
        email=EmailId.get()
        contact=Contact.get()
        Specialist=c.get()
        sch=var.get()
        conn=sqlite3.connect('appointment1.db')
        with conn:
             cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS BLOOMS(PatientName TEXT,gender TEXT,EmailId TEXT,Contact INT(10),Specialist TEXT,Scheduled TEXT)')
        cursor.execute('INSERT INTO BLOOMS(PatientName,gender,EmailId,Contact,Specialist,Scheduled) VALUES(?,?,?,?,?,?)',(name1,gender,email,contact,Specialist,sch))
        conn.commit()
    
   
    lab0=Label(root1,text="Book Appointment",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=45)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=48)
 
    lab1=Label(root1,text="Gender          :",font=("times new roman",15),bg="red",fg="black")
    lab1.place(x=50,y=80)

    gen=StringVar()
    r1=Radiobutton(root1,text="MALE",variable=gen,value="MALE",font=("times new roman",10),bg="red",fg="black").place(x=180,y=83)

    r2=Radiobutton(root1,text="FEMALE",variable=gen,value="FEMALE",font=("times new roman",10),bg="red",fg="black").place(x=260,y=83)

    r3=Radiobutton(root1,text="OTHER",variable=gen,value="OTHER",font=("times new roman",10),bg="red",fg="black").place(x=360,y=83)
    
    lab2=Label(root1,text="Email Id        :",font=("times new roman",15),bg="red",fg="black")
    lab2.place(x=50,y=120)  

    EmailId=Entry(root1,width=30,borderwidth="2")
    EmailId.place(x=180,y=123)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=160)


    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=163)
   

    lab4=Label(root1,text="Specialist      :",font=("times new roman",15),bg="red",fg="black")
    lab4.place(x=50,y=200)

    list=["Select Option","Plastic sugion","Pulmonologist","Sycologist"," orthologist"]
    c=StringVar()
    droplist=OptionMenu(root1,c,*list)
    c.set("Select Option")
    droplist.config(bg="red")
    droplist.place(x=180,y=195)

    lab5=Label(root1,text="Scheduled     :",font=("times new roman",15),bg="red",fg="black")
    lab5.place(x=50,y=240)

    var=StringVar()
    c1=Radiobutton(root1,text="10:00",variable=var,value="10:00",bg="red").place(x=180,y=243)


    c2=Radiobutton(root1,text="10:30",variable=var,value="10:30",bg="red").place(x=250,y=243)


    c3=Radiobutton(root1,text="11:00",variable=var,value="11:00",bg="red").place(x=320,y=243)


    c4=Radiobutton(root1,text="11:30",variable=var,value="11:30",bg="red").place(x=180,y=283)


    c5=Radiobutton(root1,text="12:00",variable=var,value="12:00",bg="red").place(x=250,y=283)



    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,borderwidth="5",command=database).place(x=300,y=333)




    root1.mainloop()


def can4():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x250")

    del1=StringVar()
    
    def dele():
        dee=del1.get()
        connt=sqlite3.connect("appointment1.db")
        cursor=connt.cursor()
        cursor.execute("DELETE FROM BLOOMS WHERE PatientName = ?",(dee))
        connt.commit()

    lab0=Label(root1,text="Appointment Cancel",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=80)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=83)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=120)

    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=125)

    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,command=dele,borderwidth="5").place(x=300,y=180)


    root1.mainloop()







def h5():
    r7=Tk()
    r7.config(bg="red")
   
    r7.title("Detail of hospitals")
    r7.minsize(350,350)
    lab6=Label(r7,text="Detaile of Dreams of Health Provision:\n",bg="red",font=("times new roman",10,"bold")).pack()
    lab7=Label(r7,text="Add:Panvel(East) near by police station ",bg="red",fg="black").place(x=8,y=20)
    lab8=Label(r7,text="Contact:022465754556/02252345637624",bg="red",fg="black").place(x=8,y=40)
    lab9=Label(r7,text="Hospital geting so much effort for treatment for patients",bg="red",fg="black").place(x=8,y=60)         
    lab0=Label(r7,text="Treatment:mine surgery/kidney operation/heart operation",bg="red",fg="black").place(x=8,y=80)
    la=Label(r7,text="The Aim are to giving to more (best) Treatment to the patients.\n__________________________________________________________________",bg="red",fg="black").place(x=8,y=100)
    labe300=Label(r7,text="Specialist of Diseases",bg="red",fg="black",font=("times new roman",10,"bold")).place(x=90,y=140)
    
    LA=Label(r7,text="1.Cardiologist ",bg="red",fg="black").place(x=10,y=160)
    LA1=Label(r7,text="2. Pulmonologist",bg="red",fg="black").place(x=110,y=160)
    LA2=Label(r7,text="3. Major Surgury ",bg="red",fg="black").place(x=230,y=160)
    LA3=Label(r7,text="4. orthoDontist",bg="red",fg="black").place(x=10,y=190)

    button=Button(r7,text="Book Appointment",bg="red",activebackground="red",font=("times new roman",10),command=ap5,borderwidth=5,relief=GROOVE).place(x=40,y=250)
    button=Button(r7,text="Appointment Cancel",bg="red",activebackground="red",font=("times new roman",10),command=can5,borderwidth=5,relief=GROOVE).place(x=180,y=250)

    
    b12=Button(r7,text="BACK",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=desk2).place(x=8,y=300)
    b13=Button(r7,text="EXIT",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,command=ex).place(x=300,y=300)
    
    r7.mainloop()



def ap5():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x400")

    PatientName=StringVar()
    gen=StringVar()
    EmailId=StringVar()
    c=StringVar()
    var=StringVar()
    Contact=StringVar()

    def database():
        messagebox.showinfo("appointment","Your appointment are successfully Done.")
        name1=PatientName.get()
        gender=gen.get()
        email=EmailId.get()
        contact=Contact.get()
        Specialist=c.get()
        sch=var.get()
        conn=sqlite3.connect('appointment1.db')
        with conn:
             cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS DREAMS(PatientName TEXT,gender TEXT,EmailId TEXT,Contact INT(10),Specialist TEXT,Scheduled TEXT)')
        cursor.execute('INSERT INTO DREAMS(PatientName,gender,EmailId,Contact,Specialist,Scheduled) VALUES(?,?,?,?,?,?)',(name1,gender,email,contact,Specialist,sch))
        conn.commit()
    
   
    lab0=Label(root1,text="Book Appointment",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=45)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=48)
 
    lab1=Label(root1,text="Gender          :",font=("times new roman",15),bg="red",fg="black")
    lab1.place(x=50,y=80)

    gen=StringVar()
    r1=Radiobutton(root1,text="MALE",variable=gen,value="MALE",font=("times new roman",10),bg="red",fg="black").place(x=180,y=83)

    r2=Radiobutton(root1,text="FEMALE",variable=gen,value="FEMALE",font=("times new roman",10),bg="red",fg="black").place(x=260,y=83)

    r3=Radiobutton(root1,text="OTHER",variable=gen,value="OTHER",font=("times new roman",10),bg="red",fg="black").place(x=360,y=83)
    
    lab2=Label(root1,text="Email Id        :",font=("times new roman",15),bg="red",fg="black")
    lab2.place(x=50,y=120)  

    EmailId=Entry(root1,width=30,borderwidth="2")
    EmailId.place(x=180,y=123)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=160)


    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=163)
   

    lab4=Label(root1,text="Specialist      :",font=("times new roman",15),bg="red",fg="black")
    lab4.place(x=50,y=200)

    list=["Select Option","Cardiologist","Pulmonologist","Major Surgury"," orthoDontist"]
    c=StringVar()
    droplist=OptionMenu(root1,c,*list)
    c.set("Select Option")
    droplist.config(bg="red")
    droplist.place(x=180,y=195)

    lab5=Label(root1,text="Scheduled     :",font=("times new roman",15),bg="red",fg="black")
    lab5.place(x=50,y=240)

    var=StringVar()
    c1=Radiobutton(root1,text="10:00",variable=var,value="10:00",bg="red").place(x=180,y=243)


    c2=Radiobutton(root1,text="10:30",variable=var,value="10:30",bg="red").place(x=250,y=243)


    c3=Radiobutton(root1,text="11:00",variable=var,value="11:00",bg="red").place(x=320,y=243)


    c4=Radiobutton(root1,text="11:30",variable=var,value="11:30",bg="red").place(x=180,y=283)


    c5=Radiobutton(root1,text="12:00",variable=var,value="12:00",bg="red").place(x=250,y=283)



    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,borderwidth="5",command=database).place(x=300,y=333)




    root1.mainloop()

def can5():
    root1=Tk()
    root1.config(bg="red")
    root1.geometry("500x250")

    del1=StringVar()
    
    def dele():
        dee=del1.get()
        connt=sqlite3.connect("appointment1.db")
        cursor=connt.cursor()
        cursor.execute("DELETE FROM DREAMS WHERE PatientName = ?",(dee))
        connt.commit()

    lab0=Label(root1,text="Appointment Cancel",relief=GROOVE,font=("times new roman",25,"bold"),bg="yellow",fg="black")
    lab0.place(x=0,y=0,relwidth=1)

    lab01=Label(root1,text="Patient Name :",font=("times new roman",15),bg="red",fg="black")
    lab01.place(x=50,y=80)

    PatientName=Entry(root1,width=30,borderwidth="2")
    PatientName.place(x=180,y=83)


    lab3=Label(root1,text="Contact no.    :",font=("times new roman",15),bg="red",fg="black")
    lab3.place(x=50,y=120)

    Contact=Entry(root1,width=30,borderwidth="2")
    Contact.place(x=180,y=125)

    b1=Button(root1,text="Submit",font=("times new roman",15,"bold"),bg="red",width="10",relief=GROOVE,command=dele,borderwidth="5").place(x=300,y=180)


    root1.mainloop()






       
def ex():
    quit()
    
b000=Button(root,text="ENTER",bg="red",fg="black",activebackground="red",borderwidth=5,relief=GROOVE,font="10",command=desk1).pack()
root.mainloop()












