import tkinter as tk
window = tk.Tk()
window.title("Calculator ")
window.geometry("900x600")
window.configure(bg = "light grey")

entry_var = tk.StringVar()
entry = tk.Entry(window , textvariable= entry_var ,font = ("ariel" , 20 , "bold"),fg = "black",bg="white")
entry.grid(row = 0 , column = 0 , pady = 20 , columnspan = 4)

expression = ""
def on_button_click(value):
    global expression
    expression += str(value)
    entry_var.set(expression)
def evaluate():
    global expression
    result = str(eval(expression))
    entry_var.set(result)
    expression = result 
def clears():
    global expression
    expression = "" 
    entry_var.set("")
def delete():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)
def negative():
    global expression
    expression = str(-float(expression))
    entry_var.set(expression)

button = tk.Button(window , text = "7" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda: on_button_click("7"))
button.grid(row = 5 , column = 0)

button2 = tk.Button(window , text = "8" , font = ("ariel", 20 , "bold") ,width = 3 , height = 2, fg = "black" ,bg = "white", command = lambda: on_button_click("8"))
button2.grid(row = 5 , column = 1)

button3 = tk.Button(window , text = "9" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda : on_button_click("9"))
button3.grid(row = 5 , column = 2)

button4 = tk.Button(window , text = "4" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda : on_button_click("4"))
button4.grid(row = 6 , column = 0)

button5 = tk.Button(window , text = "5" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda :  on_button_click("5"))
button5.grid(row = 6 , column = 1)

button6 = tk.Button(window , text = "6" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda : on_button_click("6"))
button6.grid(row = 6 , column = 2)

button7 = tk.Button(window, text = "1" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda : on_button_click("1"))
button7.grid(row = 7 , column = 0)

button8 = tk.Button(window, text = "2" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda : on_button_click("2"))
button8.grid(row = 7 , column = 1)

button9 = tk.Button(window , text = "3" , font = ("ariel" , 20 , "bold") ,width = 3 , height = 2, fg = "black",bg = "white", command = lambda : on_button_click("3"))
button9.grid(row = 7 , column = 2)

button10 = tk.Button(window , text = "+" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg = "green", command = lambda : on_button_click("+"))
button10.grid(row = 7 , column = 3)

button11 = tk.Button(window , text = "-" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg = "green",  command = lambda : on_button_click ("-"))
button11.grid(row = 6 , column = 3)

button12 = tk.Button(window , text = "×" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg = "green",  command = lambda : on_button_click ("*"))
button12.grid(row = 5 , column = 3)

button13 = tk.Button(window , text = "÷" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg = "green",  command = lambda : on_button_click ("/"))
button13.grid(row = 4 , column = 3)

button14 = tk.Button(window , text = "=" , font = ("ariel" , 20 , "bold"),width = 4 , height = 2 , fg = "black",bg ="yellow", command = evaluate)
button14.grid(row = 8 , column = 3)

button17 = tk.Button(window , text = "%" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg = "red",  command = lambda : on_button_click ("%"))
button17.grid(row = 8, column = 0)

button20 = tk.Button(window , text = "0" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "black",bg = "white" , command = lambda : on_button_click ("0"))
button20.grid(row = 8, column = 1)

button18 = tk.Button(window , text = "." , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white", bg = "red" ,  command = lambda : on_button_click ("."))
button18.grid(row = 8, column = 2)

button19 = tk.Button(window , text = "+/-" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2,  fg = "white",bg = "red",  command = lambda: negative())
button19.grid(row = 4, column = 2)

button15 = tk.Button(window , text = "AC" , font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg="red", command = lambda: clears())
button15.grid(row = 4 , column = 0)

button16 = tk.Button(window, text = "⌫", font = ("ariel" , 20 , "bold") ,width = 4 , height = 2, fg = "white",bg = "red", command = lambda: delete())
button16.grid(row = 4 , column = 1)

window.mainloop()
