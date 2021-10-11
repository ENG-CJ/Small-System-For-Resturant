from tkinter import *
from  tkinter import ttk
from  tkinter import messagebox as  msg
import  pyodbc
from  PIL import ImageTk,Image


class AL_QUDUS_APP:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.config(bg='#fff')
        self.root.resizable(0,0)
        self.root.iconbitmap('logo.ico')
        self.root.title('HEALTH FOOD, HEALTH LIFE | AXLAAM SWEETS')


        self.frame = Frame(self.root, bg='#019', bd=4, relief='groove', width=390, height=780)
        self.frame.place(x=0, y=93)

        # Label(self.frame,text='Mange Products').place(x=1)

        self.img=Image.open('stock.jpg')
        self.res=self.img.resize((382,300),Image.ANTIALIAS)
        self.new=ImageTk.PhotoImage(self.res)
        Label(self.frame,image=self.new,bg='#019').place(x=1,y=1)

        Label(self.root,text='HEALTH FOOD, HEALTH LIFE | AXLAAM SWEETS| MANAGE THE DATABASE',bg='#019',
              fg='white',font=('Verdana',18,'bold'),height=3).pack(fill=X)

        self.img1 = Image.open('CHICK.jpg')
        self.img2=ImageTk.PhotoImage(self.img1)
        Label(self.root,bg='white',image=self.img2).place(x=590,y=200)

        self.total_products=Label(self.root,bg='#017',fg='white',font=('Verdana',19,'bold')
              ,bd=10,relief='sunken',text='Total Products\n[0]')
        self.total_products.place(x=590,y=700)

        self.total_customers=Label(self.root, bg='#017', fg='white', font=('Verdana', 19, 'bold')
              , bd=10, relief='sunken', text='Total Customers\n[0]')
        self.total_customers.place(x=900, y=700)

        self.total_stuff=Label(self.root, bg='#017', fg='white', font=('Verdana', 19, 'bold')
              , bd=10, relief='sunken', text='Total Stuffs\n[0]')
        self.total_stuff.place(x=1260, y=700)


        #btns
        self.product_btn = Button(self.frame, text='Products', cursor='hand2',bg='#019', fg='white',
                          font=('Verdana', 18, 'bold'),command=self.products, width=15, justify=CENTER)
        self.product_btn.place(x=50, y=340)

        self.c_btn = Button(self.frame, text='Customers', bg='#019', fg='white',
                          font=('Verdana', 18, 'bold'),cursor='hand2', width=15, justify=CENTER,command=self.Customers)
        self.c_btn.place(x=50, y=430)

        self.st_btn = Button(self.frame, text='Stuff', bg='#019', fg='white',
                          font=('Verdana', 18, 'bold'), cursor='hand2',width=15, justify=CENTER)
        self.st_btn.place(x=50, y=530)
        print(pyodbc.drivers())
        self.show()



    def show(self):
        conn=pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
        "Database=Albaraka_Shop;"
        "Trusted_Connection=yes;"
        )
        cursor=conn.cursor()
        cursor.execute("SELECT *FROM pro")
        row=cursor.fetchall()
        self.total_products.config(text=f'Total Products\n[{len(row)}]')

        cursor = conn.cursor()
        cursor.execute("SELECT *FROM customers")
        row = cursor.fetchall()
        self.total_customers.config(text=f'Total Customers\n[{len(row)}]')

        cursor = conn.cursor()
        cursor.execute("SELECT *FROM Stuffs")
        row = cursor.fetchall()
        self.total_stuff.config(text=f'Total Stuffs\n[{len(row)}]')

# product window
    def products(self):
        self.product=Toplevel()
        self.product.geometry('1100x740+30+20')
        self.product.focus_force()
        self.product.title('Products')
        self.product.resizable(0,0)
        self.product.config(bg='#fff')
        self.product.iconbitmap('logo.ico')

        # image
        self.icon_bg = Image.open('icon.png')
        self.resizing = self.icon_bg.resize((500, 500), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        lb = Label(self.product, image=self.new_icon, bd=0)
        lb.place(x=690, y=20)

        # prodyct
        Label(self.product,text='Manage The Products',bg='#015',fg='white',bd=3,relief='flat',
              font=('Verdana',18,'bold'),height=2).pack(fill=X)

        Label(self.product,text='ProductID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=120,y=100)
        self.pr_id=Entry(self.product,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=15)
        self.pr_id.place(x=120,y=150)

        # product name
        Label(self.product,text='Product Name',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=120,y=200)
        self.pr_name=Entry(self.product,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=15)
        self.pr_name.place(x=120,y=250)

        # price
        Label(self.product,text='Price',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=120,y=300)
        self.price=Entry(self.product,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=15)
        self.price.place(x=120,y=350)

        # quantity
        Label(self.product, text='Quantity', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=520, y=100)
        self.QTTY = Entry(self.product, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.QTTY.place(x=520, y=150)

        #Date
        Label(self.product, text='Date', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=520, y=200)
        self.Date = Entry(self.product, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.Date.place(x=520, y=250)

        # Buttons
        self.add_btn=Button(self.product,text='Add',bg='#019',fg='white',
                            bd=7,relief='ridge',font=('Verdana',18,'bold'),command=self.add)
        self.add_btn.place(x=190,y=420)

        self.update_btn = Button(self.product, text='Update', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 ,command=self.update)
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.product, text='Delete', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self.Delete)

        self.dele.place(x=445, y=420)

        # self.search = Button(self.product, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search = Entry(self.product, bg='#f4f4f4', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=20)
        self.search.place(x=800, y=15)

        self.search_img=Image.open('search-icon.png')
        self.resize_=self.search_img.resize((20,20))
        self.search_icon=ImageTk.PhotoImage(self.resize_)
        self.search_bth=Button(self.product,image=self.search_icon,bd=0,bg='#f4f4f4',activebackground='#f4f4f4',cursor='hand2',
                               command=self.Search)
        self.search.bind('<Return>',self.click)

        self.search.insert(0,'Search Product ID')
        self.search.config(state=DISABLED)
        self.search.bind('<Button-1>', self.active)
        self.search_bth.place(x=1055,y=22)



        # tree-view table


        self.frame_tree=Frame(self.product,bg='red',width=1090,bd=8,relief='sunken')
        self.frame_tree.place(x=5,y=500)
        scrollbar=Scrollbar(self.frame_tree,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tree=ttk.Treeview(self.frame_tree,yscrollcommand=scrollbar.set,columns=('ProductID','Product_Name','Price','QTTY','Date'))
        self.tree.pack(fill=BOTH,expand=True)
        self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree.yview)
        self.tree.column('ProductID',width=60)
        self.tree.heading('ProductID',text='ProductID')
        self.tree.heading('Product_Name',text='Product_Name')
        self.tree.heading('Price',text='Price')
        self.tree.heading('QTTY',text='QTTY')
        self.tree.heading('Date',text='Date')
        self.fetch()

        # configuring labels

    #______________________Start Functions____________________________________
     # selecting
    def fetch(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=Albaraka_Shop;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT *FROM pro ")
        rows=cursor.fetchall()
        for row in rows:
            self.tree.insert('',END,values=(row[0],row[1],row[2],row[3],row[4]))


    #add
    def add(self):
        try:
            if self.pr_id.get()=='' and self.pr_name.get()=='' and self.price.get()=='' and self.QTTY.get()=='' and self.Date.get()=='':
                msg.showerror('Error','All Fields Are required',parent=self.product)
            else:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute('INSERT INTO pro Values(?,?,?,?,?)',
                               (self.pr_id.get(),self.pr_name.get(),self.price.get(),self.QTTY.get(),self.Date.get()))
                conn.commit()
                msg.showinfo('AL-QUDUS', f'The Item {self.pr_name.get()} Added Successfully', parent=self.product)
                self.tree.delete(*self.tree.get_children())
                self.pr_id.delete(0, END)
                self.pr_name.delete(0, END)
                self.price.delete(0, END)
                self.QTTY.delete(0, END)
                self.Date.delete(0, END)
                self.fetch()
                self.show()
                self.pr_id.delete(0, END)
                self.pr_name.delete(0, END)
                self.price.delete(0, END)
                self.QTTY.delete(0, END)
                self.Date.delete(0, END)
        except Exception as err:
            msg.showerror("ERR",f"{err}",parent=self.product)

     #selction
    def select(self,event):
        self.pr_id.delete(0,END)
        self.pr_name.delete(0,END)
        self.price.delete(0,END)
        self.QTTY.delete(0,END)
        self.Date.delete(0,END)
        item=self.tree.focus()
        selection=self.tree.item(item,'values')
        self.pr_id.insert(0,selection[0])
        self.pr_name.insert(0,selection[1])
        self.price.insert(0,selection[2])
        self.QTTY.insert(0,selection[3])
        self.Date.insert(0,selection[4])


    # updating
    def update(self):
        try:
            if self.pr_id.get()=='' and self.pr_name.get()=='' and self.price.get()=='' and self.QTTY.get()=='' and self.Date.get()=='':
                msg.showerror('Error','Plz Select The Item You Want To Update',parent=self.product)
            else:
                item = self.tree.focus()
                selection = self.tree.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f"UPDATE pro SET ProID=?,ProName=?,Price=?,Quantity=?,Date_=? WHERE ProID={selection[0]}",
                               (self.pr_id.get(),self.pr_name.get(),self.price.get(),self.QTTY.get(),self.Date.get()))
                conn.commit()
                msg.showinfo('UPDATED','UPDATED SUCCESSFULLY',parent=self.product)
                self.pr_id.delete(0, END)
                self.pr_name.delete(0, END)
                self.price.delete(0, END)
                self.QTTY.delete(0, END)
                self.Date.delete(0, END)
                self.tree.delete(*self.tree.get_children())
                self.fetch()
        except Exception as err:
            msg.showerror('ERR',f"The ID [{self.pr_id.get()}] Already Exist Plz Choose Another One",parent=self.product)

    # delete
    def Delete(self):
        try:
            if self.pr_id.get()=='' and self.pr_name.get()=='' and self.price.get()=='' and self.QTTY.get()=='' and self.Date.get()=='':
                msg.showerror('Error','Plz Select The Item You Want To Delete',parent=self.product)
            else:
                item=self.tree.focus()
                selection=self.tree.item(item,'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans=msg.askyesno('Confirm',f'Are You Sure To Delete [{selection[1]}] ?',parent=self.product)
                if ans==1:
                    cursor.execute(f"DELETE Pro WHERE ProID={selection[0]}")
                    conn.commit()
                    msg.showinfo('AL-QUDUS','Successfully Deleted',parent=self.product)
                    self.tree.delete(*self.tree.get_children())
                    self.fetch()
                    self.show()
                else:
                    pass

        except Exception as err:
            msg.showerror('Err',f'Error Occurred Due To {err}')



    def active(self,event):
        self.search.config(state=NORMAL)
        self.search.delete(0,END)

    def Search(self):
        if self.search.get()=='':
            msg.showerror('ERR','ID IS REQUIRED',parent=self.product)
        else:
            try:

                # saerch
                search=self.search.get()
                conn = pyodbc.connect(
                            "Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                            "Database=Albaraka_Shop;"
                            "Trusted_Connection=yes;"
                        )
                cursor = conn.cursor()
                cursor.execute(f"SELECT *from pro where ProID={search}")
                select=cursor.fetchone()
                if select!=None:
                    for x in self.tree.get_children():
                        self.tree.delete(x)
                    self.tree.insert('',END,values=(select[0],select[1],select[2],select[3],select[4]))
                else:
                    msg.showerror('Error','No Record Found',parent=self.product)

                conn.close()
            except Exception as err:
                print(err)

    def click(self,e):
        if self.search.get() == '':
            msg.showerror('ERR', 'ID IS REQUIRED', parent=self.product)
        else:
            try:

                # saerch
                search = self.search.get()
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f"SELECT *from pro where ProID={search}")
                select = cursor.fetchone()
                if select != None:
                    for x in self.tree.get_children():
                        self.tree.delete(x)
                    self.tree.insert('', END, values=(select[0],select[1],select[2],select[3],select[4]))
                else:
                    msg.showerror('Error', 'No Record Found', parent=self.product)
                    self.search.delete(0,END)

                conn.close()
            except Exception as err:
                print(err)



    #============== Customers Window ===========================
    def Customers(self):
        self.customer = Toplevel()
        # self.customer.geometry('1200x840')
        self.customer.state('zoomed')

        self.customer.focus_force()
        self.customer.title('Customers')
        self.customer.resizable(0,0)
        self.customer.config(bg='#fff')
        self.customer.iconbitmap('logo.ico')
        style=ttk.Style()
        style.configure('TNotebook.Tab',font=('Yanone Kaffeesatz','18'),fg='red')
        notebook=ttk.Notebook(self.customer)
        self.tab_customer=Frame(notebook,width=1580,height=800,bg='white')
        self.customer_images=Frame(notebook,width=1200,height=800,bg='white')
        notebook.add(self.tab_customer,text='Customer')
        notebook.add(self.customer_images,text='Customer Photos')
        notebook.place(x=1,y=70)

        self.c_icon = Image.open('process.png')
        self.c_resize = self.c_icon.resize((550, 500), Image.ANTIALIAS)
        self.new_c = ImageTk.PhotoImage(self.c_resize)
        label_customer_icon = Label(self.tab_customer, image=self.new_c, bd=0)
        label_customer_icon.place(x=820, y=0)

        Label(self.customer, text='Manage The Customers', bg='#021', fg='white', bd=3, relief='flat',
              font=('Verdana', 18, 'bold'), height=2).pack(fill=X)
        #
        # # labels and boxes
        Label(self.tab_customer, text='CustomerID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=70, y=50)

        self.c_id = Entry(self.tab_customer, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.c_id.place(x=70, y=100)

        # product name
        Label(self.tab_customer, text='Customer Name', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=70, y=150)

        self.c_name = Entry(self.tab_customer, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=15)
        self.c_name.place(x=70, y=200)

        # price
        Label(self.tab_customer, text='Mobile', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=70, y=250)
        self.c_phone = Entry(self.tab_customer, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.c_phone.place(x=70, y=300)

        # quantity
        Label(self.tab_customer, text='Address', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=470, y=50)
        self.Address = Entry(self.tab_customer, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=15)
        self.Address.place(x=470, y=100)

        # Date
        Label(self.tab_customer, text='Date', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=470, y=150)
        self.date = Entry(self.tab_customer, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=15)
        self.date.place(x=470, y=200)


        # btns

        self._add_ = Button(self.tab_customer, text='Add', bg='#0202EF', fg='white',cursor='plus',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self.add_customer)
        self._add_.place(x=190, y=380)

        self._update_ = Button(self.tab_customer, text='Update', bg='#3F943B', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self.update_customer
                                 )
        self._update_.place(x=290, y=380)

        self._delete_ = Button(self.tab_customer, text='Delete', bg='#F50057', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self.deletion)

        self._delete_.place(x=445, y=380)

        # frame table
        self.tree_frame = Frame(self.tab_customer,bg='white', bd=0, )
        self.tree_frame.place(x=0, y=505)
        self.scrollbar = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_table = ttk.Treeview(self.tree_frame, yscrollcommand=self.scrollbar.set,
                                 columns=('CustomerID', 'CustomerName', 'Mobile', 'Address', 'Date'))
        self.tree_table.pack(fill=BOTH, expand=True)
        self.scrollbar.config(command=self.tree_table.yview)
        self.tree_table.column('CustomerID', width=90)
        self.tree_table.heading('CustomerID', text='CustomerID')
        self.tree_table.heading('CustomerName', text='CustomerName')
        self.tree_table.heading('Mobile', text='Mobile')
        self.tree_table.heading('Address', text='Address')
        self.tree_table.heading('Date', text='Date')
        self.tree_table.bind('<ButtonRelease-1>',self.select2)
        self.fetching()


        self.tiny_frame=Frame(self.tab_customer,width=420,height=220,bg='#f4f4f4',bd=5,relief='ridge')
        self.tiny_frame.place(x=1110,y=505)

        self.search1 = Entry(self.customer, bg='#f4f4f4', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=20)
        self.search1.place(x=1200, y=15)

        self.search_img1 = Image.open('search-icon.png')
        self.resize_1 = self.search_img1.resize((20, 20))
        self.search_icon1 = ImageTk.PhotoImage(self.resize_1)
        self.search_bth1 = Button(self.customer, image=self.search_icon1, bd=0, bg='#f4f4f4', activebackground='#f4f4f4',
                                 cursor='hand2',command=self.Searching
                                )
        self.search1.bind('<Return>', self.click1)

        self.search1.insert(0, "Search Customer's ID")
        self.search1.config(state=DISABLED)
        self.search1.bind('<Button-1>', self.active2)
        self.search_bth1.place(x=1465, y=22)


        # btns

    def fetching(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=Albaraka_Shop;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT *FROM customers ")
        rows = cursor.fetchall()
        for row in rows:
            self.tree_table.insert('', END, values=(row[0], row[1], row[2], row[3], row[4]))

    def add_customer(self):
        try:
            if self.c_id.get() == '' and self.c_name.get() == '' and self.c_phone.get() == '' and self.Address.get() == '' and self.date.get() == '':
                msg.showerror('Error', 'All Fields Are required', parent=self.customer)
            else:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute('INSERT INTO customers Values(?,?,?,?,?)',
                               (self.c_id.get(), self.c_name.get(), self.c_phone.get(), self.Address.get(),
                                self.date.get()))
                conn.commit()
                msg.showinfo('Axlaam',f'The Customer {self.c_name.get()} Added Successfully',parent=self.customer)
                self.tree_table.delete(*self.tree_table.get_children())
                self.fetching()
                self.show()
                self.c_id.delete(0, END)
                self.c_name.delete(0, END)
                self.c_phone.delete(0, END)
                self.Address.delete(0, END)
                self.date.delete(0, END)
        except Exception as err:
            msg.showerror("ERR",f"This ID -> {self.c_id.get()} All Ready Exist\nPlz Choose Another One", parent=self.customer)

        except:
            msg.showerror("ERR", f"This Number [{self.c_phone.get()}] is already Exist",
                          parent=self.customer)

    # slect
    def select2(self,event):
        self.c_id.delete(0,END)
        self.c_name.delete(0,END)
        self.c_phone.delete(0,END)
        self.Address.delete(0,END)
        self.date.delete(0,END)
        item2=self.tree_table.focus()
        selection_=self.tree_table.item(item2,'values')
        self.c_id.insert(0,selection_[0])
        self.c_name.insert(0,selection_[1])
        self.c_phone.insert(0,selection_[2])
        self.Address.insert(0,selection_[3])
        self.date.insert(0,selection_[4])


    #$ update
    def update_customer(self):
        try:
            if self.c_id.get()=='' and self.c_name.get()=='' and self.c_phone.get()=='' and self.Address.get()=='' and self.date.get()=='':
                msg.showerror('Error','Plz Select The Item You Want To Update',parent=self.customer)
            else:
                item3= self.tree_table.focus()
                selection3 = self.tree_table.item(item3, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f"UPDATE customers SET cid=?,cname=?,cphone=?,caddress=?,Date_=? WHERE cid={selection3[0]}",
                               (self.c_id.get(),self.c_name.get(),self.c_phone.get(),self.Address.get(),self.date.get()))
                conn.commit()
                msg.showinfo('UPDATED','UPDATED SUCCESSFULLY',parent=self.customer)
                self.tree_table.delete(*self.tree_table.get_children())
                self.fetching()
                self.c_id.delete(0, END)
                self.c_name.delete(0, END)
                self.c_phone.delete(0, END)
                self.Address.delete(0, END)
                self.date.delete(0, END)
        except Exception as err:

            msg.showerror('ERR',f"The ID [{self.c_id.get()}] Already Exist Plz Choose Another One",parent=self.customer)



    # delete
    def deletion(self):
        try:
            if self.c_id.get()=='' and self.c_name.get()=='' and self.c_phone.get()=='' and self.Address.get()=='' and self.date.get()=='':
                msg.showerror('Error','Plz Select The Item You Want To Delete',parent=self.customer)
            else:
                item4=self.tree_table.focus()
                selection4=self.tree_table.item(item4,'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans=msg.askyesno('Confirm',f'Are You Sure To Delete [{selection4[1]}] ?',parent=self.customer)
                if ans==1:
                    cursor.execute(f"DELETE customers WHERE cid={selection4[0]}")
                    conn.commit()
                    msg.showinfo('AL-QUDUS','Successfully Deleted',parent=self.customer)
                    self.tree_table.delete(*self.tree_table.get_children())
                    self.fetching()
                    self.show()
                else:
                    pass

        except Exception as err:
            msg.showerror('Err',f'Error Occurred Due To {err}')


    def active2(self,e):
        self.search1.config(state=NORMAL)
        self.search1.delete(0,END)



    def Searching(self):
        if self.search1.get()=='':
            msg.showerror('ERR','ID IS REQUIRED',parent=self.customer)
        else:
            try:

                # saerch
                search=self.search1.get()
                conn = pyodbc.connect(
                            "Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                            "Database=Albaraka_Shop;"
                            "Trusted_Connection=yes;"
                        )
                cursor = conn.cursor()
                cursor.execute(f"SELECT *from customers where cid={search}")
                select=cursor.fetchone()
                if select!=None:
                    for x in self.tree_table.get_children():
                        self.tree_table.delete(x)
                    self.tree_table.insert('',END,values=(select[0],select[1],select[2],select[3],select[4]))
                else:
                    msg.showerror('Error','No Record Found',parent=self.customer)

                conn.close()
            except Exception as err:
                print(err)


    def click1(self,e):
        if self.search1.get() == '':
            msg.showerror('ERR', 'ID IS REQUIRED', parent=self.customer)
        else:
            try:

                # saerch
                search2 = self.search1.get()
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=Albaraka_Shop;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f"SELECT *from customers where cid={search2}")
                select = cursor.fetchone()
                if select != None:
                    for x in self.tree_table.get_children():
                        self.tree_table.delete(x)
                    self.tree_table.insert('', END, values=(select[0],select[1],select[2],select[3],select[4]))
                else:
                    msg.showerror('Error', 'No Record Found', parent=self.customer)
                    self.search1.delete(0,END)

                conn.close()
            except Exception as err:
                print(err)


    #____________________________end function __________________________________

root=Tk()
obj=AL_QUDUS_APP(root)
root.mainloop()
