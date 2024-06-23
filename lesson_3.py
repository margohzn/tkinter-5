from tkinter import * 

window = Tk()
window.geometry("500x500")
window.config(background = "pink")

items = Label(window, text = "Ice cream and chocos", font = "50").pack()

#creating frame 
frame = Frame(window).pack()
bottom_frame = Frame(window).pack(side = BOTTOM)

b1 = Button(frame, text = "choco", fg = "pink")
b1.pack(side = LEFT)
b3 = Button(frame, text = "pastrys", fg = "blue").pack(side = LEFT)

b2 = Button(bottom_frame, text = "ice cream", fg = "blue").pack(side = BOTTOM)
b4 = Button(bottom_frame, text = "bread", fg = "green").pack(side = BOTTOM)


window.mainloop()