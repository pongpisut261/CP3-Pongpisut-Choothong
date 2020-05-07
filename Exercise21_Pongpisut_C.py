from tkinter import *
import math

def leftClickButton(event):
    bmi = (float(textboxWeight.get()) / math.pow(float(textboxHeight.get()) / 100, 2))
    if bmi  >= 30:
        labelResult2.configure(text = "อ้วนมาก")
    elif bmi >= 25:
        labelResult2.configure(text="อ้วน")
    elif bmi >= 23:
        labelResult2.configure(text="น้ำหนักเกิน")
    elif bmi >= 18.6:
        labelResult2.configure(text="น้ำหนักปกติ")
    else:
        labelResult2.configure(text="ผอมเกินไป")
    print(bmi)
    labelBMI2.configure(text = bmi)


main = Tk()
labelHeight = Label(main,text = "ส่วนสูง (ซม.)")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(main,)
textboxHeight.grid(row=0,column=1)
labelWeight = Label(main,text = "น้ำหนัก (กก.)")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(main,)
textboxWeight.grid(row=1,column=1)
labelBMI = Label(main,text = "ดัชนีมวลกาย")
labelBMI.grid(row=2,column=0)
labelBMI2 = Label(main,text = "")
labelBMI2.grid(row=2,column=1)
labelResult = Label(main,text = "อยู่ในเกณฑ์")
labelResult.grid(row=3,column=0)
labelResult2 = Label(main,text = "")
labelResult2.grid(row=3,column=1)
calcButton = Button(main,text = "คำนวณ")
calcButton.bind('<Button-1 >',leftClickButton)
calcButton.grid(row=4,column=1)

main.mainloop()