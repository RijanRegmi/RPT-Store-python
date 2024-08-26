from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random,os
import customtkinter as ctk
import mysql.connector

class regmiplastic:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1020x644+400+200")
        self.root.title("Regmi Plastic Traders")
        self.root.resizable(0, 0)
        self.products_added = []

        # connection =mysql.connector.connect(host="localhost",username="root",password="root",database="rpt",port="3306")
        # c = connection.cursor

        # Left Frame
        left_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#34aad0")
        left_Frame.place(x=0, y=0, width=180, height=644)

        # #image
        # img1 = Image.open("C:/allcode/Regmi Plastic Traders/image/logo 2.png")
        # img1 = img1.resize((120, 80), Image.LANCZOS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # label_img1 = Label(left_Frame, bg="#34aad0", image=self.photoimg1)
        # label_img1.place(x=25, y=10, width=120, height=80)


        self.btndashboard = Button(left_Frame, text="DashBoard", command=self.dashboard, height=50, font=('arial', 15, 'bold'), bg="#67606B", fg="#abafbd", width=120, cursor="hand2")
        self.btndashboard.place(x=20, y=80, width=130, height=44)

        self.btnbilling = Button(left_Frame, text="Billing", command=self.billing, height=50, font=('arial', 15, 'bold'), bg="#67606B", fg="#abafbd", width=120, cursor="hand2")
        self.btnbilling.place(x=20, y=150, width=130, height=44)

        self.btnstock = Button(left_Frame, text="Stocks", height=50,command=self.stock, font=('arial', 15, 'bold'), bg="#67606B", fg="#abafbd", width=120, cursor="hand2")
        self.btnstock.place(x=20, y=220, width=130, height=44)
        self.dashboard()





# =============================================================================================DASHBOARD====================================================================================



    def dashboard(self):
        # Main Frame
        Dashboard_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Dashboard_Frame.place(x=180, y=0, width=840, height=644)

       
       

        Name_Frame = Frame(Dashboard_Frame, bd=0, relief=GROOVE, bg="White")
        Name_Frame.place(x=190, y=0, width=640, height=200)

        #img
        # logo_img = Image.open("C:/allcode/Regmi Plastic Traders/image/logo 2.png")
        # logo_img = logo_img.resize((120, 80), Image.LANCZOS)
        # self.logo_img = ImageTk.PhotoImage(logo_img)
        # label_logo_img = Label(Name_Frame, bg="white", image=self.logo_img)
        # label_logo_img.place(x=100, y=10, width=120, height=80)

        contact_text = Label(Name_Frame,text="9851012554\n9841940933",bg="white",fg="red", font=("Arail",12,"bold"))
        contact_text.place(x=500, y=20, width=100, height=40)

        Name_text = Label(Name_Frame,text="HARI REGMI",bg="white",fg="red", font=("Arail",22,"bold"))
        Name_text.place(x=240, y=20, width=200, height=40)

        business_text = Label(Name_Frame,text="Regmi Plastic Traders",bg="white",fg="#3682F0", font=("Arail",42,"bold"))
        business_text.place(x=5, y=100, width=640, height=70)

        Address_text = Label(Name_Frame,text="Kalimati, Kathmandu",bg="white",fg="red", font=("Arail",12,"bold"))
        Address_text.place(x=250, y=170, width=160, height=15)

        # #side image
        # top_left_img = Image.open("C:/allcode/Regmi Plastic Traders/image/Triángulos celestes.jpg")
        # top_left_img = top_left_img.resize((200, 635), Image.LANCZOS)
        # self.top_left_img = ImageTk.PhotoImage(top_left_img)
        # label_top_left_img = Label(Dashboard_Frame, bg="white", image=self.top_left_img)
        # label_top_left_img.place(x=0, y=0, width=200, height=635)

        # #image frame
        # img_frame=Frame(Dashboard_Frame, bd=5, bg="white")
        # img_frame.place(x=200, y=200, width=630, height=255)

        # #tirpal image
        # tirpal_img = Image.open("C:/allcode/Regmi Plastic Traders/image/Tirpal.jpg")
        # tirpal_img = tirpal_img.resize((100, 100), Image.LANCZOS)
        # self.tirpal_img = ImageTk.PhotoImage(tirpal_img)
        # label_tirpal_img = Label(img_frame, bg="white", image=self.tirpal_img)
        # label_tirpal_img.place(x=0, y=0, width=100, height=100)

        # #net image
        # net_img = Image.open("C:/allcode/Regmi Plastic Traders/image/green net.jpg")
        # net_img = net_img.resize((150, 100), Image.LANCZOS)
        # self.net_img = ImageTk.PhotoImage(net_img)
        # label_net_img = Label(img_frame, bg="white", image=self.net_img)
        # label_net_img.place(x=100, y=0, width=150, height=100)

        # #fabric image
        # fabric_img = Image.open("C:/allcode/Regmi Plastic Traders/image/fabric jhola.jpg")
        # fabric_img = fabric_img.resize((100, 100), Image.LANCZOS)
        # self.fabric_img = ImageTk.PhotoImage(fabric_img)
        # label_fabric_img = Label(img_frame, bg="white", image=self.fabric_img)
        # label_fabric_img.place(x=280, y=0, width=100, height=100)


        # #dori image
        # nylon_dori_img = Image.open("C:/allcode/Regmi Plastic Traders/image/nylon dori.jpg")
        # nylon_dori_img = nylon_dori_img.resize((100, 100), Image.LANCZOS)
        # self.nylon_dori_img = ImageTk.PhotoImage(nylon_dori_img)
        # label_nylon_dori_img = Label(img_frame, bg="white", image=self.nylon_dori_img)
        # label_nylon_dori_img.place(x=400, y=0, width=100, height=100)

        # #tape image
        # tape_img = Image.open("C:/allcode/Regmi Plastic Traders/image/tape.png")
        # tape_img = tape_img.resize((100, 100), Image.LANCZOS)
        # self.tape_img = ImageTk.PhotoImage(tape_img)
        # label_tape_img = Label(img_frame, bg="white", image=self.tape_img)
        # label_tape_img.place(x=520, y=0, width=100, height=100)

        # #Bike Cover image
        # bike_cover_img = Image.open("C:/allcode/Regmi Plastic Traders/image/bike cover.png")
        # bike_cover_img = bike_cover_img.resize((100, 100), Image.LANCZOS)
        # self.bike_cover_img = ImageTk.PhotoImage(bike_cover_img)
        # label_bike_cover_img = Label(img_frame, bg="white", image=self.bike_cover_img)
        # label_bike_cover_img.place(x=0, y=120, width=100, height=100)

        # #plastic dori image
        # plastic_dori_img = Image.open("C:/allcode/Regmi Plastic Traders/image/plastic dori.png")
        # plastic_dori_img = plastic_dori_img.resize((100, 100), Image.LANCZOS)
        # self.plastic_dori_img = ImageTk.PhotoImage(plastic_dori_img)
        # label_plastic_dori_img = Label(img_frame, bg="white", image=self.plastic_dori_img)
        # label_plastic_dori_img.place(x=180, y=120, width=100, height=100)

        # #jhola image
        # jhola_img = Image.open("C:/allcode/Regmi Plastic Traders/image/jhola.jpg")
        # jhola_img = jhola_img.resize((100, 100), Image.LANCZOS)
        # self.jhola_img = ImageTk.PhotoImage(jhola_img)
        # label_jhola_img = Label(img_frame, bg="white", image=self.jhola_img)
        # label_jhola_img.place(x=350, y=120, width=100, height=100)


        # #bora image
        # bora_img = Image.open("C:/allcode/Regmi Plastic Traders/image/bora.jpg")
        # bora_img = bora_img.resize((100, 100), Image.LANCZOS)
        # self.bora_img = ImageTk.PhotoImage(bora_img)
        # label_bora_img = Label(img_frame, bg="white", image=self.bora_img)
        # label_bora_img.place(x=500, y=120, width=100, height=100)


        # #item frame
        # Item_Frame = Frame(Dashboard_Frame, bd=0, relief=GROOVE,bg="#2C9CF5")  
        # Item_Frame.place(x=200, y=455, width=630, height=180)

        # Item_text = Label(Item_Frame,text="Tirpal, Tunnel Plastic, Plastic Bag, I.D. Sheets, PP Plastic \n Plastic Sutari, Nylon Dori, Plastic Bora, M.C. Cover, \n Carton Tape & all Kinds of Plastic Goods",bg="white",fg="#3682F0", font=("Arail",15,"bold"))
        # Item_text.place(x=0, y=0, width=630, height=180)


# ===================================================================BILLING=========================================================================


    def billing(self):
        # ======================Variables======================
        self.Date = StringVar()
        self.Name = StringVar()
        self.Product = StringVar()
        self.Qty = IntVar()
        self.Rate = IntVar()
        self.Amount = IntVar()
        self.TotalAmount = DoubleVar()
        self.search_bill = StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)

        # billing frame
        Billing_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Billing_Frame.place(x=180, y=0, width=840, height=644)

        self.lblDate = Label(Billing_Frame, text="Date", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblDate.place(x=10, y=100)

        self.txtDate = ttk.Entry(Billing_Frame, textvariable=self.Date, font=("arial", 12, "bold"), width=24)
        self.txtDate.place(x=150, y=100)

        # Name
        self.lblName = Label(Billing_Frame, text="Name", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblName.place(x=10, y=150)

        self.txtName = ttk.Entry(Billing_Frame, textvariable=self.Name, font=("arial", 12, "bold"), width=24)
        self.txtName.place(x=150, y=150)
       
       

        # Product
        self.lblProduct = Label(Billing_Frame, text="Product", font=("arial", 12, "bold"), bg="white", fg="black",
                                bd=4)
        self.lblProduct.place(x=10, y=200)

        self.txtProduct = ttk.Entry(Billing_Frame, textvariable=self.Product, font=("arial", 12, "bold"), width=24)
        self.txtProduct.place(x=150, y=200)

        # Qty
        self.lblQty = Label(Billing_Frame, text="Qty", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblQty.place(x=10, y=250)

        self.txtQty = ttk.Entry(Billing_Frame, textvariable=self.Qty, font=("arial", 12, "bold"), width=24)
        self.txtQty.place(x=150, y=250)

        # Rate
        self.lblRate = Label(Billing_Frame, text="Rate", font=("arial", 12, "bold"), bg="white", fg="black", bd=4)
        self.lblRate.place(x=10, y=300)

        self.txtRate = ttk.Entry(Billing_Frame, textvariable=self.Rate, font=("arial", 12, "bold"), width=24)
        self.txtRate.place(x=150, y=300)

        # Amount
        self.lblAmount = Label(Billing_Frame, text="Amount", font=("arial", 12, "bold"), bg="white", fg="black",
                               bd=4)
        self.lblAmount.place(x=10, y=350)

        self.txtAmount = ttk.Entry(Billing_Frame, textvariable=self.Amount, font=("arial", 12, "bold"), width=24)
        self.txtAmount.place(x=150, y=350)

        # button
        # add
        self.btnadd = Button(Billing_Frame, text="Add", height=1, font=('arial', 15, 'bold'), bg="#4f5c8b",
                             fg="#abafbd", width=10, cursor="hand2", command=self.add)
        self.btnadd.place(x=50, y=550)

        # clear
        self.btngen_bill = Button(Billing_Frame, text="Generate Bill", command=self.gen_bill, height=1,
                                  font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#abafbd", width=10, cursor="hand2")
        self.btngen_bill.place(x=200, y=550)

        # save
        self.btnsave = Button(Billing_Frame, text="Save", height=1, font=('arial', 15, 'bold'), bg="#4f5c8b",
                              fg="#abafbd", width=10, cursor="hand2", command=self.save)
        self.btnsave.place(x=350, y=550)

        # clear
        self.btnclear = Button(Billing_Frame, text="Clear", command=self.clear, height=1, font=('arial', 15, 'bold'),
                               bg="#4f5c8b", fg="#abafbd", width=10, cursor="hand2")
        self.btnclear.place(x=500, y=550)

        # search frame
        Search_Frame = Frame(Billing_Frame, bd=2, bg="white")
        Search_Frame.place(x=400, y=40, width=350, height=40)

        self.lblBill = Label(Search_Frame, text="Date", font=("arial", 13, "bold"), width=7, bg="#4f5c8b",
                             fg="white")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame, textvariable=self.search_bill, font=('arial', 13, 'bold'), width=18)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.btnSearch = Button(Search_Frame,command=self.find_bill, text="Search", font=('arial', 9, 'bold'), bg="#4f5c8b", fg="white",
                                width=10, cursor="hand2")
        self.btnSearch.grid(row=0, column=2)

        # bill frame
        BillLabelFrame = LabelFrame(Billing_Frame, text="Info Aria", font=("times new romen", 12, "bold"), bg="white",
                                    fg="#b90508")
        BillLabelFrame.place(x=400, y=80, width=420, height=440)

        scroll_y = Scrollbar(BillLabelFrame, orient=VERTICAL)
        self.textarea = Text(BillLabelFrame, yscrollcommand=scroll_y.set, font=("times new romen", 12, "bold"),
                             bg="white", fg="#b90508")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # total amount
        self.lblTotal = Label(Billing_Frame, text="Total Amount", font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txtTotal = ttk.Entry(Billing_Frame, textvariable=self.TotalAmount, font=("arial", 10, "bold"), width=24)
        self.txtTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)



    def InsertDAta(self):
        Date = self.txtDate.get()
        Name = self.txtName.get()
        Product = self.txtProduct.get()
        Qty = self.txtQty.get()
        Rate = self.txtRate.get()
        Amount = self.txtAmount.get()
        Total_amount = self.txtTotal.get()



        # insert_query="INSERT INTO 'rpt_billing'('Date','Name','Product','Qty','Rate','Amount','Total_amount') VALUES (%s,%s,%s,%s,%s,%s,%s)"
        # vals=(Date,Name,Product,Qty,Rate,Amount,Total_amount)
        # c.exicute(insert_query,vals)
        # connection.commit()


        self.Bill()

        self.l = []
        self.k = []

    # functions
    def add(self):
        self.n = self.Rate.get()
        self.o = self.Qty.get()
        self.m = self.o * self.n
        self.l.append(self.m)

        self.a = self.n * self.o
        self.k.append(self.a)

        product = {
                "name": self.Product.get(),
                "qty": self.Qty.get(),
                "rate": self.Rate.get(),
                "amount": self.a
            }
        self.products_added.append(product)
       
        if self.Name.get() == "" or self.Product.get() == "" or self.Qty.get() == "" or self.Rate.get() == "" or self.Amount.get() == "":
            messagebox.showerror("Error", "Enter All detail")
        elif self.Date.get() == "":
            messagebox.showerror("Error", "Enter Date")
        else:
            self.textarea.insert(END, f"\n {self.Product.get()}\t\t{self.Qty.get()}\t{self.Rate.get()}\t{self.a}")
            self.TotalAmount.set(round(sum(self.l),2))


    def gen_bill(self):
       
        if not self.textarea.get(1.0, END).isspace():
            self.Bill()
            for product in self.products_added:
                self.textarea.insert(END, f"{product['name']}\t\t{product['qty']}\t{product['rate']}\t{product['amount']}\n")
           
            self.textarea.insert(END, f"\n===========================================")
            self.textarea.insert(END, f"\nTotal\t\t{self.TotalAmount.get():.2f}\n")
            self.textarea.insert(END, f"===========================================\n")

    def save(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            f1 =open(f'Bill/'f'{str(self.Name.get())},{str(self.bill_no.get())}''.txt','w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved", f"Date:{self.bill_no.get()} saved successfully")
            f1.close()

    def find_bill(self):
        found="no"
        for i in os.listdir("Bill/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bill/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Date")

    def clear(self):
        self.textarea.delete(1.0, END)
        self.Date.set("")
        self.Name.set("")
        self.Product.set("")
        self.Qty.set(0)
        self.Rate.set(0)
        self.Amount.set(0)
        self.search_bill.set("")
        self.TotalAmount.set(0.0)
        self.Bill()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

    def Bill(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\t Welcome to Regmi Plastic Traders\n")
        self.textarea.insert(END,f"\n\t\t\t\t Bill No.:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Date:{self.Date.get()}")
        self.textarea.insert(END, f"\n Name:{self.Name.get()}")
        self.textarea.insert(END, "\n===========================================")
        self.textarea.insert(END, f"\nProduct\t\tQty\tRate\tAmount")
        self.textarea.insert(END, "\n===========================================\n")




   






# ======================================================================STOCK=================================================================================
       


    def stock(self):
        Stock_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Stock_Frame.place(x=180, y=0, width=840, height=644)

        self.btnclear = Button(Stock_Frame, text="Godowm 1", height=1, font=('arial', 15, 'bold'),
                               bg="lightblue", fg="white", width=10, cursor="hand2")
        self.btnclear.place(x=20, y=50)

   

       
       





if __name__ == "__main__":
    root = Tk()
    obj = regmiplastic(root)
    root.mainloop()