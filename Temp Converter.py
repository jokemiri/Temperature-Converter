from tkinter import *
import tkinter.ttk as ttk

#Window Properties
root=Tk()
root.geometry("900x510")
root.resizable(False, False)
root.title("Temperature Converter")
root.configure(background='#154c79')


#main window icon
main_window_icon = PhotoImage(file='icon.png')
root.iconphoto(False, main_window_icon)

primary_color = '#063970'
primary_bt = '#76b5c5'
secondary_color = '#0c1214'
secondary_bt = '#C5768f'

def getFont(size=9, bold=False):
    return('Raleway', size, 'bold' if bold else 'normal')

def validate(P):
    empty = P == ""
    digit = empty or P[-1].isdigit()
    minus =P=="-" and len(P)==1
    decimal = P.count(".")==1
    output = empty or digit or minus or decimal
    return output

calculateFunction = {
    "cf": lambda T: T*9/5+32,
    "ck": lambda T: T+273.15,
    "fc": lambda T:(T-32)*5/9,
    "kc": lambda T: T-273.15
    
    
}

calculateFunction["fk"] = lambda T: calculateFunction["ck"](calculateFunction["fc"](T))
calculateFunction["kf"] = lambda T: calculateFunction["cf"](calculateFunction["kc"](T))

def convert(input_entry, fromUnit, toUnit, resultVar):
    fromUnitVar = fromUnit.get().lower()
    toUnitVar = toUnit.get()[0].lower()

    try:
        value = float(input_entry.get())
    except ValueError:
        resultVar.set('Error!')
        return
    
    if fromUnitVar == toUnitVar:
        res = value
    else:
        res = calculateFunction[fromUnitVar + toUnitVar](value)

    if not toUnitVar == 'K':
        resultVar.set(f'{res:.2f}°{toUnitVar.upper()}')
    else:
        resultVar.set(f'{res:.2f}{toUnitVar.upper()}')

reg = root.register(validate)

borderFrame = Frame(root, bg=secondary_color, width=450, height=510)
borderFrame.place(x=0, y=0)

left_frame = Frame(borderFrame, bg=primary_color, width=440, height=500)
left_frame.place(x=5, y=5)

enter_label = Label(left_frame, text='Enter Temperature', bg=primary_color, fg=primary_bt, font=getFont(16, True))
enter_label.place(x=30, y=50)

degree_label = Label(left_frame, text='Temperature', bg=primary_color, fg=primary_bt, font=getFont(9))
degree_label.place(x=30, y=120)

input_entry = Entry(left_frame, bg=primary_bt, fg=secondary_color, insertbackground='white', borderwidth=5, relief='flat', validatecommand=(reg, '%P'), validate='key')
input_entry.place(x=30, y=160, width=265, height=42)

unitVar = StringVar(root)
unitVar.set('C')

convertVar = StringVar(root)
convertVar.set('Farenheit')

styles = ttk.Style()
styles.configure('unit.TMenubutton', background=primary_bt) # font=getFont(9, True),
styles.configure('unit.TMenubutton', relief = 'flat')

styles.configure('convert.TMenubutton', relief='flat') #font=getFont(9, True)
styles.configure('convert.TMenubutton', backgroung=primary_bt)
styles.configure('convert.TMenubutton', foreground=secondary_color)
styles.configure('convert.TMenubutton', width=320)

unitMenu = ttk.OptionMenu(left_frame, unitVar, "C", "C", "F", "K", style='unit.TMenubutton')
unitMenu.place(x=300, y=160, width=50, height=42)

convert_label = Label(left_frame, text='Convert', bg=primary_color, fg=primary_bt, font=getFont(9))
convert_label.place(x=30, y=280)

convert_menu = ttk.OptionMenu(left_frame, convertVar, 'Farenheit', 'Celcius', 'Farenheit', 'Kelvin', style='convert.TMenubutton')
convert_menu.place(x=30, y=320, width=320, height=42)

convert_button = Button(left_frame, text='Convert', bg=secondary_color, fg=primary_bt, font=getFont(12), relief='flat', activebackground=secondary_bt, bd=0,)
convert_button.place(x=150, y=420, width=140, height=40)

right_frame = Frame(root, bg=secondary_color, width=450, height=510)
right_frame.place(x=450, y=0)

resultVar = StringVar(root)
resultVar.set("")

result_label = Label(right_frame, textvariable=resultVar, bg=secondary_color, fg=primary_color, font=getFont(32, True))
result_label.place(relx=0.5, rely=0.4901, anchor=CENTER)

convert_button.configure(command=lambda: convert(input_entry, unitVar, convertVar, resultVar))

#main window logo
photo=PhotoImage(file="logo.png")
myimage=Label(root, image=photo,background=secondary_color)
myimage.place(x=760, y=5)


root.mainloop()