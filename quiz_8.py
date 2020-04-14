#Linh

import tkinter as tk
from tkinter import font as tkFont
import math

def button(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def equal():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""

    except:
        equation.set("Error")
        expression = ""

def sqrt():
    global expression
    result = str(math.sqrt(float(expression)))
    equation.set(result)
    expression = ""

def bigger():
    text_size = font_size.cget('size') + 2
    font_size.configure(size = text_size)

def smaller():
    text_size = font_size.cget('size') - 2
    font_size.configure(size = text_size)

def clear():
    global expression
    expression = ""
    equation.set("")

def back():
    global expression
    expression = expression[:-1]
    equation.set(expression)
    
if __name__ == "__main__":

    expression = ""
    window = tk.Tk()
    window.title("Simple Calculator")
    window.configure(bg = "#43a2ca")
    window.geometry("500x300")

    font_size = tkFont.Font(size = 12)

    equation = tk.StringVar()

    display = tk.Entry(window, border = 5, font = font_size,
                       textvariable = equation)
    display.grid(columnspan = 4, ipadx=100, ipady=15, sticky = 'NSEW')

    equation.set('0')

    bigger_button = tk.Button(window, text = '<<o>>', font=font_size,
                              fg = 'black', bg = '#a8ddb5', command = bigger,
                              height = 2, width = 7)
    bigger_button.grid(row = 1, column = 0, sticky = 'NSEW')

    smaller_button = tk.Button(window, text = '>>.<<', font=font_size,
                               fg = 'black', bg = '#a8ddb5', command = smaller,
                               height = 2, width = 7)
    smaller_button.grid(row = 1, column = 1, sticky = 'NSEW')

    clear_button = tk.Button(window, text = 'CLEAR', font=font_size,
                             fg = 'black', bg = '#a8ddb5', command = clear,
                             height = 2, width = 7)
    clear_button.grid(row = 1, column = 2, sticky = 'NSEW')

    back_button = tk.Button(window, text = 'BACK', font=font_size,
                            fg = 'black', bg = '#a8ddb5',
                            command = back, height = 2, width = 7)
    back_button.grid(row = 1, column = 3, sticky = 'NSEW')

    button1 = tk.Button(window, text = '1', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(1),
                        height = 2, width = 7)
    button1.grid(row = 4, column = 0, sticky = 'NSEW')
    
    button2 = tk.Button(window, text = '2', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(2),
                        height = 2, width = 7)
    button2.grid(row = 4, column = 1, sticky = 'NSEW')
    
    button3 = tk.Button(window, text = '3', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(3),
                        height = 2, width = 7)
    button3.grid(row = 4, column = 2, sticky = 'NSEW')
    
    button4 = tk.Button(window, text = '4', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(4),
                        height = 2, width = 7)
    button4.grid(row = 3, column = 0, sticky = 'NSEW')
    
    button5 = tk.Button(window, text = '5', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(5),
                        height = 2, width = 7)
    button5.grid(row = 3, column = 1, sticky = 'NSEW')
    
    button6 = tk.Button(window, text = '6', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(6),
                        height = 2, width = 7)
    button6.grid(row = 3, column = 2, sticky = 'NSEW')
    
    button7 = tk.Button(window, text = '7', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(7),
                        height = 2, width = 7)
    button7.grid(row = 2, column = 0, sticky = 'NSEW')
    
    button8 = tk.Button(window, text = '8', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(8),
                        height = 2, width = 7)
    button8.grid(row = 2, column = 1, sticky = 'NSEW')
    
    button9 = tk.Button(window, text = '9', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(9),
                        height = 2, width = 7)
    button9.grid(row = 2, column = 2, sticky = 'NSEW')
    
    button0 = tk.Button(window, text = '0', font=font_size, fg = 'black',
                        bg = '#a8ddb5', command = lambda: button(0),
                        height = 2, width = 7)
    button0.grid(row = 5, column = 0, sticky = 'NSEW')

    plus = tk.Button(window, text = " + ", font=font_size, fg = 'black',
                     bg = '#a8ddb5', command = lambda: button('+'), height = 2,
                     width = 7)
    plus.grid(row = 2, column = 3, sticky = 'NSEW')

    minus = tk.Button(window, text = " - ", font=font_size, fg = 'black',
                      bg = '#a8ddb5', command = lambda: button('-'),
                      height = 2, width = 7)
    minus.grid(row = 3, column = 3, sticky = 'NSEW')

    multiply = tk.Button(window, text = " x ", font=font_size, fg = 'black',
                         bg = '#a8ddb5', command = lambda: button('*'),
                         height = 2, width = 7)
    multiply.grid(row = 4, column = 3, sticky = 'NSEW')

    divide = tk.Button(window, text = " / ", font=font_size, fg = 'black',
                       bg = '#a8ddb5', command = lambda: button('/'),
                       height = 2, width = 7)
    divide.grid(row = 5, column = 3, sticky = 'NSEW')

    sqrt_button = tk.Button(window, text = "SQRT", font=font_size,
                            fg = 'black', bg = '#a8ddb5', command = sqrt,
                            height = 2, width = 7)
    sqrt_button.grid(row = 5, column = 1, sticky = 'NSEW')

    equal_button = tk.Button(window, text = " = ", font=font_size,
                             fg = 'black', bg = '#a8ddb5', command = equal,
                             height = 2, width = 7)
    equal_button.grid(row = 5, column = 2, sticky = 'NSEW')
    
    for i in range(4):
        window.columnconfigure(i, weight = 1)

    for i in range(6):
        window.rowconfigure(i, weight = 1)
     
    window.mainloop()
