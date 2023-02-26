from tkinter import *

def miles_to_kms():
    m=float(miles_input.get())
    km= m*1.60934
    km_label.config(text=f"{km}")



window=Tk()
window.title("Miles to Kilometer converter")
window.config(padx=150, pady=150)
window.minsize(width=300, height=300)


miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)


label = Label(text="Miles" )
label.grid(column=2,row=0)

label1 = Label(text="is equal to")
label1.grid(column=0,row=1)

km_label = Label(text="0")
km_label.grid(column=1,row=1)

km_label1 = Label(text="km")
km_label1.grid(column=2,row=1)


calculate = Button(text="Calculate" ,command= miles_to_kms)
calculate.grid(column=1 , row=2)


window.mainloop()

