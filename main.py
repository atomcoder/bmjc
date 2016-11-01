# coding = utf-8

import tkinter
import list_net_interface

app = tkinter.Tk()
app.title('Tools by Atom')
app.geometry('800x600')

label1 = tkinter.Label(app, text=list_net_interface.list_net_interface())
label1.pack()

app.mainloop()
