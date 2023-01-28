import socket
from tkinter import *

def fact(k):
    if k==0: return 1
    if k < 1: return 0
    
    else: return k * fact(k - 1)
##Функція з факторіалом
def clicked():  
    btn.configure(text="Сервер запущен")
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind(('127.0.0.1',2000))
    
    val, ip = server.recvfrom(1024)
    a = int(val); b = 0.75; c = 5.25; x = 0.7; y = 4; i = 0
    for i in range(5):
        func = pow(-1,i+5)*a*x+b*y+pow(c,x*y)/fact(i)*pow(x,y)
    func = round(func , 3)
    print(f"Result: {func}")    
    res = f"Your result :{func}".encode('utf-8')
    server.sendto(res, ip)    
window = Tk()  
window.title("Server")  
window.geometry('300x200')
##Кнопка

dsc = Label (window , text = "Server address: 127.0.0.1 \n Port: 2000", width=40,height = 5)
dsc.grid(column = 0, row = 0)


btn = Button(window, text="Запустить сервер!", command=clicked)  
btn.grid(column=0, row=2)
window.mainloop()




