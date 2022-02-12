from tkinter import *
from math import *

def calculateBMI():
	x = float(txtBoxWeight.get())
	y = float(txtBoxHeight.get()) / 100
	result = x / pow(y, 2)
	txtResult = "{:.1f}".format(result)
	if result >= 30:
		return lblResult.configure(text=txtResult + " / อ้วนมาก", fg="red")
	elif result >= 25:
		return lblResult.configure(text=txtResult + " / อ้วน", fg="red")
	elif result >= 23:
		return lblResult.configure(text=txtResult + " / น้ำหนักเกิน", fg="red")
	elif result >= 18.6:
		return lblResult.configure(text=txtResult + " / เหมาะสม", fg="green")
	elif result <= 18.5:
		return lblResult.configure(text=txtResult + " / ผอมเกินไป")
	else:
		return lblResult.configure(text="Error", fg="red")

frame = Tk()
frame.title("BMI Calculator")

lblWeight = Label(frame, text="Your Weight (kg)").grid(row=0,column=0)

txtBoxWeight = Entry(frame)
txtBoxWeight.get()
txtBoxWeight.grid(row=0, column=1)

lblHeight = Label(frame, text="Your Height (cm)").grid(row=1, column=0)

txtBoxHeight = Entry(frame)
txtBoxHeight.get()
txtBoxHeight.grid(row=1, column=1)

btnCal = Button(frame, text="BMI Calculation", command=calculateBMI)
btnCal.grid(row=3, column=0)

lblResult = Label(frame, text="Result")
lblResult.grid(row=3, column=1)

frame.mainloop()
