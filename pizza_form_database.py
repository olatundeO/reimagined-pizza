from tkinter import *
import sqlite3

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        #self.toppings = ["Sausage", "Pepperoni", "Chicken", "Mushroom", "Black Olive", "Green Pepper", "Red Pepper","Onion"]
        #self.prices = {"medium":1500, "large":2500, "xlarge":4500, "m_toppings":0.05, "l_toppings":0.10, "x_toppings":0.15}

        self.toppings = []
        self.prices = {"medium":0, "large":0, "xlarge":0, "m_toppings":0, "l_toppings":0, "x_toppings":0}

        self.conn = sqlite3.connect('pizza.db')
        self.cursor = self.conn.cursor()

        for row in self.cursor.execute('SELECT * FROM Prices'):
            self.prices[row[0]] = row[1]

        for row in self.cursor.execute('SELECT * FROM Toppings order by topping'):
            self.toppings.append(row[0])

        self.chk = list(self.toppings)
        self.chkVar = list(self.toppings)

        self.lbl_ss = Label(self, text = "Select size: ")
        self.lbl_ss.grid(row = 0, column = 0, sticky = W)

        self.size = StringVar()

        self.rad_medium = Radiobutton(self, text = "Medium", value = "medium", variable = self.size)
        self.rad_medium.grid(row = 1, column = 0, sticky = W)

        self.rad_large = Radiobutton(self, text = "Large", value = "large", variable = self.size)
        self.rad_large.grid(row = 1, column = 1, sticky = W)

        self.rad_xlarge = Radiobutton(self, text="Extra Large", value="xlarge", variable = self.size)
        self.rad_xlarge.grid(row=1, column=2, sticky=W)

        self.rad_medium.select()

        self.lbl_empty = Label(self, text = " ")
        self.lbl_empty.grid(row = 2, column = 0, sticky = W)

        self.lbl_st = Label(self, text = "Select Toppings: ")
        self.lbl_st.grid(row = 3, column = 0, sticky = W)

        line = 4

        for i in range(len(self.toppings)):
            self.chkVar[i] = BooleanVar()
            self.chk[i] = Checkbutton(self, text = self.toppings[i], variable = self.chkVar[i])
            self.chk[i].grid(row = line, column = 1, sticky = W)
            line += 1

        line += 1
        self.lbl_empty = Label(self, text = " ")
        self.lbl_empty.grid(row = line, column = 0, sticky = W)

        line += 1
        self.btn_reset = Button(self, text = "Reset", width = 10, command = self.reset)
        self.btn_reset.grid(row = line, column = 0)

        self.btn_calcprice = Button(self, text = "Calculate Price", width = 14, command = self.calculate)
        self.btn_calcprice.grid(row = line, column = 1, sticky = W)

        line += 1
        self.empty_space = Label(self, text = " ")
        self.empty_space.grid(row = line, column = 0)

        line += 1
        self.lbl_price = Label(self, text = "Price:")
        self.lbl_price.grid(row = line, column = 0)

        self.ent_price = Entry(self, width = 15)
        self.ent_price.grid(row = line, column = 1, sticky = W)

    def reset(self):
        self.rad_medium.select()
        for i in range(len(self.toppings)):
            self.chk[i].deselect()
        self.ent_price.delete(0, END)

    def calculate(self):
        self.ent_price.delete(0, END)
        self.total_toppings = 0
        self.total_prices = 0

        for i in range(len(self.toppings)):
            if self.chkVar[i].get():
                self.total_toppings += 1

        if self.total_toppings == 0:
            self.ent_price.insert(END, 0)

        else:
            if self.size.get() == "medium":
                self.total_prices = self.prices["medium"] + (
                            self.prices["medium"] * self.prices["m_toppings"] * self.total_toppings)

            elif self.size.get() == "large":
                self.total_prices = self.prices["large"] + (
                            self.prices["large"] * self.prices["l_toppings"] * self.total_toppings)

            elif self.size.get() == "xlarge":
                self.total_prices = self.prices["xlarge"] + (
                            self.prices["xlarge"] * self.prices["x_toppings"] * self.total_toppings)

            self.ent_price.insert(END, self.total_prices)




window = Tk()
window.title("Pizza Party")
window.geometry("300x400")
app = Application(window)
app.mainloop()

