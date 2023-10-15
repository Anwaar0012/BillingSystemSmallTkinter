from tkinter import *
from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = CTk()
root.title("Billing System")
root.geometry(f"{1100}x{580}")
set_appearance_mode("dark")
set_default_color_theme("blue")
my_bg="#4D0039"


# ========== variables ========================
customer_name =StringVar()
customer_phone =StringVar()
bill_no = StringVar()
item=StringVar()
rate=IntVar()
quantity = IntVar()

# x= round(random.random()+100)
# x=round(x*10/2)
x = random.randint(1000,9999)
bill_no.set(str(x)+"HA")

global l
l=[]
# =================== functions ================
def welcome ():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t Welcome to Anwaar Retail Shop")
    textarea.insert(END,f"\n\n Bill No:\t{bill_no.get()}")
    textarea.insert(END,f"\n Customer Name:\t{customer_name.get()}")
    textarea.insert(END,f"\n Phone No:\t{customer_phone.get()}")
    textarea.insert(END,f"\n\n==========================================")
    textarea.insert(END,"\n Product\t\tQTY\t\tPrice ")
    textarea.insert(END,f"\n==========================================\n")
    textarea.configure(font=('arial',19,'bold'))

def addItem():
    gotRate = rate.get()
    # print(gotRate)
    price = quantity.get()*gotRate
    # print(price)
    l.append(price)
    if item.get()=='':
        messagebox.showerror(title="Error",message="Please enter product name")
    else:
        # textarea.insert(END,f' {item.get()}\t\t{quantity.get()}\t\t {price}\n')
        # usi mein enter karna ho to usi form kay end par ho 
        textarea.insert((10.0+float(len(l)-1)),f' {item.get()}\t\t{quantity.get()}\t\t {price}\n')

def getBill():
    if(customer_name.get()=='' or customer_phone == ''):
        messagebox.showerror('Error','Please enter customer details')
    else:
        textofLineTenToDown=textarea.get(10.0,+(10.0+(float(len(l)))))
        welcome()
        textarea.insert(END,textofLineTenToDown)
        textarea.insert(END,f"\n==========================================")
        textarea.insert(END,f"\n \t Total Payable Amount \t (Rs.{sum(l)})/-")
        textarea.insert(END,f"\n==========================================")
        saveBill()

def saveBill():
    askToSave =messagebox.askyesno('Save Bill','Do you want to save the bill')
    # print(askToSave)
    bill_details=textarea.get(1.0,END)
    if askToSave>0:
        file1=open('bills/'+str(bill_no.get())+'.txt','w')
        file1.write(bill_details)
        file1.close()
        messagebox.showinfo('saved',f'Bill No: {bill_no.get()} saved successfully')
    else:
        return
    
def clear():
    customer_name.set('')
    customer_phone.set('')
    item.set('')
    rate.set(0)
    quantity.set(0)
    welcome()

def exit():
    op=messagebox.askyesno("Exit","Do you really want to exit")
    if op>0:
        root.destroy()
    else:
        return


    



# ======== Top Section ==========
title_label = CTkLabel(root,text="Billing System",bg_color=my_bg,font=("time new roman",25,'bold'),height=50)
title_label.pack(fill=X)

# ======== Customers Details =========
customer_frame = CTkFrame(root,width=500, corner_radius=0)
customer_frame.place(x=10,y=70)

cust_detail_label=CTkLabel(customer_frame,text="Customer Details",font=("time new roman",18,'bold'),bg_color=my_bg)
cust_detail_label.grid(row=0,column=0)

cuntomer_name_entry= CTkEntry(customer_frame,placeholder_text=" Enter Customer Name ",width=200,font=("arial",15,'bold'),textvariable=customer_name)
cuntomer_name_entry.grid(row=2,column=0,padx=10,pady=5)

cuntomer_mobile_entry= CTkEntry(customer_frame,placeholder_text=" Enter Customer Mobile No. ",width=200,textvariable=customer_phone)
cuntomer_mobile_entry.grid(row=2,column=2, padx=5,pady=5)

seperator= CTkLabel(customer_frame,text=" ",width=200)
seperator.grid(row=3,column=0)

# ========= product details ==============
product_detail_frame = CTkFrame(root,width=400,height=300, corner_radius=0)
product_detail_frame.place(x=25,y=200)

prod_detail_label=CTkLabel(product_detail_frame,text="Product Details",font=("time new roman",18,'bold'),bg_color=my_bg)
prod_detail_label.grid(row=0,column=0,padx=10,pady=5)

prod_name_label=CTkLabel(product_detail_frame,text="Name of Product",font=("time new roman",18,'bold'),bg_color=my_bg)
prod_name_label.grid(row=3,column=0,padx=10,pady=5)


product_name_entry= CTkEntry(product_detail_frame,placeholder_text=" Enter your product Name ",width=200,font=("arial",15,'bold'),textvariable=item)
product_name_entry.grid(row=3,column=1,padx=10,pady=5)

prod_rate_label=CTkLabel(product_detail_frame,text="Rate in Rs.",font=("time new roman",18,'bold'),bg_color=my_bg)
prod_rate_label.grid(row=4,column=0,padx=10,pady=5)

product_rate_entry= CTkEntry(product_detail_frame,placeholder_text=" Enter the rate of product ",width=200,font=("arial",15,'bold'),textvariable=rate)
product_rate_entry.grid(row=4,column=1,padx=10,pady=5)

prod_Quantity_label=CTkLabel(product_detail_frame,text="Quantity",font=("time new roman",18,'bold'),bg_color=my_bg)
prod_Quantity_label.grid(row=5,column=0,padx=10,pady=5)

quantity_entry= CTkEntry(product_detail_frame,placeholder_text=" Enter required Quantity ",width=200,font=("arial",15,'bold'),textvariable=quantity)
quantity_entry.grid(row=5,column=1,padx=10,pady=5)

# =========== buttons ===================== 
add_item_button = CTkButton(product_detail_frame,text="Add item ",font=("time new roman",18,'bold'),command=addItem)
add_item_button.grid(row=6,column=0,padx=15, pady=30)

generate_bill_button = CTkButton(product_detail_frame,text="Generate Bill",font=("time new roman",18,'bold'),command=getBill)
generate_bill_button.grid(row=6,column=1, padx=5, pady=30)

clear_button = CTkButton(product_detail_frame,text="Clear", font=("time new roman",18,'bold'),command=clear)
clear_button.grid(row=7,column=0, padx=5, pady=20)

exit_button = CTkButton(product_detail_frame,text="Exit",font=("time new roman",18,'bold'),command=exit)
exit_button.grid(row=7,column=1, padx=5, pady=20)


# bill_detail_frame = CTkFrame(root,width=200,height=400, corner_radius=0)
# bill_detail_frame.place(x=500,y=80)

# bill_title = CTkLabel(bill_detail_frame,text="Bill Area",font=("time new roman",18,'bold'),bg_color=my_bg)
# bill_title.pack(fill=X)

# scrol_y=Scrollbar(bill_detail_frame,orient=VERTICAL)
# textArea=Text(bill_detail_frame,yscrollcommand=scrol_y)
# textArea.pack(side=RIGHT,fill=X)
# scrol_y.config(command=textArea.yview)

blil_frame = CTkScrollableFrame(root,label_text="Bill Details",width=500,height=350, orientation=VERTICAL,)

blil_frame.place(x=500,y=80)

textarea=CTkTextbox(blil_frame,width=455,height=340)
textarea.pack(fill=BOTH)
welcome()






root.mainloop()