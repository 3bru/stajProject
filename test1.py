from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
from backend import Database

database = Database("staj.db")

def view_command(): #Komutları listboxta göster
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    database.delete(selected_tuple[0])


def get_selected_row(event):
    try:
        index = list1.curselection()[0]  # get cursor index
        print(index)
        global selected_tuple
        selected_tuple = list1.get(index)

        # replace field values with current selected row values
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])

    except IndexError:
        pass


window = Tk()

window.wm_title("StajGünlügü")
window.geometry("700x500")
window.configure(background="orange")

l1 = Label(window, text="baslik")#title
l1.grid(row=0, column=0)

l2 = Label(window, text="yazan")#author
l2.grid(row=0, column=2)

l3 = Label(window, text="gün")#year
l3.grid(row=1, column=0)

l4 = Label(window, text="günün konusu", width=18)#isbn
l4.grid(row=1, column=2, sticky=E)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=6)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)


isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=6, padx=10, pady=8, sticky=E, columnspan=4)

#------------------------------------------------------------------------------------------------------------
list1 = Listbox(window, height=8, width=40)
list1.grid(row=12, column=0, rowspan=8, columnspan=8)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=12, column=2, rowspan=6, columnspan=14)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=12, column=10)

b2 = Button(window, text="Add entry", width=12, command=add_command)
b2.grid(row=13, column=10)

b3 = Button(window, text="Update selected", width=12, command=update_command)
b3.grid(row=14, column=10)

b4 = Button(window, text="Delete selected", width=12, command=delete_command)
b4.grid(row=15, column=10)

b5 = Button(window, text="Close", width=12, command=window.destroy)
b5.grid(row=17, column=10)

window.mainloop()