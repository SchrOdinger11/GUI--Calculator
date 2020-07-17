from tkinter import *

lbl1=Label( text='First number')
lbl2=Label( text='Second number')
lbl3=Label( text='Result')
t1=Entry()
t2=Entry()
t3=Entry()

def add():
    t3.delete(0, 'end')
    ArithmeticErrornum1=int(t1.get())
    num2=int(t2.get())
    result=num1+num2
    t3.insert(END, str(result))
def sub( ):
    t3.delete(0, 'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1-num2
    t3.insert(END, str(result))
def mul():
    t3.delete(0,'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1*num2
    t3.insert(END, str(result))
def div():
    t3.delete(0,'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1/num2
    t3.insert(END, str(result))
btn1 = Button( text='Add')
btn2=Button( text='Subtract')
btn3=Button(text='multiplication')
btn4=Button(text='divide')
lbl1.place(x=100, y=50)
t1.place(x=200, y=50)
lbl2.place(x=100, y=100)
t2.place(x=200, y=100)
b1=Button(text='Add', command=add)
b2=Button(text='Subtract',command=sub)
b3=Button(text='Multiplication',command=mul)
b4=Button(text='Divide(first number is numerator'),command=div)
#b2.bind('<Button-1>', sub)
b1.place(x=100, y=150)
b2.place(x=200, y=150)
b3.place(x=300, y=150) 
b4.place(x=400, y=150)

lbl3.place(x=100, y=200)
t3.place(x=200, y=200)


window=Tk()

window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()

