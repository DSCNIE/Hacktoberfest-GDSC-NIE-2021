from tkinter import *
import tkinter as tk

WHITE = "#F8F8F8" # white for nunbers
Red = "#47191b" # browinsh-Red

var = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

root = tk.Tk()
root.title('Calculator')
root.iconbitmap("images\calculator1.ico")
root.config(bg='#272533')

display_text = tk.StringVar()
display_text.set('0.0000')

canvas = tk.Canvas(bg='#272533', bd=0, highlightthickness=0)
canvas.pack(padx=15, pady=15)

def std_btn(text, bg, row, col, width=6, height=2, font=('Bold', 24)):
    btn = tk.Button(canvas, text=text, bg=bg, width=width, height=height, font=font, command=lambda: event_click(text))
    return btn.grid(row=row, column=col, padx=4, pady=4)

tk.Label(canvas, textvariable=display_text, anchor='e', bg='black', fg='red', font=('Digital-7',47)).grid(row=1, columnspan=4, sticky='ew', padx=4, pady=2)
std_btn("C", Red, 2, 0),   std_btn("CE", Red, 2, 1),  std_btn("%", Red, 2, 2),   std_btn("/", Red, 2, 3)
std_btn("7", WHITE, 3, 0), std_btn("8", WHITE, 3, 1), std_btn("9", WHITE, 3, 2), std_btn("*", Red, 3, 3)
std_btn("4", WHITE, 4, 0), std_btn("5", WHITE, 4, 1), std_btn("6", WHITE, 4, 2), std_btn("-", Red, 4, 3)
std_btn("1", WHITE, 5, 0), std_btn("2", WHITE, 5, 1), std_btn("3", WHITE, 5, 2), std_btn("+", Red, 5, 3)
std_btn("0", WHITE, 6, 0), std_btn(".", WHITE, 6, 1)

rtn_btn = tk.Button(canvas, text='=', bg='#ECA527', width=15, height=2, font=('bold', 24), command=lambda: event_click("="))
rtn_btn.focus()
rtn_btn.grid(row=6, column=2, columnspan=2, padx=4, pady=4)

# calculator functions
def event_click(operation):
    global var
    if operation in ['CE','C']:
        clear_click()
        update_display(0.0)
        var['operator'] = ''
        var['result'] = 0.0
    if operation in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(operation)
    if operation in ['*','/','+','-']:
        operator_click(operation)
    if operation == '.':
        var['decimal'] = True 
    if operation == '%':
        update_display(var['result'] / 100.0)
    if operation == '=':
        calculate_click()

# helper functions
def update_display(display_value):
    global display_text
    try: # to display floating point numbers
        display_text.set('{:,.4f}'.format(display_value))
    except: # to display the error messages
        display_text.set(display_value)

def format_number():
    return ''.join(var['front']) + '.' + ''.join(var['back'])

# onclick events
def number_click(operation):
    global var
    if var['decimal']:
        var['back'].append(operation)
    else:
        var['front'].append(operation)

    display_value = float(format_number())
    update_display(display_value)

def clear_click():
    # to reset the calculator to 0.000
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False

def operator_click(operation):
    # on click operations
    global var
    var['operator'] = operation
    try: # if no x_val exists, use prior result
        var['x_val'] = float(format_number())
    except:
        var['x_val'] = var['result']
    clear_click()

def calculate_click():
    # perform operation on the variables x and y 
    global var
    # check for x value
    if not var['x_val']:
        return 
    try: # check for y value
        var['y_val'] = float(format_number())
    except:
        var['y_val'] = 0.0
    try: # check for division by zero error
        var['result'] = float(eval(str(var['x_val']) + var['operator'] + str(var['y_val'])))
        update_display(var['result'])
    except ZeroDivisionError: 
        error = "ERROR! DIV/0"
        var['x_val'] = 0.0
        clear_click()
        update_display(error)

    clear_click()

root.mainloop()
