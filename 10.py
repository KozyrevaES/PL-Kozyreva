from tkinter import * 
from tkinter import ttk 
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog as fd

win = Tk() 
win.title("Козырева Е.С.") 
win.geometry('400x250')

tab_control = ttk.Notebook(win)
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая') 
tab_control.add(tab3, text='Третья') 

def calcul():
    try:
        result = eval(display.get())
        input_text.set(result)
    except:
        input_text.set("Ошибка!")

input_text = tk.StringVar()
display = tk.Entry(tab1, textvariable=input_text, width=28)
display.grid(row=0, columnspan=4, ipady=10)

tk.Button(tab1, text="(", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("("))).grid(row=1, column=0)
tk.Button(tab1, text=")", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(")"))).grid(row=1, column=1)
tk.Button(tab1, text="С", width=5, height=1, command=lambda: display.delete(len(display.get())-1)).grid(row=1, column=2)
tk.Button(tab1, text="=", width=5, height=1, command=calcul).grid(row=1, column=3)

tk.Button(tab1, text="1", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(1))).grid(row=2, column=0)
tk.Button(tab1, text="2", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(2))).grid(row=2, column=1)
tk.Button(tab1, text="3", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(3))).grid(row=2, column=2)
tk.Button(tab1, text="+", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("+"))).grid(row=2, column=3)

tk.Button(tab1, text="4", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(4))).grid(row=3, column=0)
tk.Button(tab1, text="5", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(5))).grid(row=3, column=1)
tk.Button(tab1, text="6", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(6))).grid(row=3, column=2)
tk.Button(tab1, text="-", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("-"))).grid(row=3, column=3)

tk.Button(tab1, text="7", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(7))).grid(row=4, column=0)
tk.Button(tab1, text="8", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(8))).grid(row=4, column=1)
tk.Button(tab1, text="9", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(9))).grid(row=4, column=2)
tk.Button(tab1, text="x", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("*"))).grid(row=4, column=3)

tk.Button(tab1, text="C", width=5, height=1, command=lambda: input_text.set("")).grid(row=5, column=0)
tk.Button(tab1, text="0", width=5, height=1, command=lambda: display.insert(tk.INSERT, str(0))).grid(row=5, column=1)
tk.Button(tab1, text=".", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("."))).grid(row=5, column=2)
tk.Button(tab1, text="/", width=5, height=1, command=lambda: display.insert(tk.INSERT, str("/"))).grid(row=5, column=3)

def V():
	messagebox.showinfo('Информация', chk_state.get())
	
chk_state = StringVar() 
chk_state.set('No')
chk1 = Checkbutton(tab2, text='Первый', variable=chk_state, onvalue="1 вариант")
chk2 = Checkbutton(tab2, text='Второй', variable=chk_state, onvalue="2 вариант") 
chk3 = Checkbutton(tab2, text='Третий', variable=chk_state, onvalue="3 вариант")  
chk1.grid(column=1, row=1)
chk2.grid(column=1, row=2)
chk3.grid(column=1, row=3)

bt= Button(tab2, text = 'Клик', command = V)
bt.grid(column=1, row=4)

def clear():
    my_text.delete(1.0, END)

def open_file():
	file = fd.askopenfilename()
	with open(file, "r+", encoding="utf-8-sig") as f:
		line = f.read()
		my_text.insert("1.0", line)
		my_text.place(x=0,y=0)

my_text = Text(tab3, width=60, height=20)
my_text.pack(pady=20)
button_frame = Frame(tab3)
button_frame.pack()

menu = Menu(tab3) 
new_item = Menu(menu) 
new_item.add_command(label='Добавить',command=open_file)
new_item.add_separator()
menu.add_cascade(label="Файл",menu=new_item)
win.config(menu=menu)

tab_control.pack(expand=1, fill='both') 
win.mainloop()
