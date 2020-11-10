import tkinter as tk
from tkinter import Text #TO DISPLAY TEXT AND ACCEPT TEXT INPUT
#from PIL import ImageTk, Image
import os #additional requirements
import winsound
from tkinter import messagebox
import time
import mysql.connector
import smtplib


winsound.PlaySound(os.getcwd()+"\Hans Zimmer - Chevaliers de Sangreal.wav", winsound.SND_LOOP+winsound.SND_ASYNC)
mycon = mysql.connector.connect(host = 'localhost', user = '', passwd = '')
cursor = mycon.cursor()

def Append(L):
    message = '''We have recognised that you are facing issues
The issues that you have reported are: '''+str(L[3])+'''
We hope that you are currently doing okay and are in a slightly stable environment as you read this.
We wish to tell you that you are not alone. There are people that you can talk to. Though it may seem like a massive hurdle at first, we hope we can help you take the first step in overcoming your problems so that you may live upto your full potential.
We wish that your times get better from here on.

Sincerely,
Team Soluchan
'''
    return message

def DOMESTIC_V_WIN():
    LIST_OF_VALUES=[]  ### SAM, THIS IS THE LIST WHERE ALL THE INPUT FROM THE USER IS STORED. THE ELEMENTS ARE STORED IN THE ORDER NAME, PHONE NUMBER, EMAIL, ISSUES. ALL ARE TEXT FORMS. KINDLY DO ALL STUFF THAT YOU NEED TO ONLY ON THIS LIST, AND DONT DESTROY MY CODE :P.
    #PLEASE MAKE SURE THAT ALL CHANGES AND MANIPULATIONS YOU NEED TO DO ARE DONE UNDER A FUNCTION WHICH YOU CAN DEFINE AFTER POPUP(). JUST DEFINE THE FUNCTION. LEAVE THE CALLING AND WORKING OF THE FUNCTION TO ME
    def ENTERING_NAME():
        NAME= NAMEBOX.get()
        LIST_OF_VALUES.append(NAME)
    def ENTERING_PHONE_NUMBER():
        NUMBER=PHONE.get()
        LIST_OF_VALUES.append(NUMBER) 
    def ENTERING_EMAIL():
        E_mail=EMAIL.get()
        LIST_OF_VALUES.append(E_mail)
    def ENTERING_ISSUES():
        Issues= ISSUES.get()
        LIST_OF_VALUES.append(Issues)
    def popup():
        messagebox.showinfo("CONGRATULATIONS",'THANK YOU FOR REACHING OUT TO US. WE SYMPATHISE WITH YOUR PROBLEMS AND WILL TRY OUR BEST TO LINK YOU WITH OTHERS WHO FACE THE SAME ISSUES. KINDLY CHECK YOUR MAIL FOR FURTHER INFORMATION')
    DOMESTIC_WIN=tk.Toplevel()
    DOMESTIC_WIN.title("DOMESTIC VIOLENCE AID")
    width= DOMESTIC_WIN.winfo_screenwidth()
    height= DOMESTIC_WIN.winfo_screenheight()
    bgimage1= tk.PhotoImage(file=os.getcwd()+"\DOMESTIC_VIOLENCE.png")
    tk.Label(DOMESTIC_WIN,image= bgimage1).place(relwidth=1, relheight=1)
    name=tk.StringVar(None)
    NAMEBOX= tk.Entry(DOMESTIC_WIN,textvariable=name,width=50)
    NAMEBOX.place(x=150,y=50)
    namebox=tk.Button(DOMESTIC_WIN,text="NAME",state='disabled',fg='blue',bg='white').place(x=25,y=50)
    phone=tk.StringVar(None)
    PHONE= tk.Entry(DOMESTIC_WIN,textvariable=phone,width=50)
    PHONE.place(x=150,y=150)
    #PHONE.insert(0,"PHONE: ")
    phonebox=tk.Button(DOMESTIC_WIN,text="PHONENUMBER",state='disabled',fg='blue',bg='white').place(x=25,y=150)
    Email=tk.StringVar(None)
    EMAIL= tk.Entry(DOMESTIC_WIN,textvariable=Email,width=50)
    EMAIL.place(x=150,y=250)
    emailbox=tk.Button(DOMESTIC_WIN,text="EMAIL",state='disabled',fg='blue',bg='white').place(x=25,y=250)
    issues=tk.StringVar(None)
    ISSUES= tk.Entry(DOMESTIC_WIN,textvariable=issues,width=50)
    ISSUES.place(x=150,y=350)
    issuesbox=tk.Button(DOMESTIC_WIN,text="ISSUES",state='disabled',fg='blue',bg='white').place(x=20,y=350)
    enterbutton= tk.Button(DOMESTIC_WIN,height=2,width=50,text='SUBMIT DETAILS',command=lambda:[ENTERING_NAME(),ENTERING_PHONE_NUMBER(),ENTERING_EMAIL(),ENTERING_ISSUES(),popup(),DOMESTIC_WIN.destroy()]).place(x=200,y=750)
    DOMESTIC_WIN.mainloop()
    global cursor
    s = 'insert into domestic_violence(' + LIST_OF_VALUES[0] + ', ' + LIST_OF_VALUES[1] + ', ' + LIST_OF_VALUES[2] + ', ' + LIST_OF_VALUES[3])
    cursor.execute(s)
    sender = 'soluchanbyasy62636@gmail.com'
    receivers = ['samhruth@gmail.com', 'adk91215@gmail.com']
    subject = '(no-reply) Team Soluchan welcomes you'


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('soluchanbyasy62636@gmail.com', 'We<3Yashas')
        server.sendmail(sender, receivers, subject, Append(LIST_OF_VALUES))         
        print ("Successfully sent email")
    except smtplib.SMTPException:
        print('Unable to send mail')
    
def ANIMAL_A_WIN():
    LIST_OF_VALUES=[]
    ### SAM, THIS IS THE LIST WHERE ALL THE INPUT FROM THE USER IS STORED. THE ELEMENTS ARE STORED IN THE ORDER NAME, PHONE NUMBER, EMAIL, ISSUES. ALL ARE TEXT FORMS. KINDLY DO ALL STUFF THAT YOU NEED TO ONLY ON THIS LIST, AND DONT DESTROY MY CODE :P
    #PLEASE MAKE SURE THAT ALL CHANGES AND MANIPULATIONS YOU NEED TO DO ARE DONE UNDER A FUNCTION WHICH YOU CAN DEFINE AFTER POPUP(). JUST DEFINE THE FUNCTION. LEAVE THE CALLING AND WORKING OF THE FUNCTION TO ME
    def ENTERING_NAME():
        NAME= NAMEBOX.get()
        LIST_OF_VALUES.append(NAME)
    def ENTERING_PHONE_NUMBER():
        NUMBER=PHONE.get()
        LIST_OF_VALUES.append(NUMBER) 
    def ENTERING_EMAIL():
        E_mail=EMAIL.get()
        LIST_OF_VALUES.append(E_mail)
    def ENTERING_ISSUES():
        Issues= ISSUES.get()
        LIST_OF_VALUES.append(Issues)
    def popup():
        messagebox.showinfo("CONGRATULATIONS",'THANK YOU FOR REACHING OUT TO US. WE SYMPATHISE WITH YOUR PROBLEMS AND WILL TRY OUR BEST TO LINK YOU WITH OTHERS WHO FACE THE SAME ISSUES. KINDLY CHECK YOUR MAIL FOR FURTHER INFORMATION')
    DOMESTIC_WIN=tk.Toplevel()
    DOMESTIC_WIN.title("ANIMAL ABUSE AID")
    width= DOMESTIC_WIN.winfo_screenwidth()
    height= DOMESTIC_WIN.winfo_screenheight()
    bgimage1= tk.PhotoImage(file=os.getcwd()+"\ANIMAL ABUSE.png")
    tk.Label(DOMESTIC_WIN,image= bgimage1).place(relwidth=1, relheight=1)
    name=tk.StringVar(None)
    NAMEBOX= tk.Entry(DOMESTIC_WIN,textvariable=name,width=50)
    NAMEBOX.place(x=150,y=50)
    namebox=tk.Button(DOMESTIC_WIN,text="NAME",state='disabled',fg='blue',bg='white').place(x=25,y=50)
    phone=tk.StringVar(None)
    PHONE= tk.Entry(DOMESTIC_WIN,textvariable=phone,width=50)
    PHONE.place(x=150,y=150)
    #PHONE.insert(0,"PHONE: ")
    phonebox=tk.Button(DOMESTIC_WIN,text="PHONENUMBER",state='disabled',fg='blue',bg='white').place(x=25,y=150)
    Email=tk.StringVar(None)
    EMAIL= tk.Entry(DOMESTIC_WIN,textvariable=Email,width=50)
    EMAIL.place(x=150,y=250)
    emailbox=tk.Button(DOMESTIC_WIN,text="EMAIL",state='disabled',fg='blue',bg='white').place(x=25,y=250)
    issues=tk.StringVar(None)
    ISSUES= tk.Entry(DOMESTIC_WIN,textvariable=issues,width=50)
    ISSUES.place(x=150,y=350)
    issuesbox=tk.Button(DOMESTIC_WIN,text="ISSUES",state='disabled',fg='blue',bg='white').place(x=20,y=350)
    enterbutton= tk.Button(DOMESTIC_WIN,height=2,width=50,text='SUBMIT DETAILS',command=lambda:[ENTERING_NAME(),ENTERING_PHONE_NUMBER(),ENTERING_EMAIL(),ENTERING_ISSUES(),popup(),DOMESTIC_WIN.destroy()]).place(x=200,y=750)
    DOMESTIC_WIN.mainloop()
    global cursor
    s = 'insert into animal_abuse(' + LIST_OF_VALUES[0] + ', ' + LIST_OF_VALUES[1] + ', ' + LIST_OF_VALUES[2] + ', ' + LIST_OF_VALUES[3])
    cursor.execute(s)
    sender = 'soluchanbyasy62636@gmail.com'
    receivers = ['samhruth@gmail.com', 'adk91215@gmail.com']
    subject = '(no-reply) Team Soluchan welcomes you'


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('soluchanbyasy62636@gmail.com', 'We<3Yashas')
        server.sendmail(sender, receivers, subject, Append(LIST_OF_VALUES))         
        print ("Successfully sent email")
    except smtplib.SMTPException:
        print('Unable to send mail')

def ADDICTION_H_WIN():
    LIST_OF_VALUES=[]
    ### SAM, THIS IS THE LIST WHERE ALL THE INPUT FROM THE USER IS STORED. THE ELEMENTS ARE STORED IN THE ORDER NAME, PHONE NUMBER, EMAIL, ISSUES. ALL ARE TEXT FORMS. KINDLY DO ALL STUFF THAT YOU NEED TO ONLY ON THIS LIST, AND DONT DESTROY MY CODE :P
    #PLEASE MAKE SURE THAT ALL CHANGES AND MANIPULATIONS YOU NEED TO DO ARE DONE UNDER A FUNCTION WHICH YOU CAN DEFINE AFTER POPUP(). JUST DEFINE THE FUNCTION. LEAVE THE CALLING AND WORKING OF THE FUNCTION TO ME

    def ENTERING_NAME():
        NAME= NAMEBOX.get()
        LIST_OF_VALUES.append(NAME)
    def ENTERING_PHONE_NUMBER():
        NUMBER=PHONE.get()
        LIST_OF_VALUES.append(NUMBER) 
    def ENTERING_EMAIL():
        E_mail=EMAIL.get()
        LIST_OF_VALUES.append(E_mail)
    def ENTERING_ISSUES():
        Issues= ISSUES.get()
        LIST_OF_VALUES.append(Issues)
    def popup():
        messagebox.showinfo("CONGRATULATIONS",'THANK YOU FOR REACHING OUT TO US. WE SYMPATHISE WITH YOUR PROBLEMS AND WILL TRY OUR BEST TO LINK YOU WITH OTHERS WHO FACE THE SAME ISSUES. KINDLY CHECK YOUR MAIL FOR FURTHER INFORMATION')
    DOMESTIC_WIN=tk.Toplevel()
    DOMESTIC_WIN.title("ADDICTION AID")
    width= DOMESTIC_WIN.winfo_screenwidth()
    height= DOMESTIC_WIN.winfo_screenheight()
    bgimage1= tk.PhotoImage(file=os.getcwd()+"\ADDICTION.png")
    tk.Label(DOMESTIC_WIN,image= bgimage1).place(relwidth=1, relheight=1)
    name=tk.StringVar(None)
    NAMEBOX= tk.Entry(DOMESTIC_WIN,textvariable=name,width=50)
    NAMEBOX.place(x=150,y=50)
    namebox=tk.Button(DOMESTIC_WIN,text="NAME",state='disabled',fg='blue',bg='white').place(x=25,y=50)
    phone=tk.StringVar(None)
    PHONE= tk.Entry(DOMESTIC_WIN,textvariable=phone,width=50)
    PHONE.place(x=150,y=150)
    #PHONE.insert(0,"PHONE: ")
    phonebox=tk.Button(DOMESTIC_WIN,text="PHONENUMBER",state='disabled',fg='blue',bg='white').place(x=25,y=150)
    Email=tk.StringVar(None)
    EMAIL= tk.Entry(DOMESTIC_WIN,textvariable=Email,width=50)
    EMAIL.place(x=150,y=250)
    emailbox=tk.Button(DOMESTIC_WIN,text="EMAIL",state='disabled',fg='blue',bg='white').place(x=25,y=250)
    issues=tk.StringVar(None)
    ISSUES= tk.Entry(DOMESTIC_WIN,textvariable=issues,width=50)
    ISSUES.place(x=150,y=350)
    issuesbox=tk.Button(DOMESTIC_WIN,text="ISSUES",state='disabled',fg='blue',bg='white').place(x=20,y=350)
    enterbutton= tk.Button(DOMESTIC_WIN,height=2,width=50,text='SUBMIT DETAILS',command=lambda:[ENTERING_NAME(),ENTERING_PHONE_NUMBER(),ENTERING_EMAIL(),ENTERING_ISSUES(),popup(),DOMESTIC_WIN.destroy()]).place(x=200,y=750)
    DOMESTIC_WIN.mainloop()
    global cursor
    s = 'insert into addiction(' + LIST_OF_VALUES[0] + ', ' + LIST_OF_VALUES[1] + ', ' + LIST_OF_VALUES[2] + ', ' + LIST_OF_VALUES[3])
    cursor.execute(s)
    sender = 'soluchanbyasy62636@gmail.com'
    receivers = ['samhruth@gmail.com', 'adk91215@gmail.com']
    subject = '(no-reply) Team Soluchan welcomes you'


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('soluchanbyasy62636@gmail.com', 'We<3Yashas')
        server.sendmail(sender, receivers, subject, Append(LIST_OF_VALUES))         
        print ("Successfully sent email")
    except smtplib.SMTPException:
        print('Unable to send mail')
    
def FINANCIAL_A_WIN():
    LIST_OF_VALUES=[]
    ### SAM, THIS IS THE LIST WHERE ALL THE INPUT FROM THE USER IS STORED. THE ELEMENTS ARE STORED IN THE ORDER NAME, PHONE NUMBER, EMAIL, ISSUES. ALL ARE TEXT FORMS. KINDLY DO ALL STUFF THAT YOU NEED TO ONLY ON THIS LIST, AND DONT DESTROY MY CODE :P
    #PLEASE MAKE SURE THAT ALL CHANGES AND MANIPULATIONS YOU NEED TO DO ARE DONE UNDER A FUNCTION WHICH YOU CAN DEFINE AFTER POPUP(). JUST DEFINE THE FUNCTION. LEAVE THE CALLING AND WORKING OF THE FUNCTION TO ME
    def ENTERING_NAME():
        NAME= NAMEBOX.get()
        LIST_OF_VALUES.append(NAME)
    def ENTERING_PHONE_NUMBER():
        NUMBER=PHONE.get()
        LIST_OF_VALUES.append(NUMBER) 
    def ENTERING_EMAIL():
        E_mail=EMAIL.get()
        LIST_OF_VALUES.append(E_mail)
    def ENTERING_ISSUES():
        Issues= ISSUES.get()
        LIST_OF_VALUES.append(Issues)
    def popup():
        messagebox.showinfo("CONGRATULATIONS",'THANK YOU FOR REACHING OUT TO US. WE SYMPATHISE WITH YOUR PROBLEMS AND WILL TRY OUR BEST TO LINK YOU WITH OTHERS WHO FACE THE SAME ISSUES. KINDLY CHECK YOUR MAIL FOR FURTHER INFORMATION')
    DOMESTIC_WIN=tk.Toplevel()
    DOMESTIC_WIN.title("FINANCIAL AID")
    width= DOMESTIC_WIN.winfo_screenwidth()
    height= DOMESTIC_WIN.winfo_screenheight()
    bgimage1= tk.PhotoImage(file=os.getcwd()+"\FINANCIAL AID.png")
    tk.Label(DOMESTIC_WIN,image= bgimage1).place(relwidth=1, relheight=1)
    name=tk.StringVar(None)
    NAMEBOX= tk.Entry(DOMESTIC_WIN,textvariable=name,width=50)
    NAMEBOX.place(x=150,y=50)
    namebox=tk.Button(DOMESTIC_WIN,text="NAME",state='disabled',fg='blue',bg='white').place(x=25,y=50)
    phone=tk.StringVar(None)
    PHONE= tk.Entry(DOMESTIC_WIN,textvariable=phone,width=50)
    PHONE.place(x=150,y=150)
    #PHONE.insert(0,"PHONE: ")
    phonebox=tk.Button(DOMESTIC_WIN,text="PHONENUMBER",state='disabled',fg='blue',bg='white').place(x=25,y=150)
    Email=tk.StringVar(None)
    EMAIL= tk.Entry(DOMESTIC_WIN,textvariable=Email,width=50)
    EMAIL.place(x=150,y=250)
    emailbox=tk.Button(DOMESTIC_WIN,text="EMAIL",state='disabled',fg='blue',bg='white').place(x=25,y=250)
    issues=tk.StringVar(None)
    ISSUES= tk.Entry(DOMESTIC_WIN,textvariable=issues,width=50)
    ISSUES.place(x=150,y=350)
    issuesbox=tk.Button(DOMESTIC_WIN,text="ISSUES",state='disabled',fg='blue',bg='white').place(x=20,y=350)
    enterbutton= tk.Button(DOMESTIC_WIN,height=2,width=50,text='SUBMIT DETAILS',command=lambda:[ENTERING_NAME(),ENTERING_PHONE_NUMBER(),ENTERING_EMAIL(),ENTERING_ISSUES(),popup(),DOMESTIC_WIN.destroy()]).place(x=200,y=750)
    DOMESTIC_WIN.mainloop()
    global cursor
    s = 'insert into financial_aid(' + LIST_OF_VALUES[0] + ', ' + LIST_OF_VALUES[1] + ', ' + LIST_OF_VALUES[2] + ', ' + LIST_OF_VALUES[3])
    cursor.execute(s)
    sender = 'soluchanbyasy62636@gmail.com'
    receivers = ['samhruth@gmail.com', 'adk91215@gmail.com']
    subject = '(no-reply) Team Soluchan welcomes you'


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('soluchanbyasy62636@gmail.com', 'We<3Yashas')
        server.sendmail(sender, receivers, subject, Append(LIST_OF_VALUES))         
        print ("Successfully sent email")
    except smtplib.SMTPException:
        print('Unable to send mail')
    
def DEPRESSION_H_WIN():
    LIST_OF_VALUES=[]
    ### SAM, THIS IS THE LIST WHERE ALL THE INPUT FROM THE USER IS STORED. THE ELEMENTS ARE STORED IN THE ORDER NAME, PHONE NUMBER, EMAIL, ISSUES. ALL ARE TEXT FORMS. KINDLY DO ALL STUFF THAT YOU NEED TO ONLY ON THIS LIST, AND DONT DESTROY MY CODE :P
    #PLEASE MAKE SURE THAT ALL CHANGES AND MANIPULATIONS YOU NEED TO DO ARE DONE UNDER A FUNCTION WHICH YOU CAN DEFINE AFTER POPUP(). JUST DEFINE THE FUNCTION. LEAVE THE CALLING AND WORKING OF THE FUNCTION TO ME
    def ENTERING_NAME():
        NAME= NAMEBOX.get()
        LIST_OF_VALUES.append(NAME)
    def ENTERING_PHONE_NUMBER():
        NUMBER=PHONE.get()
        LIST_OF_VALUES.append(NUMBER) 
    def ENTERING_EMAIL():
        E_mail=EMAIL.get()
        LIST_OF_VALUES.append(E_mail)
    def ENTERING_ISSUES():
        Issues= ISSUES.get()
        LIST_OF_VALUES.append(Issues)
    def popup():
        messagebox.showinfo("CONGRATULATIONS",'THANK YOU FOR REACHING OUT TO US. WE SYMPATHISE WITH YOUR PROBLEMS AND WILL TRY OUR BEST TO LINK YOU WITH OTHERS WHO FACE THE SAME ISSUES. KINDLY CHECK YOUR MAIL FOR FURTHER INFORMATION')
    DOMESTIC_WIN=tk.Toplevel()
    DOMESTIC_WIN.title("DEPRESSION AID")
    width= DOMESTIC_WIN.winfo_screenwidth()
    height= DOMESTIC_WIN.winfo_screenheight()
    bgimage1= tk.PhotoImage(file=os.getcwd()+"\DEPRESSION.png")
    tk.Label(DOMESTIC_WIN,image= bgimage1).place(relwidth=1, relheight=1)
    name=tk.StringVar(None)
    NAMEBOX= tk.Entry(DOMESTIC_WIN,textvariable=name,width=50)
    NAMEBOX.place(x=150,y=50)
    namebox=tk.Button(DOMESTIC_WIN,text="NAME",state='disabled',fg='blue',bg='white').place(x=25,y=50)
    phone=tk.StringVar(None)
    PHONE= tk.Entry(DOMESTIC_WIN,textvariable=phone,width=50)
    PHONE.place(x=150,y=150)
    #PHONE.insert(0,"PHONE: ")
    phonebox=tk.Button(DOMESTIC_WIN,text="PHONENUMBER",state='disabled',fg='blue',bg='white').place(x=25,y=150)
    Email=tk.StringVar(None)
    EMAIL= tk.Entry(DOMESTIC_WIN,textvariable=Email,width=50)
    EMAIL.place(x=150,y=250)
    emailbox=tk.Button(DOMESTIC_WIN,text="EMAIL",state='disabled',fg='blue',bg='white').place(x=25,y=250)
    issues=tk.StringVar(None)
    ISSUES= tk.Entry(DOMESTIC_WIN,textvariable=issues,width=50)
    ISSUES.place(x=150,y=350)
    issuesbox=tk.Button(DOMESTIC_WIN,text="ISSUES",state='disabled',fg='blue',bg='white').place(x=20,y=350)
    enterbutton= tk.Button(DOMESTIC_WIN,height=2,width=50,text='SUBMIT DETAILS',command=lambda:[ENTERING_NAME(),ENTERING_PHONE_NUMBER(),ENTERING_EMAIL(),ENTERING_ISSUES(),popup(),DOMESTIC_WIN.destroy()]).place(x=200,y=750)
    DOMESTIC_WIN.mainloop()
    global cursor
    s = 'insert into depression(' + LIST_OF_VALUES[0] + ', ' + LIST_OF_VALUES[1] + ', ' + LIST_OF_VALUES[2] + ', ' + LIST_OF_VALUES[3])
    cursor.execute(s)
    
    
def OTHERS_H_WIN():
    LIST_OF_VALUES=[]
    ### SAM, THIS IS THE LIST WHERE ALL THE INPUT FROM THE USER IS STORED. THE ELEMENTS ARE STORED IN THE ORDER NAME, PHONE NUMBER, EMAIL, ISSUES. ALL ARE TEXT FORMS. KINDLY DO ALL STUFF THAT YOU NEED TO ONLY ON THIS LIST, AND DONT DESTROY MY CODE :P
    #PLEASE MAKE SURE THAT ALL CHANGES AND MANIPULATIONS YOU NEED TO DO ARE DONE UNDER A FUNCTION WHICH YOU CAN DEFINE AFTER POPUP(). JUST DEFINE THE FUNCTION. LEAVE THE CALLING AND WORKING OF THE FUNCTION TO ME
    
    def ENTERING_NAME():
        NAME= NAMEBOX.get()
        LIST_OF_VALUES.append(NAME)
    def ENTERING_PHONE_NUMBER():
        NUMBER=PHONE.get()
        LIST_OF_VALUES.append(NUMBER) 
    def ENTERING_EMAIL():
        E_mail=EMAIL.get()
        LIST_OF_VALUES.append(E_mail)
    def ENTERING_ISSUES():
        Issues= ISSUES.get()
        LIST_OF_VALUES.append(Issues)
    def popup():
        messagebox.showinfo("CONGRATULATIONS",'THANK YOU FOR REACHING OUT TO US. WE SYMPATHISE WITH YOUR PROBLEMS AND WILL TRY OUR BEST TO LINK YOU WITH OTHERS WHO FACE THE SAME ISSUES. KINDLY CHECK YOUR MAIL FOR FURTHER INFORMATION')
    DOMESTIC_WIN=tk.Toplevel()
    DOMESTIC_WIN.title("OTHERS")
    width= DOMESTIC_WIN.winfo_screenwidth()
    height= DOMESTIC_WIN.winfo_screenheight()
    bgimage1= tk.PhotoImage(file=os.getcwd()+"\OTHERS.png")
    tk.Label(DOMESTIC_WIN,image= bgimage1).place(relwidth=1, relheight=1)
    name=tk.StringVar(None)
    NAMEBOX= tk.Entry(DOMESTIC_WIN,textvariable=name,width=50)
    NAMEBOX.place(x=150,y=50)
    namebox=tk.Button(DOMESTIC_WIN,text="NAME",state='disabled',fg='blue',bg='white').place(x=25,y=50)
    phone=tk.StringVar(None)
    PHONE= tk.Entry(DOMESTIC_WIN,textvariable=phone,width=50)
    PHONE.place(x=150,y=150)
    #PHONE.insert(0,"PHONE: ")
    phonebox=tk.Button(DOMESTIC_WIN,text="PHONENUMBER",state='disabled',fg='blue',bg='white').place(x=25,y=150)
    Email=tk.StringVar(None)
    EMAIL= tk.Entry(DOMESTIC_WIN,textvariable=Email,width=50)
    EMAIL.place(x=150,y=250)
    emailbox=tk.Button(DOMESTIC_WIN,text="EMAIL",state='disabled',fg='blue',bg='white').place(x=25,y=250)
    issues=tk.StringVar(None)
    ISSUES= tk.Entry(DOMESTIC_WIN,textvariable=issues,width=50)
    ISSUES.place(x=150,y=350)
    issuesbox=tk.Button(DOMESTIC_WIN,text="ISSUES",state='disabled',fg='blue',bg='white').place(x=20,y=350)
    enterbutton= tk.Button(DOMESTIC_WIN,height=2,width=50,text='SUBMIT DETAILS',command=lambda:[ENTERING_NAME(),ENTERING_PHONE_NUMBER(),ENTERING_EMAIL(),ENTERING_ISSUES(),popup(),DOMESTIC_WIN.destroy()]).place(x=200,y=750)
    DOMESTIC_WIN.mainloop()
    global cursor
    s = 'insert into others(' + LIST_OF_VALUES[0] + ', ' + LIST_OF_VALUES[1] + ', ' + LIST_OF_VALUES[2] + ', ' + LIST_OF_VALUES[3])
    cursor.execute(s)
    sender = 'soluchanbyasy62636@gmail.com'
    receivers = ['samhruth@gmail.com', 'adk91215@gmail.com']
    subject = '(no-reply) Team Soluchan welcomes you'


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('soluchanbyasy62636@gmail.com', 'We<3Yashas')
        server.sendmail(sender, receivers, subject, Append(LIST_OF_VALUES))         
        print ("Successfully sent email")
    except smtplib.SMTPException:
        print('Unable to send mail')


def database_create():
    cursor.execute('create database soluchan')
    cursor.execute('use soluchan')
    cursor.execute('create table domestic_violence(name varchar(30),phone_num integer, email varchar(30), issues varchar(75))')
    cursor.execute('create table animal_abuse(name varchar(30),phone_num integer, email varchar(30), issues varchar(75))')
    cursor.execute('create table addiction(name varchar(30),phone_num integer, email varchar(30), issues varchar(75))')
    cursor.execute('create table financial_aid(name varchar(30),phone_num integer, email varchar(30), issues varchar(75))')
    cursor.execute('create table depression(name varchar(30),phone_num integer, email varchar(30), issues varchar(75))')
    cursor.execute('create table others(name varchar(30),phone_num integer, email varchar(30), issues varchar(75))')

database_create()

root = tk.Tk() #holds framework of the code
root.title("MAIN WORKING WINDOW FOR PROJECT")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#bgimage= tk.PhotoImage(file="C:\COMP PROJECT\MAIN BACKDROP.png")
bgimage= tk.PhotoImage(file=os.getcwd()+"\MAIN BACKDROP.png")
tk.Label(root,image= bgimage).place(relwidth=1, relheight=1)
DOMESTIC_VIOLENCE= tk.Button(root,text="DOMESTIC VIOLENCE",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[DOMESTIC_V_WIN()]).place(x=50,y=25)
ANIMAL_ABUSE= tk.Button(root,text="ANIMAL ABUSE",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[ANIMAL_A_WIN()]).place(x=50,y=450)
#ANIMAL_ABUSE= tk.Button(root,text="ANIMAL ABUSE",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[ANIMAL_ABUSE()]).place(x=50,y=450)
ADDICTION= tk.Button(root,text="ADDICTION",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[ADDICTION_H_WIN()]).place(x=50,y=700)
#ADDICTION= tk.Button(root,text="ADDICTION",fg='blue',bg='#7FFFD4',padx=20,pady=20).place(x=50,y=700)
FINANCIAL_AID= tk.Button(root,text="FINANCIAL AID",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[FINANCIAL_A_WIN()]).place(x=950,y=25)
#FINANCIAL_AID= tk.Button(root,text="FINANCIAL AID",fg='blue',bg='#7FFFD4',padx=20,pady=20).place(x=950,y=25)
DEPRESSION= tk.Button(root,text="DEPRESSION",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[DEPRESSION_H_WIN()]).place(x=950,y=450)
#DEPRESSION= tk.Button(root,text="DEPRESSION",fg='blue',bg='#7FFFD4',padx=20,pady=20).place(x=950,y=450)
OTHERS= tk.Button(root,text="OTHERS",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=lambda:[OTHERS_H_WIN()]).place(x=950,y=700)
#OTHERS= tk.Button(root,text="OTHERS",fg='blue',bg='#7FFFD4',padx=20,pady=20).place(x=950,y=700)
EXIT=tk.Button(root,text="EXIT",fg='blue',bg='#7FFFD4',padx=20,pady=20,command=root.destroy).place(x=1350,y=700)
root.mainloop()
