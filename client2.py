import socket
from tkinter import *
from tkinter import messagebox

def clicked():
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    address = ('127.0.0.1',2000)

    var = txt.get()
    client.sendto(var.encode('utf-8'), address)
    res = client.recv(2048).decode('utf-8')
    messagebox.showinfo('Connected', f'{res}')

window = Tk()  
window.title("Client")  
window.geometry('350x200')


lbl = Label(window, text="Введите параметр а:", height = 5)  
lbl.grid(column=1, row=0)
txt = Entry(window,width=10)  
txt.grid(column=2, row=0)
con = Button(window, text="Подключиться к серверу!", command=clicked)
con.grid(column =2, row = 3)

window.mainloop()

