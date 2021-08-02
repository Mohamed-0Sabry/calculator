from tkinter import *
calculator = Tk()
calculator.title("MSN2")

e = Entry(calculator, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def clickButton(number):
    currentNumber = e.get()
    e.delete(0, END)
    e.insert(0, str(currentNumber) + str(number))

def clearButton():
    e.delete(0, END)

def addBUtton():
    firstNumber = e.get()
    global fNumber
    global math 
    math = "addition"
    fNumber = int(firstNumber)
    e.delete(0, END)

def subtractButton():
    firstNumber = e.get()
    global fNumber
    global math 
    math = "subtraction"
    fNumber = int(firstNumber)
    e.delete(0, END)


def multiplyButton():
    firstNumber = e.get()
    global fNumber
    global math 
    math = "multiplication"
    fNumber = int(firstNumber)
    e.delete(0, END)


def dividButton():
    firstNumber = e.get()
    global fNumber
    global math 
    math = "division"
    fNumber = int(firstNumber)
    e.delete(0, END)

def equalButton():
    secondNumber = e.get()
    e.delete(0, END)


    if math == "addition":
        e.insert(0, fNumber + int(secondNumber))
    if math == "subtraction":
        e.insert(0, fNumber - int(secondNumber))
    if math == "multiplication":
        e.insert(0, fNumber * int(secondNumber))
    if math == "division":
        e.insert(0, fNumber / int(secondNumber))

button1 = Button(calculator, text = "1", padx = 60, pady = 20, command = lambda: clickButton(1))
button2 = Button(calculator, text = "2", padx = 60, pady = 20, command = lambda: clickButton(2))
button3 = Button(calculator, text = "3", padx = 60, pady = 20, command = lambda: clickButton(3))
button4 = Button(calculator, text = "4", padx = 60, pady = 20, command = lambda: clickButton(4))
button5 = Button(calculator, text = "5", padx = 60, pady = 20, command = lambda: clickButton(5))
button6 = Button(calculator, text = "6", padx = 60, pady = 20, command = lambda: clickButton(6))
button7 = Button(calculator, text = "7", padx = 60, pady = 20, command = lambda: clickButton(7))
button8 = Button(calculator, text = "8", padx = 60, pady = 20, command = lambda: clickButton(8))
button9 = Button(calculator, text = "9", padx = 60, pady = 20, command = lambda: clickButton(9))
button0 = Button(calculator, text = "0", padx = 60, pady = 20, command = lambda: clickButton(0))

buttonAdd = Button(calculator, text = "+", padx = 59, pady = 20, command = addBUtton)
buttonSubtract = Button(calculator, text = "-", padx = 61, pady = 20, command = subtractButton)
buttonMultiply = Button(calculator, text = "X", padx = 61, pady = 20, command = multiplyButton)
buttonDivide = Button(calculator, text = "/", padx = 62, pady = 20, command = dividButton)
buttonEqual = Button(calculator, text = "=", padx = 127, pady = 20, command = equalButton)
buttonClear = Button(calculator, text = "Clear", padx = 116, pady = 20, command = clearButton)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=2)

buttonAdd.grid(row=4, column=1)
buttonSubtract.grid(row=4, column=0)
buttonMultiply.grid(row=5, column=0)
buttonDivide.grid(row=6, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
buttonClear.grid(row=6, column=1, columnspan=2)
calculator.mainloop()




