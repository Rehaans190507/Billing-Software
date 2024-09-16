from tkinter import *
import random
from tkinter import messagebox
from fpdf import FPDF

class Bill_App:
    def __init__(self, root1):
        self.total_other_prices = 0
        self.total_grocery_prices =0
        self.total_cosmetics_prices =0
        self.root = root1
        self.total_tax_en=StringVar()
        self.total_tax_en.set("RS. 0")
        self.total_cost = StringVar()
        self.total_cost.set("Rs. 0")
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=1280, height=720)
        self.root.minsize(width=1280, height=720)
        self.root.title("Billing Software")

        # ====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        # For Generating Random Bill Numbers
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()
        # Setting Value to variable
        self.c_bill_no.set(str(x))

        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.sunscreens=IntVar()
        self.Conditioners=IntVar()
        self.Deodorants=IntVar()

        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.milk=IntVar()
        self.Brown_Rice=IntVar()
        self.Nuts=IntVar()

        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()
        self.Cookies=IntVar()
        self.Candy=IntVar()
        self.Dried_Fruit=IntVar()

        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        # ===================================
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        font='inter'
        # Title of App
        Label(self.root, text="Billing Software", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
              font=(font, 30, "bold"), pady=3).pack(fill=X)

        # ==========Customers Frame==========#
        f1 = LabelFrame(text="Customer Details", font=(font, 12, "bold"), fg="gold", bg=bg_color,
                        relief=GROOVE, bd=10)
        f1.place(x=0, y=80, relwidth=10)

        # ===============Customer Name===========#
        Label(f1, text="Customer Name", bg=bg_color, fg=fg_color,
              font=(font, 13, "bold")).grid(row=0, column=0, padx=5, pady=5)
        cname_en = Entry(f1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=25, pady=5)

        # =================Customer Phone==============#
        Label(f1, text="Phone No", bg=bg_color, fg=fg_color, font=(font, 13, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(f1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=25, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(f1, text="Bill No.", bg=bg_color, fg=fg_color, font=(font, 13, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(f1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ====================Bill Search Button===============#
        bill_btn = Button(f1, text="Enter", bd=7, relief=GROOVE, font=(font, 12, "bold"), bg=bg_color,
                          fg=fg_color,command=self.check_details)
        bill_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

        # ==================Cosmetics Frame=====================#
        f2 = LabelFrame(self.root, text='Cosmetics', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f2.place(x=5, y=180, width=340, height=380)

        # ===========Frame Content
        bath_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Bath Soap")
        bath_lbl.grid(row=0, column=0, padx=0, pady=10)
        bath_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.bath_soap)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=0)

        # =======Face Cream
        face_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Cream")
        face_lbl.grid(row=1, column=0, padx=10, pady=10)
        face_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.face_cream)
        face_en.grid(row=1, column=1, ipady=5, ipadx=0)

        # ========Face Wash
        wash_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Face Wash")
        wash_lbl.grid(row=2, column=0, padx=10, pady=10)
        wash_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.face_wash)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=0)

        # ========Hair Spray
        hair_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Hair Spray")
        hair_lbl.grid(row=3, column=0, padx=10, pady=10)
        hair_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.hair_spray)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=0)

        # ============Body Lotion
        lot_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Body Lotion")
        lot_lbl.grid(row=4, column=0, padx=10, pady=10)
        lot_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.body_lotion)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=0)

        sun_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Sunscreens")
        sun_lbl.grid(row=5, column=0, padx=10, pady=10)
        sun_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.sunscreens)
        sun_en.grid(row=5, column=1, ipady=5, ipadx=0)

        cond_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Conditioners")
        cond_lbl.grid(row=6, column=0, padx=10, pady=10)
        cond_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Conditioners)
        cond_en.grid(row=6, column=1, ipady=5, ipadx=0)

        deod_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Deodorants")
        deod_lbl.grid(row=7, column=0, padx=10, pady=10)
        deod_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Deodorants)
        deod_en.grid(row=7, column=1, ipady=5, ipadx=0)

        # ==================Grocery Frame=====================#
        f2 = LabelFrame(self.root, text='Grocery', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f2.place(x=345, y=180, width=315, height=380)

        # ===========Frame Content
        rice_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10)
        rice_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        oil_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil")
        oil_lbl.grid(row=1, column=0, padx=10, pady=10)
        oil_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.food_oil)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        daal_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Daal")
        daal_lbl.grid(row=2, column=0, padx=10, pady=10)
        daal_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.daal)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        wheat_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=10)
        wheat_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        sugar_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Sugar")
        sugar_lbl.grid(row=4, column=0, padx=10, pady=10)
        sugar_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.sugar)
        sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

        milk_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Milk")
        milk_lbl.grid(row=5, column=0, padx=10, pady=10)
        milk_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.milk)
        milk_en.grid(row=5, column=1, ipady=5, ipadx=5)

        brown_rice_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Brown Rice")
        brown_rice_lbl.grid(row=6, column=0, padx=10, pady=10)
        brown_rice_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Brown_Rice)
        brown_rice_en.grid(row=6, column=1, ipady=5, ipadx=5)

        nuts_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Nuts")
        nuts_lbl.grid(row=7, column=0, padx=10, pady=10)
        nuts_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Nuts)
        nuts_en.grid(row=7, column=1, ipady=5, ipadx=5)

        # ==================Other Stuff=====================#

        f2 = LabelFrame(self.root, text='Others', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f2.place(x=655, y=180, width=315, height=380)

        # ===========Frame Content
        maza_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Maza")
        maza_lbl.grid(row=0, column=0, padx=10, pady=10)
        maza_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.maza)
        maza_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        cock_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Coke")
        cock_lbl.grid(row=1, column=0, padx=10, pady=10)
        cock_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.coke)
        cock_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        frooti_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Frooti")
        frooti_lbl.grid(row=2, column=0, padx=10, pady=10)
        frooti_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.frooti)
        frooti_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        cold_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Nimkos")
        cold_lbl.grid(row=3, column=0, padx=10, pady=10)
        cold_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.nimko)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        bis_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Biscuits")
        bis_lbl.grid(row=4, column=0, padx=10, pady=10)
        bis_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.biscuits)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        bis_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Cookies")
        bis_lbl.grid(row=5, column=0, padx=10, pady=10)
        bis_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Cookies)
        bis_en.grid(row=5, column=1, ipady=5, ipadx=5)

        bis_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Candy")
        bis_lbl.grid(row=6, column=0, padx=10, pady=10)
        bis_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Candy)
        bis_en.grid(row=6, column=1, ipady=5, ipadx=5)

        bis_lbl = Label(f2, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Dried Fruit")
        bis_lbl.grid(row=7, column=0, padx=10, pady=10)
        bis_en = Entry(f2, bd=5, relief=GROOVE, textvariable=self.Dried_Fruit)
        bis_en.grid(row=7, column=1, ipady=5, ipadx=5)

        # ===================Bill Area================#
        f3 = Label(self.root, bd=10, relief=GROOVE)
        f3.place(x=960, y=180, width=325, height=380)
        # ===========
        bill_title = Label(f3, text="Bill Area", font=(font, 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(f3, orient=VERTICAL)
        self.txt = Text(f3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        f4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=(font, 13, "bold"))
        f4.place(x=0, y=560, relwidth=1, height=160)

        # Configure columns to have equal weight
        for i in range(9):
            f4.columnconfigure(i, weight=1)

        # Buttons and labels as before
        cosm_lbl = Label(f4, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="TotalCosmetics")
        cosm_lbl.grid(row=0, column=0, padx=11, pady=0)
        cosm_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_cosmetics)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        gro_lbl = Label(f4, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Grocery")
        gro_lbl.grid(row=1, column=0, padx=11, pady=5)
        gro_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        oth_lbl = Label(f4, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Others Total")
        oth_lbl.grid(row=2, column=0, padx=11, pady=5)
        oth_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_other)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        total_cost_lbl = Label(f4, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Total cost")
        total_cost_lbl.grid(row=0, column=2, padx=30, pady=0)
        total_cost_en= Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_cost)
        total_cost_en.grid(row=0, column=3, ipady=2, ipadx=5)

        total_tax_lbl = Label(f4, font=(font, 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Tax")
        total_tax_lbl.grid(row=2, column=2, padx=10, pady=5)
        total_tax_en = Entry(f4, bd=8, relief=GROOVE, textvariable=self.total_tax_en)
        total_tax_en.grid(row=2, column=3, ipady=2, ipadx=5)

        total_btn = Button(f4, text="Total", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=0, column=4, ipadx=20, padx=10, pady=1)

        genbill_btn = Button(f4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=0, column=5, ipadx=20,padx=10, pady=1)

        clear_btn = Button(f4, text="Clear", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=0, column=6, ipadx=20, padx=10,pady=1)

        save_btn = Button(f4, text="Save", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,command=self.save_bill)
        save_btn.grid(row=2, column=4, ipadx=20,padx=10, pady=1)

        discount_button = Button(f4, text="Apply 5% Discount", bg=bg_color, fg=fg_color,font=("font", 12, "bold"), bd=7,relief=GROOVE,command=self.apply_discount)
        discount_button.grid(row=2, column=5, ipadx=20,padx=10, pady=1)

        exit_btn = Button(f4, text="Exit", bg=bg_color, fg=fg_color, font=("font", 12, "bold"), bd=7, relief=GROOVE,command=self.exit_bill)
        exit_btn.grid(row=2, column=6, ipadx=20,padx=10, pady=1)
    # Enter button
    def check_details(self):
        # Get the values from the entry fields
        name = self.cus_name.get().strip()
        phone = self.c_phone.get().strip()
        bill_no = self.c_bill_no.get().strip()

        # Check if all fields are filled
        if not name or not phone or not bill_no:
            # If any field is empty, show an error message
            messagebox.showwarning("Warning", "Please enter all customer details.")
        else:
            # Proceed to the next step (e.g., open the cosmetics and grocery section)
            self.open_next_step()
    @staticmethod
    def open_next_step():
        # This function will handle the next step after validating customer details
        # For example, you could open a new window or frame here
        messagebox.showinfo("Next step", "Select the items!")
    # Function to get total prices
    def total(self):
        # =================Total Cosmetics Prices
        self.total_cosmetics_prices = (
                (self.bath_soap.get() * 40) +
                (self.face_cream.get() * 140) +
                (self.face_wash.get() * 240) +
                (self.hair_spray.get() * 340) +
                (self.body_lotion.get() * 260)+
                (self.sunscreens.get()*600)+
                (self.Conditioners.get()*350)+
                (self.Deodorants.get()*200)
        )
        self.total_cosmetics.set("Rs. " + str(self.total_cosmetics_prices))
        # ====================Total Grocery Prices
        self.total_grocery_prices = (
                (self.wheat.get() * 100) +
                (self.food_oil.get() * 180) +
                (self.daal.get() * 80) +
                (self.rice.get() * 80) +
                (self.sugar.get() * 170)+
                (self.milk.get()*35)+
                (self.Brown_Rice.get()*90)+
                (self.Nuts.get()*100)

        )
        self.total_grocery.set("Rs. " + str(self.total_grocery_prices))
        # ======================Total Other Prices
        self.total_other_prices = (
                (self.maza.get() * 20) +
                (self.frooti.get() * 50) +
                (self.coke.get() * 60) +
                (self.nimko.get() * 20) +
                (self.biscuits.get() * 20)+
                (self.Cookies.get()*80)+
                (self.Candy.get()*5)+
                (self.Dried_Fruit.get()*200)
        )
        self.total_other.set("Rs. " + str(self.total_other_prices))
        total_before_discount = self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices
        total_tax = self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05

        # Update the Entry widget for total cost
        self.total_cost.set("Rs. " + str(total_before_discount))
        self.total_tax_en.set("Rs. " + str(total_tax))
        # Function For Text Area
    # Bill area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "       Welcome To Hanan's Retail\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n===================================")
    def bill_area(self):
        self.welcome_soft()
        if self.bath_soap.get() != 0:
            self.txt.insert(END, f"\nBath Soap         {self.bath_soap.get()}            {self.bath_soap.get() * 40}")
        if self.face_cream.get() != 0:
            self.txt.insert(END, f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 140}")
        if self.face_wash.get() != 0:
            self.txt.insert(END, f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 240}")
        if self.hair_spray.get() != 0:
            self.txt.insert(END, f"\nHair Spray        {self.hair_spray.get()}           {self.hair_spray.get() * 340}")
        if self.body_lotion.get() != 0:
            self.txt.insert(END, f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 260}")
        if self.sunscreens.get() !=0:
            self.txt.insert(END, f"\nSunscreens        {self.sunscreens.get()}           {self.sunscreens.get() * 600}")
        if self.Conditioners.get() !=0:
            self.txt.insert(END, f"\nConditioners      {self.Conditioners.get()}           {self.Conditioners.get() * 350}")
        if self.Deodorants.get() !=0:
            self.txt.insert(END, f"\nDeodorants        {self.Deodorants.get()}           {self.Deodorants.get() * 200}")
        if self.wheat.get() != 0:
            self.txt.insert(END, f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END, f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END, f"\nDaal              {self.daal.get()}            {self.daal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END, f"\nRice              {self.rice.get()}            {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txt.insert(END, f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 170}")
        if self.milk.get() !=0:
            self.txt.insert(END, f"\nMilk              {self.milk.get()}            {self.milk.get() * 35}")
        if self.Brown_Rice.get() !=0:
            self.txt.insert(END, f"\nBrown Rice        {self.Brown_Rice.get()}            {self.Brown_Rice.get() * 90}")
        if self.Nuts.get() !=0:
            self.txt.insert(END, f"\nNuts              {self.Nuts.get()}           {self.Nuts.get() * 100}")
        if self.maza.get() != 0:
            self.txt.insert(END, f"\nMaza              {self.maza.get()}            {self.maza.get() * 20}")
        if self.frooti.get() != 0:
            self.txt.insert(END, f"\nFrooti            {self.frooti.get()}            {self.frooti.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END, f"\nCoke              {self.coke.get()}            {self.coke.get() * 60}")
        if self.nimko.get() != 0:
            self.txt.insert(END, f"\nNimko             {self.nimko.get()}            {self.nimko.get() * 20}")
        if self.biscuits.get() != 0:
            self.txt.insert(END, f"\nBiscuits          {self.biscuits.get()}            {self.biscuits.get() * 20}")
        if self.Cookies.get() !=0:
            self.txt.insert(END, f"\nCookies           {self.Cookies.get()}            {self.Cookies.get() * 80}")
        if self.Candy.get() !=0:
            self.txt.insert(END, f"\nCandy             {self.Candy.get()}             {self.Candy.get() * 5}")
        if self.Dried_Fruit.get() !=0:
            self.txt.insert(END, f"\nDried_Fruit       {self.Dried_Fruit.get()}           {self.Dried_Fruit.get() * 200}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n                      Total : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices}")

        self.txt.insert(END,
                        f"\n              Total With Tax: {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}")
        self.txt.insert(END,
                        f"\n  ")
        self.txt.insert(END,
                        f"\n  ")
        self.txt.insert(END,
                        f"\n                       Total: {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}")
    # After Discount
    def apply_discount(self):
        # Calculate the total with discount
        self.total()  # Recalculate totals
        total_before_discount = self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices
        total_tax = self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05
        discount_amount = (5 / 100) * (total_before_discount + total_tax)
        final_total = (total_before_discount + total_tax) - discount_amount
        # Update the bill area with the discount applied
        self.bill_area_with_discount(final_total)
    def bill_area_with_discount(self, final_total):
        self.txt.delete('1.0', END)  # Clear previous content
        self.welcome_soft()  # Re-add the initial content

        # Add products and prices to the bill area
        if self.bath_soap.get() != 0:
            self.txt.insert(END, f"\nBath Soap         {self.bath_soap.get()}            {self.bath_soap.get() * 40}")
        if self.face_cream.get() != 0:
            self.txt.insert(END, f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 140}")
        if self.face_wash.get() != 0:
            self.txt.insert(END, f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 240}")
        if self.hair_spray.get() != 0:
            self.txt.insert(END, f"\nHair Spray        {self.hair_spray.get()}           {self.hair_spray.get() * 340}")
        if self.body_lotion.get() != 0:
            self.txt.insert(END,
                            f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 260}")
        if self.sunscreens.get() != 0:
            self.txt.insert(END, f"\nSunscreens        {self.sunscreens.get()}           {self.sunscreens.get() * 600}")
        if self.Conditioners.get() != 0:
            self.txt.insert(END,
                            f"\nConditioners      {self.Conditioners.get()}           {self.Conditioners.get() * 350}")
        if self.Deodorants.get() != 0:
            self.txt.insert(END, f"\nDeodorants        {self.Deodorants.get()}           {self.Deodorants.get() * 200}")
        if self.wheat.get() != 0:
            self.txt.insert(END, f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END, f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END, f"\nDaal              {self.daal.get()}            {self.daal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END, f"\nRice              {self.rice.get()}            {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txt.insert(END, f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 170}")
        if self.milk.get() != 0:
            self.txt.insert(END, f"\nMilk              {self.milk.get()}            {self.milk.get() * 35}")
        if self.Brown_Rice.get() != 0:
            self.txt.insert(END, f"\nBrown Rice        {self.Brown_Rice.get()}            {self.Brown_Rice.get() * 90}")
        if self.Nuts.get() != 0:
            self.txt.insert(END, f"\nNuts              {self.Nuts.get()}           {self.Nuts.get() * 100}")
        if self.maza.get() != 0:
            self.txt.insert(END, f"\nMaza              {self.maza.get()}            {self.maza.get() * 20}")
        if self.frooti.get() != 0:
            self.txt.insert(END, f"\nFrooti            {self.frooti.get()}            {self.frooti.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END, f"\nCoke              {self.coke.get()}            {self.coke.get() * 60}")
        if self.nimko.get() != 0:
            self.txt.insert(END, f"\nNimko             {self.nimko.get()}            {self.nimko.get() * 20}")
        if self.biscuits.get() != 0:
            self.txt.insert(END, f"\nBiscuits          {self.biscuits.get()}            {self.biscuits.get() * 20}")
        if self.Cookies.get() != 0:
            self.txt.insert(END, f"\nCookies           {self.Cookies.get()}            {self.Cookies.get() * 80}")
        if self.Candy.get() != 0:
            self.txt.insert(END, f"\nCandy             {self.Candy.get()}             {self.Candy.get() * 5}")
        if self.Dried_Fruit.get() != 0:
            self.txt.insert(END,  f"\nDried_Fruit       {self.Dried_Fruit.get()}           {self.Dried_Fruit.get() * 200}")

        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n                      Total : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices}")
        self.txt.insert(END,
                        f"\n             Total With Tax : {self.total_cosmetics_prices + self.total_grocery_prices + self.total_other_prices + self.total_cosmetics_prices * 0.05 + self.total_grocery_prices * 0.05 + self.total_other_prices * 0.05}")
        self.txt.insert(END, f"\n Total after 5% Discount: Rs. {round(final_total, 2)}")
        self.txt.insert(END,
                        f"\n  ")
        self.txt.insert(END,
                        f"\n  ")
        self.txt.insert(END, f"\n                       Total. {round(final_total, 2)}")
    # Save to pdf Function
    def save_bill(self):
        # Check if the Bill Area is empty
        bill_content = self.txt.get(1.0, END).strip()
        if not bill_content:
            # Display a message box if the Bill Area is empty
            messagebox.showwarning("Warning", "The Bill Area is empty! Please generate a bill before saving.")
            return  # Exit the method without saving
        # Create an instance of FPDF
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # Set font (must add at least one font)
        pdf.set_font("Arial", size=12)
        # Add the bill content
        for line in bill_content.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)
        # Save the PDF with a predefined filename or prompt for a filename
        pdf_file = "Bill.pdf"
        pdf.output(pdf_file)
        # Display a message box indicating the PDF is saved
        messagebox.showinfo("Saved", f"Bill has been saved as {pdf_file}!")
    # Function To Clear All Fields
    def clear(self):
        # Clear the text widget
        self.txt.delete('1.0', END)

        # Reset all Entry fields
        self.bath_soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.body_lotion.set(0)
        self.sunscreens.set(0)
        self.Conditioners.set(0)
        self.Deodorants.set(0)
        self.wheat.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.rice.set(0)
        self.sugar.set(0)
        self.milk.set(0)
        self.Brown_Rice.set(0)
        self.Nuts.set(0)
        self.maza.set(0)
        self.frooti.set(0)
        self.coke.set(0)
        self.nimko.set(0)
        self.biscuits.set(0)
        self.Cookies.set(0)
        self.Candy.set(0)
        self.Dried_Fruit.set(0)

        # Reset all Label fields
        self.total_cosmetics.set("Rs. 0")
        self.tax_cos.set("Rs. 0")
        self.total_grocery.set("Rs. 0")
        self.tax_groc.set("Rs. 0")
        self.total_other.set("Rs. 0")
        self.tax_other.set("Rs. 0")
        self.total_cost.set("Rs. 0")
        self.total_tax_en.set("Rs. 0")
    # Exit function
    def exit_bill(self):
        self.root.destroy()


root = Tk()
object = Bill_App(root)
root.mainloop()