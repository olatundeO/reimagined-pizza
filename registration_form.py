from tkinter import *
import os
import shutil

class Registration(Frame):
    def __init__(self, master):
        super(Registration, self).__init__(master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.lbl_empty = Label(self, text = "Application Form ").grid(row = 0, column = 1)

        line = 1

        self.lbl_lname = Label(self, text = "Lastname: ")
        self.lbl_lname.grid(row = line, column = 0, sticky = W)

        self.ent_lname = Entry(self, text = "")
        self.ent_lname.grid(row = line, column = 1, sticky = W)

        line += 1

        self.lbl_empty = Label(self, text=" ").grid(row=line, column=0)

        line += 1

        self.lbl_fname = Label(self, text = "Firstname: ")
        self.lbl_fname.grid(row = line, column = 0, sticky = W)

        self.ent_fname = Entry(self, text="")
        self.ent_fname.grid(row = line, column = 1, sticky = W)

        line += 1
        self.lbl_empty = Label(self, text=" ").grid(row=line, column=0)

        line += 1

        self.lbl_email = Label(self, text = "Email: ")
        self.lbl_email.grid(row = line, column = 0, sticky = W)

        self.ent_email = Entry(self, text = "")
        self.ent_email.grid(row = line, column = 1, sticky = W)

        line += 1
        self.lbl_empty = Label(self, text=" ").grid(row=line, column=0)

        line += 1
        self.lbl_gender = Label(self, text = "Gender: ")
        self.lbl_gender.grid(row = line, column = 0, sticky = W)

        self.gender = StringVar()
        self.gend_frame = Frame(self)
        self.gend_frame.grid(row=line, column=1, sticky=W)

        self.rad_male = Radiobutton(self.gend_frame, text = "Male", value = "Male", variable = self.gender)
        self.rad_male.grid(row = line, column = 0, sticky = W)

        self.rad_female = Radiobutton(self.gend_frame, text = "Female", value = "Female", variable = self.gender)
        self.rad_female.grid(row = line, column = 1, sticky = W)

        self.rad_male.select()

        line += 1
        self.lbl_empty = Label(self, text=" ").grid(row=line, column=1)

        line += 1
        self.qual_values = ["Select", "SSCE", "OND", "HND", "BSC", "MSC", "PHD"]
        self.qual = StringVar()
        self.lbl_qual = Label(self, text = "Qualification: ")
        self.lbl_qual.grid(row = line, column = 0, sticky = W)
        self.option_qual = OptionMenu(self, self.qual, *self.qual_values)
        self.option_qual.grid(row = line, column = 1, sticky = W)
        self.qual.set(self.qual_values[0])

        line += 1
        self.lbl_empty = Label(self, text=" ").grid(row=line, column=1)

        line += 1
        self.lbl_ps = Label(self, text = "Personal Statement: ")
        self.lbl_ps.grid(row = line, column = 0, sticky = N)

        self.txt_ps = Text(self, width = 20, height = 5)
        self.txt_ps.grid(row = line, column = 1, sticky = W)

        line += 1
        self.lbl_empty = Label(self, text=" ").grid(row=line, column=1)

        line += 1
        self.btn_submit = Button(self, text = "Submit", width = 10, command = self.submit)
        self.btn_submit.grid(row = line, column = 0, sticky = E)

        self.btn_reset = Button(self, text = "Reset", width = 10, command = self.reset)
        self.btn_reset.grid(row = line, column = 1, sticky = W)

    def reset(self):
        self.ent_lname.delete(0, END)
        self.ent_fname.delete(0, END)
        self.ent_email.delete(0, END)

        self.rad_male.select()

        self.qual.set(self.qual_values[0])

        self.txt_ps.delete("1.0", "2.0")


    def submit(self):
        self.details = []
        self.details.append("Firstname: " + self.ent_fname.get())
        self.details.append("\nLastname: " + self.ent_lname.get())
        self.details.append("\nEmail: " + self.ent_email.get())

        if self.gender.get() == "Male":
            self.details.append("\nGender: " + "Male")
        elif self.gender.get() == "Female":
            self.details.append("\nGender: " + "Female")

        if self.qual.get() == self.qual_values[0]:
            self.details.append("\nQualification: " + "no item selected")
        else:
            for i in range(len(self.qual_values)):
                if self.qual.get() == self.qual_values[i]:
                    self.details.append("\nQualification: " + self.qual.get())

        self.details.append("\nPersonal Statement: " + self.txt_ps.get("1.0", END))

        try:
            self.infile = open(r"C:\Users\KAYODE OGUNSANYA\Desktop\python tutorial\gui.txt", "a")
            for i in self.details:
                self.infile.write("%s\n" % i)
            self.infile.close()
        except TypeError:
            print("could not carry out operation")
        except ValueError:
            print("I/O operation on closed file")
        finally:
            self.infile.close()
            print("file closed")


window = Tk()
window.title("Application Form")
window.geometry("300x400")
app = Registration(window)
app.mainloop()