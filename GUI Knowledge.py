from tkinter import *
from tkinter import ttk    #Theme Of tk
from tkinter import messagebox
GUI = Tk()  #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')   #ชื่อโปรแกรม
GUI.geometry('500x400')  # ขนาดของปุ่ม

#B1 = ttk.Button(GUI,text='Show me the Money')
#B1.pack(ipadx=20,ipady=20)


L1 = Label (GUI,text='โปรแกรมบันทึกข้อมูลคอมพิวเตอร์',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

################################
def Button1():
    text = 'CPU Temp =45c'
    messagebox.showinfo('CPU Temp',text)

#B2 = Button(GUI,text='Show me the Money')
#B2.pack()
#B2.place(x=50,y=50)
FB1 = Frame(GUI)   #คล้ายกระดาน
FB1.place(x=50,y=70)
B1 = ttk.Button(FB1,text='Show CPU Temp',command=Button1)
B1.pack(ipadx=20,ipady=20)


def Button2():
    text = 'Memory Usage = 50%'
    messagebox.showinfo('Show Memory Usage',text)


FB2 = Frame(GUI)   #คล้ายกระดาน
FB2.place(x=50,y=140)
B2 = ttk.Button(FB2,text='Show Memory Usage',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'Storage Usage = 30%'
    messagebox.showinfo('Show Storage Usage',text)


FB3 = Frame(GUI)   #คล้ายกระดาน
FB3.place(x=50,y=210)
B3 = ttk.Button(FB3,text='Show Storage Usage',command=Button3)
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()

