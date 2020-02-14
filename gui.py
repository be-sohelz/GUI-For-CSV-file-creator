import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI APP')

#create Lable on window
name_lable=ttk.Label(win,text='Enter Your Name : ')
name_lable.grid(row=0,column=0, sticky=tk.W)

email=ttk.Label(win,text='Enter Your Email : ')
email.grid(row=1,column=0,sticky=tk.W)

age_lable=ttk.Label(win,text='Enter Your Age : ')
age_lable.grid(row=2,column=0,sticky=tk.W)

user_lable=ttk.Label(win,text='Select your type : ')
user_lable.grid(row=4,column=0,sticky=tk.W)

gender_lable=ttk.Label(win,text='Select Your Gender : ')
gender_lable.grid(row=5,column=0)

#defining function
def info():
    name=name_var.get()
    email=email_var.get()
    age=age_var.get()
    user=user_type.get()
    gender=gender_var.get()
    if check_var.get()==0:
        subscribe='NO'
    else:
        subscribe='Yes'
    with open('file.csv','a',newline='') as f:
        dict_write=DictWriter(f,fieldnames=['name','email','age','user_type','gender','subscribe'])
        if os.stat('file.csv').st_size==0:
            dict_write.writeheader()
        dict_write.writerow({
            'name':name,
            'email':email,
            'age':age,
            'user_type':user,
            'gender':gender,
            'subscribe':subscribe,
        })
        name_entry.delete(0,tk.END)
        age_lable.delete(0,tk.END)
        email_entry.delete(0,tk.END)

#creating variables
name_var=tk.StringVar()
name_entry=ttk.Entry(win,width=16,textvariable=name_var)
name_entry.grid(row=0,column=1)
name_entry.focus()


email_var=tk.StringVar()
email_entry=ttk.Entry(win,width=16,textvariable=email_var)
email_entry.grid(row=1,column=1)

age_var=tk.StringVar()
age_lable=ttk.Entry(win,width=16,textvariable=age_var)
age_lable.grid(row=2,column=1)

# creating combobox
gender_var=tk.StringVar()
user_gender=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
user_gender['values']=('MALE','Female','OTHER')
user_gender.current(0)
user_gender.grid(row=5,column=1)

# creating radio button
user_type=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='student',value='student',variable=user_type)
radiobtn1.grid(row=4,column=1)
radiobtn2=ttk.Radiobutton(win,text='teacher',value='teacher',variable=user_type)
radiobtn2.grid(row=4,column=2)

# Submit button
submit_button=ttk.Button(win,text='Submit', command=info)
submit_button.grid(row=7,column=1)

# check button
check_var=tk.IntVar()
checkbtn1=ttk.Checkbutton(win,text='Select For Subscribe News Letter .',variable=check_var)
checkbtn1.grid(row=6,columnspan=3)

# name_entry.focus()
win.mainloop()