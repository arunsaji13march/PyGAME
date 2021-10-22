# from tkinter import *
# from PIL import ImageTk,Image
# win = Tk()
#
# win.iconbitmap('ninja.png')
#
# img=ImageTk.PhotoImage(Image.open('itachi.jpg'))
# img_la=Label(image=img,padx=90,pady=50).pack()
#
#
# def meth():
#     la = Label(win, text="Man")
#     la.pack()
# b=Button(win,text="click",command=meth,).pack()
# exit=Button(win,text="X",command=win.quit).pack()
#
# win.mainloop()
def fun(t,age):
    print("what are u learning ?"+t.title()+'ur age?'+str(age))

fun('tarun',16)