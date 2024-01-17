from tkinter import *
import calendar

text = calendar.calendar(2023)
root = Tk()
root.geometry("1000x1000")
root.title("calendar")
label1 = Label(root, text = "calendar", bg = 'white', font = ('times',28, 'bold'))
label1.grid(row=1, column=1)
root.config(background = 'white')
l1 =Label(root, text = text, font = "Consolas 10")
l1.grid(row=2,column=1, padx=20)
root.mainloop()