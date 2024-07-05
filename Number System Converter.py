from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import time


root1 = Tk()
root1.title('')
width = 350
height = 120


def root(width, height):
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    root1.geometry(f'{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}')


root(width, height)


def start():
    try:
        progress_bar = ttk.Progressbar(root1, orient='horizontal', length=300, mode='determinate', maximum=100)
        progress_bar.place(x=24, y=50)
        label1 = Label(root1, bg="#008B8B", fg='white')
        font1 = Font(family="Comic SAns MS", size=10, slant='italic', weight='bold')
        label1.configure(font=font1)
        label1.place(x=128, y=22)
        for value in range(102):
            label1.config(text=f'Loading {round(progress_bar["value"])}%')
            progress_bar['value'] += 1
            root1.update_idletasks()
            time.sleep(0.00005)                       # change this later to 0.05
            if progress_bar['value'] == 101:
                progress_bar.stop()
                root1.destroy()
                time.sleep(1)
                main_window()
    except TclError:
        pass


canvas1 = Canvas(root1, bg='white')
canvas1.create_polygon(0, 0, 30, 30, 0, 60, fill='#79CDCD')
canvas1.create_polygon(0, 0, 30, 0, 30, 30, fill='#9ACD32')  # light green
canvas1.create_polygon(30, 30, 60, 0, 60, 60, fill='#79CDCD')
canvas1.create_polygon(30, 30, 60, 60, 30, 90, fill='#9ACD32')
canvas1.create_polygon(60, 0, 90, 0, 90, 30, fill='#9ACD32')
canvas1.create_polygon(90, 0, 120, 0, 90, 30, fill='#79CDCD')
canvas1.create_polygon(60, 0, 90, 30, 60, 60, fill='#9ACD32')
canvas1.create_polygon(60, 60, 90, 30, 90, 90, fill='#9ACD32')
canvas1.create_polygon(30, 0, 30, 30, 60, 0, fill='#6B8E23')
canvas1.create_polygon(30, 30, 0, 60, 30, 90, fill='#388E8E')
canvas1.create_polygon(0, 60, 0, 120, 30, 90, fill='#9ACD32')
canvas1.create_polygon(60, 60, 30, 90, 60, 120, fill='#79CDCD')
canvas1.create_polygon(30, 90, 0, 120, 30, 120, fill='#9ACD32')
canvas1.create_polygon(30, 90, 30, 120, 60, 120, fill='#388E8E')  # dark blue
canvas1.create_polygon(60, 60, 60, 120, 90, 90, fill='#6B8E23')
canvas1.create_polygon(120, 0, 90, 30, 120, 60, fill='#388E8E')
canvas1.create_polygon(90, 30, 120, 60, 90, 90, fill='#79CDCD')
canvas1.create_polygon(120, 0, 150, 0, 150, 30, fill='#9ACD32')
canvas1.create_polygon(150, 0, 180, 0, 150, 30, fill='#79CDCD')
canvas1.create_polygon(120, 0, 150, 30, 120, 60, fill='#6B8E23')
canvas1.create_polygon(150, 30, 120, 60, 150, 90, fill='#9ACD32')
canvas1.create_polygon(120, 60, 90, 90, 120, 120, fill='#9ACD32')
canvas1.create_polygon(180, 0, 210, 0, 210, 30, fill='#9ACD32')
canvas1.create_polygon(210, 0, 240, 0, 210, 30, fill='#6B8E23')
canvas1.create_polygon(240, 0, 270, 0, 270, 30, fill='#79CDCD')
canvas1.create_polygon(270, 0, 300, 0, 270, 30, fill='#388E8E')
canvas1.create_line(90, 90, 30, 30, width=2, fill='white')
canvas1.create_line(150, 30, 90, 90, width=2, fill='white')
canvas1.create_line(60, 0, 30, 30, width=2, fill='white')
canvas1.create_line(120, 0, 150, 30, width=2, fill='white')
canvas1.pack()

button1 = Button(root1, text='Open App', relief='flat', command=start, bg='#008B8B', fg='white')
font2 = Font(family='Comic Sans MS', size=10, weight='normal')
button1.configure(font=font2)
button1.place(x=136, y=80)


def on_entry_click1(event):
    if entry1.get() == 'Enter a Decimal Value':             # When the entry is clicked, the text gets removed
        entry1.delete(0, "end")                             # from the entry and it gets blanked for the user to enter
        entry1.insert(0, '')                                # an input
        entry1.config(fg='white')


def on_focusout1(event):                                    # When the click is removed from the entry,
    if entry1.get() == '':                                  # and if it is blank, the text is set to default
        entry1.insert(0, 'Enter a Decimal Value')


def on_entry_click2(event):
    if entry1_.get() == 'Enter a Decimal Value':             # When the entry is clicked, the text gets removed
        entry1_.delete(0, "end")                             # from the entry and it gets blanked for the user to enter
        entry1_.insert(0, '')                                # an input
        entry1_.config(fg='white')


def on_focusout2(event):                                    # When the click is removed from the entry,
    if entry1_.get() == '':                                  # and if it is blank, the text is set to default
        entry1_.insert(0, 'Enter a Decimal Value')


def on_entry_click3(event):
    if entry1__.get() == 'Enter a Decimal Value':             # When the entry is clicked, the text gets removed
        entry1__.delete(0, "end")                             # from the entry and it gets blanked for the user to enter
        entry1__.insert(0, '')                                # an input
        entry1__.config(fg='white')


def on_focusout3(event):                                    # When the click is removed from the entry,
    if entry1__.get() == '':                                  # and if it is blank, the text is set to default
        entry1__.insert(0, 'Enter a Decimal Value')


def on_entry_click4(event):
    if entry1___.get() == 'Enter a Decimal Value':             # When the entry is clicked, the text gets removed
        entry1___.delete(0, "end")                             # from the entry and it gets blanked for the user to enter
        entry1___.insert(0, '')                                # an input
        entry1___.config(fg='white')


def on_focusout4(event):                                    # When the click is removed from the entry,
    if entry1___.get() == '':                                  # and if it is blank, the text is set to default
        entry1___.insert(0, 'Enter a Decimal Value')


def destroy():               # This function checks for the existings labels to destroy/remove them,
    try:                     # otherwise the funtion just passes on to next work-out
        v.destroy()
    except NameError:
        pass
    try:
        x.destroy()
    except NameError:
        pass
    try:
        y.destroy()
    except NameError:
        pass
    try:
        z.destroy()
    except NameError:
        pass


def destroy_():               # This function checks for the existings labels to destroy/remove them,
    try:                     # otherwise the funtion just passes on to next work-out
        v_.destroy()
    except NameError:
        pass
    try:
        x_.destroy()
    except NameError:
        pass
    try:
        y_.destroy()
    except NameError:
        pass
    try:
        z_.destroy()
    except NameError:
        pass


def destroy__():               # This function checks for the existings labels to destroy/remove them,
    try:                     # otherwise the funtion just passes on to next work-out
        v__.destroy()
    except NameError:
        pass
    try:
        x__.destroy()
    except NameError:
        pass
    try:
        y__.destroy()
    except NameError:
        pass
    try:
        z__.destroy()
    except NameError:
        pass


def destroy___():               # This function checks for the existings labels to destroy/remove them,
    try:                     # otherwise the funtion just passes on to next work-out
        v___.destroy()
    except NameError:
        pass
    try:
        x___.destroy()
    except NameError:
        pass
    try:
        y___.destroy()
    except NameError:
        pass
    try:
        z___.destroy()
    except NameError:
        pass


def reset1():
    try:
        if not entry1.get() == 'Enter a Decimal Value':
            entry1.delete(0, 'end')                                  # When the Reset button is pressed this function is
            entry1.insert(0, 'Enter a Decimal Value')                # called out
        entry2.delete(0, 'end')
        if not entry2.get() == 'Result will be shown here':          # This function resets the window as it was in the
            entry2.delete(0, 'end')                                  # starting by removing label, setting entries' text
            entry2.insert(0, 'Result will be shown here')            # to default ( as before )
        destroy()
    except NameError:
        pass


def reset2():
    try:
        if not entry1_.get() == 'Enter a Decimal Value':
            entry1_.delete(0, 'end')                                # When the Reset button is pressed this function is
            entry1_.insert(0, 'Enter a Decimal Value')              # called out
        entry2_.delete(0, 'end')
        if not entry2_.get() == 'Result will be shown here':        # This function resets the window as it was in the
            entry2_.delete(0, 'end')                                # starting by removing label, setting entries' text
            entry2_.insert(0, 'Result will be shown here')          # to default ( as before )
        destroy_()
    except NameError:
        pass


def reset3():
    try:
        if not entry1__.get() == 'Enter a Decimal Value':
            entry1__.delete(0, 'end')                                # When the Reset button is pressed this function is
            entry1__.insert(0, 'Enter a Decimal Value')              # called out
        entry2__.delete(0, 'end')
        if not entry2__.get() == 'Result will be shown here':        # This function resets the window as it was in the
            entry2__.delete(0, 'end')                                # starting by removing label, setting entries' text
            entry2__.insert(0, 'Result will be shown here')          # to default ( as before )
        destroy__()
    except NameError:
        pass


def reset4():
    try:
        if not entry1___.get() == 'Enter a Decimal Value':
            entry1___.delete(0, 'end')                               # When the Reset button is pressed this function is
            entry1___.insert(0, 'Enter a Decimal Value')             # called out
        entry2___.delete(0, 'end')
        if not entry2___.get() == 'Result will be shown here':      # This function resets the window as it was in the
            entry2___.delete(0, 'end')                              # starting by removing label, setting entries' text
            entry2___.insert(0, 'Result will be shown here')        # to default ( as before )
        destroy___()
    except NameError:
        pass


def destroy_label():
    try:
        label3.destroy()
        label4.destroy()
        label5.destroy()
        label6.destroy()
    except NameError:
        pass


# noinspection PyGlobalUndefined
def binary():
    global label3
    destroy_label()
    label3 = Label(root2, text='Binary Value----->', font=('Comic Sans MS', 18), fg='#0198E1', bg='white')
    label3.place(x=180, y=378)

    global entry1_
    entry1_ = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry1_.configure(font=('-family', 'Comic Sans MS'))
    entry1_.insert(0, 'Enter a Decimal Value')
    entry1_.bind('<FocusIn>', on_entry_click2)
    entry1_.bind('<FocusOut>', on_focusout2)
    entry1_.place(x=420, y=380, height=40)

    global entry2_
    entry2_ = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry2_.configure(font=('-family', 'Comic Sans MS'))
    entry2_.insert(0, 'Result will be shown here')  # This is the second entry where the results are displayed
    entry2_.place(x=420, y=600, height=40)

    try:
        canvas2.create_text(145, 523, text="Binary", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(470, 523, text="Octal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(812, 523, text="Decimal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(1154, 523, text="Hexa-Decimal", font=("Comic Sans MS", 15), fill='black')
        button6_ = Button(root2, padx=9, bg="#009dff", command=bin_to_bin)
        button6_.place(x=80, y=511)
        button7_ = Button(root2, padx=9, bg="#009dff", command=bin_to_oct)
        button7_.place(x=410, y=511)
        button8_ = Button(root2, padx=9, bg="#009dff", command=bin_to_dec)
        button8_.place(x=740, y=511)
        button9_ = Button(root2, padx=9, bg="#009dff", command=bin_to_hex)
        button9_.place(x=1050, y=511)
        button10_ = Button(root2, text='Reset Value', padx=16, pady=2, bg='#009dff', fg='white', relief='raised',
                          font=('Comic Sans MS', 10), command=reset2)
        button10_.place(x=140, y=600)
    except TypeError:
        pass


def bin_to_bin():
    value1_ = entry1_.get()
    return bin_to_bin_1(value1_)


# noinspection PyGlobalUndefined
def bin_to_bin_1(w):
    destroy_()
    global v_  # here the global function is defined so that the assigned variables can be
    global x_  # used in different functions ( i.e. out of the scope of this function )
    global y_
    global z_
    global g_
    if str(w) == 'Enter a Decimal Value':
        if not entry2_.get() == 'Result will be shown here':
            entry2_.delete(0, 'end')
            entry2_.insert(0, 'Result will be shown here')
        labelu_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                        fg='grey', font=('bold', 12), bg='white')
        labelu_.place(x=940, y=387)
        v_ = labelu_
    else:
        if len(str(w)) < 1:
            if not entry2_.get() == 'Result will be shown here':
                entry2_.delete(0, 'end')
                entry2_.insert(0, 'Result will be shown here')
            labelv_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                            fg='grey', font=('bold', 12), bg='white')
            labelv_.place(x=940, y=387)
            x_ = labelv_
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if not '.' in str(w):
                    nor = bin(int(w, 2)).lstrip('0b')
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, nor)
                if '.' in str(w):
                    whole, decimal = str(w).split('.')
                    whole = str(bin(int(whole, 2))).lstrip('0b') + '.'
                    decimal = str(bin(int(decimal, 2))).lstrip('0b')
                    result = whole + decimal
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, result)
            except ValueError:
                if not entry2_.get() == 'Result will be shown here':     # If the user enters an invalid value, an error
                    entry2_.delete(0, 'end')                             # message will be displayed
                    entry2_.insert(0, 'Result will be shown here')
                labely_ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely_.place(x=940, y=387)
                y_ = labely_
        else:
            labelz_ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                            fg='grey', bg='white', font=('bold', 12))
            labelz_.place(x=940, y=387)
            z_ = labelz_


def bin_to_oct():
    value1 = entry1_.get()
    return bin_to_oct_1(value1)


def bin_to_oct_1(w):
    destroy_()
    global v_  # here the global function is defined so that the assigned variables can be
    global x_  # used in different functions ( i.e. out of the scope of this function )
    global y_
    global z_
    global g_
    if str(w) == 'Enter a Decimal Value':
        if not entry2_.get() == 'Result will be shown here':
            entry2_.delete(0, 'end')
            entry2_.insert(0, 'Result will be shown here')
        labelu_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                        fg='grey', font=('bold', 12), bg='white')
        labelu_.place(x=940, y=387)
        v_ = labelu_
    else:
        if len(str(w)) < 1:
            if not entry2_.get() == 'Result will be shown here':
                entry2_.delete(0, 'end')
                entry2_.insert(0, 'Result will be shown here')
            labelv_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                           fg='grey', font=('bold', 12), bg='white')
            labelv_.place(x=940, y=387)
            x_ = labelv_
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if float.is_integer(float(w)):
                    _l_ = oct(int(w, 2)).lstrip('0o')  # check if the user input value is float or integer
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, _l_)
                elif not float.is_integer(float(w)):
                    l = len(w)
                    t = -1
                    if '.' in w:
                        t = w.index('.')
                        len_left = t
                    else:
                        len_left = l
                    for i in range(1, (3 - len_left % 3) % 3 + 1):
                        w = '0' + w
                    if t != -1:
                        len_right = l - len_left - 1
                        for i in range(1, (3 - len_right % 3) % 3 + 1):
                            w = w + '0'
                    bin_oct_map = {}
                    createMap1(bin_oct_map)
                    i = 0
                    octal = ""
                    while True:
                        octal += bin_oct_map[w[i:i + 3]]
                        i += 3
                        if i == len(w):
                            break
                        if w[i] == '.':
                            octal += '.'
                            i += 1
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, octal)
            except (ValueError, KeyError):
                if not entry2_.get() == 'Result will be shown here':     # If the user enters an invalid value, an error
                    entry2_.delete(0, 'end')                             # message will be displayed
                    entry2_.insert(0, 'Result will be shown here')
                labely_ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely_.place(x=940, y=387)
                y_ = labely_
        else:
            labelz_ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                           fg='grey', bg='white', font=('bold', 12))
            labelz_.place(x=940, y=387)
            z_ = labelz_


def createMap1(bin_oct_map):
    bin_oct_map["000"] = '0'
    bin_oct_map["001"] = '1'
    bin_oct_map["010"] = '2'
    bin_oct_map["011"] = '3'
    bin_oct_map["100"] = '4'
    bin_oct_map["101"] = '5'
    bin_oct_map["110"] = '6'
    bin_oct_map["111"] = '7'


def bin_to_dec():
    value = entry1_.get()
    return bin_to_dec_1(value, len(str(value)))


def bin_to_dec_1(binary, length):
    destroy_()
    global v_  # here the global function is defined so that the assigned variables can be
    global x_  # used in different functions ( i.e. out of the scope of this function )
    global y_
    global z_
    global g_
    if str(binary) == 'Enter a Decimal Value':
        if not entry2_.get() == 'Result will be shown here':
            entry2_.delete(0, 'end')
            entry2_.insert(0, 'Result will be shown here')
        labelu_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                        fg='grey', font=('bold', 12), bg='white')
        labelu_.place(x=940, y=387)
        v_ = labelu_
    else:
        if len(str(binary)) < 1:
            if not entry2_.get() == 'Result will be shown here':
                entry2_.delete(0, 'end')
                entry2_.insert(0, 'Result will be shown here')
            labelv_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                            fg='grey', font=('bold', 12), bg='white')
            labelv_.place(x=940, y=387)
            x_ = labelv_
        elif (len(str(binary)) >= 1) and (len(str(binary)) <= 15):
            try:
                if float.is_integer(float(binary)):
                    binary = int(binary, 2)
                    decimal, i, n = 0, 0, 0
                    while binary != 0:
                        dec = binary % 10
                        decimal = decimal + dec * pow(2, i)
                        binary = binary // 10
                        i += 1
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, decimal)
                elif not float.is_integer(float(binary)):
                    # limit the user input to binary values only
                    point = binary.find('.')
                    if point == -1:
                        point = length
                    intDecimal = 0
                    fracDecimal = 0
                    twos = 1
                    for i in range(point - 1, -1, -1):
                        intDecimal += ((ord(binary[i]) - ord('0')) * twos)
                        twos *= 2
                    twos = 2
                    for i in range(point + 1, length):
                        fracDecimal += ((ord(binary[i]) - ord('0')) / twos)
                        twos *= 2.0
                    ans = intDecimal + fracDecimal
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, ans)
            except ValueError:
                if not entry2_.get() == 'Result will be shown here':     # If the user enters an invalid value, an error
                    entry2_.delete(0, 'end')                             # message will be displayed
                    entry2_.insert(0, 'Result will be shown here')
                labely_ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely_.place(x=940, y=387)
                y_ = labely_
        else:
            labelz_ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                           fg='grey', bg='white', font=('bold', 12))
            labelz_.place(x=940, y=387)
            z_ = labelz_


def bin_to_hex():
    value = entry1_.get()
    return bin_to_hex_1(value)


def bin_to_hex_1(w):
    destroy_()
    global v_  # here the global function is defined so that the assigned variables can be
    global x_  # used in different functions ( i.e. out of the scope of this function )
    global y_
    global z_
    global g_
    if str(w) == 'Enter a Decimal Value':
        if not entry2_.get() == 'Result will be shown here':
            entry2_.delete(0, 'end')
            entry2_.insert(0, 'Result will be shown here')
        labelu_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                        fg='grey', font=('bold', 12), bg='white')
        labelu_.place(x=940, y=387)
        v_ = labelu_
    else:
        if len(str(w)) < 1:
            if not entry2_.get() == 'Result will be shown here':
                entry2_.delete(0, 'end')
                entry2_.insert(0, 'Result will be shown here')
            labelv_ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                            fg='grey', font=('bold', 12), bg='white')
            labelv_.place(x=940, y=387)
            x_ = labelv_
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if float.is_integer(float(w)):
                    hex_value = hex(int(w, 2)).lstrip('0x')
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, hex_value)
                elif not float.is_integer(float(w)):
                    l = len(w)
                    t = -1
                    if '.' in w:
                        t = w.index('.')
                        len_left = t
                    else:
                        len_left = l
                    for i in range(1, (4 - len_left % 4) % 4 + 1):
                        w = '0' + w
                    if t != -1:
                        len_right = l - len_left - 1
                        for i in range(1, (4 - len_right % 4) % 4 + 1):
                            w = w + '0'
                    bin_hexa = {}
                    createMap2(bin_hexa)
                    i = 0
                    hexa = ""
                    while True:
                        hexa += bin_hexa[w[i:i + 4]]
                        i += 4
                        if i == len(w):
                            break
                        if w[i] == '.':
                            hexa += '.'
                            i += 1
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, hexa)
            except (ValueError, KeyError):
                if not entry2_.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2_.delete(0, 'end')
                    entry2_.insert(0, 'Result will be shown here')
                labely_ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely_.place(x=940, y=387)
                y_ = labely_
        else:
            labelz_ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                            fg='grey', bg='white', font=('bold', 12))
            labelz_.place(x=940, y=387)
            z_ = labelz_


def createMap2(bin_hexa):
    bin_hexa['0000'] = '0'
    bin_hexa['0001'] = '1'
    bin_hexa['0010'] = '2'
    bin_hexa['0011'] = '3'
    bin_hexa['0100'] = '4'
    bin_hexa['0101'] = '5'
    bin_hexa['0110'] = '6'
    bin_hexa['0111'] = '7'
    bin_hexa['1000'] = '8'
    bin_hexa['1001'] = '9'
    bin_hexa['1010'] = 'A'
    bin_hexa['1011'] = 'B'
    bin_hexa['1100'] = 'C'
    bin_hexa['1101'] = 'D'
    bin_hexa['1110'] = 'E'
    bin_hexa['1111'] = 'F'


def octal():
    global label5
    destroy_label()
    label5 = Label(root2, text='Octal Value----->', font=('Comic Sans MS', 18), fg='#0198E1', bg='white')
    label5.place(x=180, y=378)

    global entry1__
    entry1__ = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry1__.configure(font=('-family', 'Comic Sans MS'))
    entry1__.insert(0, 'Enter a Decimal Value')
    entry1__.bind('<FocusIn>', on_entry_click3)
    entry1__.bind('<FocusOut>', on_focusout3)
    entry1__.place(x=420, y=380, height=40)

    global entry2__
    entry2__ = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry2__.configure(font=('-family', 'Comic Sans MS'))
    entry2__.insert(0, 'Result will be shown here')  # This is the second entry where the results are displayed
    entry2__.place(x=420, y=600, height=40)

    try:
        canvas2.create_text(145, 523, text="Binary", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(470, 523, text="Octal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(812, 523, text="Decimal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(1154, 523, text="Hexa-Decimal", font=("Comic Sans MS", 15), fill='black')
        button6 = Button(root2, padx=9, bg="#009dff", command=oct_to_bin)
        button6.place(x=80, y=511)
        button7 = Button(root2, padx=9, bg="#009dff", command=oct_to_oct)
        button7.place(x=410, y=511)
        button8 = Button(root2, padx=9, bg="#009dff", command=oct_to_dec)
        button8.place(x=740, y=511)
        button9 = Button(root2, padx=9, bg="#009dff", command=oct_to_hex)
        button9.place(x=1050, y=511)
        button10 = Button(root2, text='Reset Value', padx=16, pady=2, bg='#009dff', fg='white', relief='raised',
                          font=('Comic Sans MS', 10), command=reset3)
        button10.place(x=140, y=600)
    except TypeError:
        pass


def oct_to_bin():
    value = entry1__.get()
    return oct_to_bin_1(value)


# noinspection PyTypeChecker,PyGlobalUndefined
def oct_to_bin_1(w):
    destroy__()
    global v__  # here the global function is defined so that the assigned variables can be
    global x__  # used in different functions ( i.e. out of the scope of this function )
    global y__
    global z__
    global g__
    if str(w) == 'Enter a Decimal Value':
        if not entry2__.get() == 'Result will be shown here':
            entry2__.delete(0, 'end')
            entry2__.insert(0, 'Result will be shown here')
        labelu__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                        fg='grey', font=('bold', 12), bg='white')
        labelu__.place(x=940, y=387)
        v__ = labelu__
    else:
        if len(str(w)) < 1:
            if not entry2__.get() == 'Result will be shown here':
                entry2__.delete(0, 'end')
                entry2__.insert(0, 'Result will be shown here')
            labelv__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                            fg='grey', font=('bold', 12), bg='white')
            labelv__.place(x=940, y=387)
            x__ = labelv__
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if float.is_integer(float(w)):
                    result = bin(int(w, 8)).lstrip('0b')
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, result)
                if not float.is_integer(float(w)):
                    whole, decimal = str(w).split('.')
                    whole = int(whole)
                    decimal = int(decimal)
                    res = bin(int(str(whole), 8)).lstrip('0b') + '.'
                    ult = bin(int(str(decimal), 8)).lstrip('0b')
                    bina = res + ult
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, bina)
            except(ValueError, KeyError):
                if not entry2__.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, 'Result will be shown here')
                labely__ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely__.place(x=940, y=387)
                y__ = labely__
        else:
            labelz__ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                            fg='grey', bg='white', font=('bold', 12))
            labelz__.place(x=940, y=387)
            z__ = labelz__


def oct_to_oct():
    value2 = entry1__.get()
    return oct_to_oct_1(value2)


# noinspection PyGlobalUndefined
def oct_to_oct_1(value2):
    destroy__()
    global v__  # here the global function is defined so that the assigned variables can be
    global x__  # used in different functions ( i.e. out of the scope of this function )
    global y__
    global z__
    global g__
    if str(value2) == 'Enter a Decimal Value':
        if not entry2__.get() == 'Result will be shown here':
            entry2__.delete(0, 'end')
            entry2__.insert(0, 'Result will be shown here')
        labelu__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                         fg='grey', font=('bold', 12), bg='white')
        labelu__.place(x=940, y=387)
        v__ = labelu__
    else:
        if len(str(value2)) < 1:
            if not entry2__.get() == 'Result will be shown here':
                entry2__.delete(0, 'end')
                entry2__.insert(0, 'Result will be shown here')
            labelv__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                             fg='grey', font=('bold', 12), bg='white')
            labelv__.place(x=940, y=387)
            x__ = labelv__
        elif (len(str(value2)) >= 1) and (len(str(value2)) <= 15):
            try:
                if float.is_integer(float(value2)):
                    result1 = oct(int(value2, 8)).lstrip('0o')
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, result1)
                if not float.is_integer(float(value2)):
                    whole, decimal = str(value2).split('.')
                    whole = oct(int(whole, 8)).lstrip('0o') + '.'
                    decimal = oct(int(decimal, 8)).lstrip('0o')
                    resultant = whole + decimal
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, resultant)
            except ValueError:
                if not entry2__.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, 'Result will be shown here')
                labely__ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely__.place(x=940, y=387)
                y__ = labely__
        else:
            labelz__ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                             fg='grey', bg='white', font=('bold', 12))
            labelz__.place(x=940, y=387)
            z__ = labelz__


def oct_to_dec():
    value = entry1__.get()
    return oct_to_dec_1(value)


def oct_to_dec_1(w):
    destroy__()
    global v__  # here the global function is defined so that the assigned variables can be
    global x__  # used in different functions ( i.e. out of the scope of this function )
    global y__
    global z__
    global g__
    if str(w) == 'Enter a Decimal Value':
        if not entry2__.get() == 'Result will be shown here':
            entry2__.delete(0, 'end')
            entry2__.insert(0, 'Result will be shown here')
        labelu__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                         fg='grey', font=('bold', 12), bg='white')
        labelu__.place(x=940, y=387)
        v__ = labelu__
    else:
        if len(str(w)) < 1:
            if not entry2__.get() == 'Result will be shown here':
                entry2__.delete(0, 'end')
                entry2__.insert(0, 'Result will be shown here')
            labelv__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                             fg='grey', font=('bold', 12), bg='white')
            labelv__.place(x=940, y=387)
            x__ = labelv__
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if not '.' in str(w):
                    re = int(w, 8)
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, re)
                if '.' in str(w):
                    whole, decimal = str(w).split('.')
                    whole = str(int(whole, 8)) + '.'
                    decimal = str(int(decimal, 8))
                    result2 = whole + decimal
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, result2)
            except ValueError:
                if not entry2__.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, 'Result will be shown here')
                labely__ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely__.place(x=940, y=387)
                y__ = labely__
        else:
            labelz__ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                             fg='grey', bg='white', font=('bold', 12))
            labelz__.place(x=940, y=387)
            z__ = labelz__


def oct_to_hex():
    value = entry1__.get()
    return oct_to_hex_1(value)


def oct_to_hex_1(w):
    destroy__()
    global v__  # here the global function is defined so that the assigned variables can be
    global x__  # used in different functions ( i.e. out of the scope of this function )
    global y__
    global z__
    global g__
    if str(w) == 'Enter a Decimal Value':
        if not entry2__.get() == 'Result will be shown here':
            entry2__.delete(0, 'end')
            entry2__.insert(0, 'Result will be shown here')
        labelu__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                         fg='grey', font=('bold', 12), bg='white')
        labelu__.place(x=940, y=387)
        v__ = labelu__
    else:
        if len(str(w)) < 1:
            if not entry2__.get() == 'Result will be shown here':
                entry2__.delete(0, 'end')
                entry2__.insert(0, 'Result will be shown here')
            labelv__ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                             fg='grey', font=('bold', 12), bg='white')
            labelv__.place(x=940, y=387)
            x__ = labelv__
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if float.is_integer(float(w)):
                    result1 = str(hex(int(w, 8))).lstrip('0x')
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, result1)
                if not float.is_integer(float(w)):
                    whole, decimal = str(w).split('.')
                    whole = str(hex(int(whole, 8))).lstrip('0x') + '.'
                    decimal = str(hex(int(decimal, 8))).lstrip('0x')
                    result2 = whole.upper() + decimal.upper()
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, result2)
            except ValueError:
                if not entry2__.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2__.delete(0, 'end')
                    entry2__.insert(0, 'Result will be shown here')
                labely__ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely__.place(x=940, y=387)
                y__ = labely__
        else:
            labelz__ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                             fg='grey', bg='white', font=('bold', 12))
            labelz__.place(x=940, y=387)
            z__ = labelz__


def decimal():
    global label4
    destroy_label()
    label4 = Label(root2, text='Decimal Value----->', font=('Comic Sans MS', 18), fg='#0198E1', bg='white')
    label4.place(x=180, y=378)

    global entry1
    entry1 = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry1.configure(font=('-family', 'Comic Sans MS'))
    entry1.insert(0, 'Enter a Decimal Value')
    entry1.bind('<FocusIn>', on_entry_click1)
    entry1.bind('<FocusOut>', on_focusout1)
    entry1.place(x=420, y=380, height=40)

    global entry2
    entry2 = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry2.configure(font=('-family', 'Comic Sans MS'))
    entry2.insert(0, 'Result will be shown here')  # This is the second entry where the results are displayed
    entry2.place(x=420, y=600, height=40)

    try:
        canvas2.create_text(145, 523, text="Binary", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(470, 523, text="Octal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(812, 523, text="Decimal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(1154, 523, text="Hexa-Decimal", font=("Comic Sans MS", 15), fill='black')
        button6 = Button(root2, padx=9, bg="#009dff", command=dec_to_bin)
        button6.place(x=80, y=511)
        button7 = Button(root2, padx=9, bg="#009dff", command=dec_to_oct)
        button7.place(x=410, y=511)
        button8 = Button(root2, padx=9, bg="#009dff", command=dec_to_dec)
        button8.place(x=740, y=511)
        button9 = Button(root2, padx=9, bg="#009dff", command=dec_to_hex)
        button9.place(x=1050, y=511)
        button10 = Button(root2, text='Reset Value', padx=16, pady=2, bg='#009dff', fg='white', relief='raised',
                          font=('Comic Sans MS', 10), command=reset1)
        button10.place(x=140, y=600)
    except TypeError:
        pass


def dec_to_bin():
    _x_ = entry1.get()  # This function takes the user input entered in the entry and place it as an arguement
    return dec_to_bin_1(_x_)


# noinspection PyGlobalUndefined
def dec_to_bin_1(w):
    destroy()
    global v                         # here the global function is defined so that the assigned variables can be
    global x                         # used in different functions ( i.e. out of the scope of this function )
    global y
    global z
    global g
    if str(w) == 'Enter a Decimal Value':
        if not entry2.get() == 'Result will be shown here':               # This checks if the user has entered
            entry2.delete(0, 'end')                                       # something or not
            entry2.insert(0, 'Result will be shown here')
        labelu = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                       fg='grey', font=('bold', 12), bg='white')                     # if the user has not
        labelu.place(x=940, y=387)                                                      # entered something, it displays
        v = labelu                                                                      # an error messsage ( label )
    else:
        if len(str(w)) < 1:
            if not entry2.get() == 'Result will be shown here':           # this checks if the length of the user input
                entry2.delete(0, 'end')                                   # is zero or not
                entry2.insert(0, 'Result will be shown here')
            labelv = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',  # if the length is zero, an
                           fg='grey', font=('bold', 12), bg='white')                    # error message is displayed
            labelv.place(x=940, y=387)
            x = labelv
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):               # This checks so that the lenght don't exceeds
            try:
                if float.is_integer(float(w)):                   # If the length doesn't exceed, the function will
                    whole_no = bin(int(w)).lstrip('0b')          # check if the user input value is float or integer
                    entry2.delete(0, 'end')
                    entry2.insert(0, whole_no)                   # If it is an integer, it will directly convert the
                elif not float.is_integer(float(w)):             # value to binary
                    whole, decimal = str(w).split('.')
                    whole = int(whole)                           # If it is a float value, it will split it into two
                    decimal = int(decimal)                       # parts and convert them separately into binary values
                    ful = bin(whole).lstrip('0b') + '.'
                    for i in range(5):
                        whole, decimal = str((c_decimal(decimal)) * 2).split('.')
                        decimal = int(decimal)
                        ful += whole                             # It will convert the decimal part to binary upto 5
                    entry2.delete(0, 'end')                      # decimal places
                    entry2.insert(0, ful)
            except ValueError:
                if not entry2.get() == 'Result will be shown here':     # If the user enters an invalid value, an error
                    entry2.delete(0, 'end')                             # message will be displayed
                    entry2.insert(0, 'Result will be shown here')
                labely = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely.place(x=940, y=387)
                y = labely
        else:
            labelz = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                           fg='grey', bg='white', font=('bold', 12))
            labelz.place(x=940, y=387)                                           # If the user input exceeds the range,
            z = labelz                                                           # an error messange is displayed


def c_decimal(a):
    while float(a) >= 1:      # This function is called to convert the spearated decimal user input value to binary
        a /= 10
    return a


def dec_to_oct():
    value = entry1.get()
    return dec_to_oct_1(value)


def dec_to_oct_1(w):
    destroy()
    global v  # here the global function is defined so that the assigned variables can be
    global x  # used in different functions ( i.e. out of the scope of this function )
    global y
    global z
    global g
    if str(w) == 'Enter a Decimal Value':
        if not entry2.get() == 'Result will be shown here':  # This checks if the user has entered
            entry2.delete(0, 'end')  # something or not
            entry2.insert(0, 'Result will be shown here')
        labelu = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                       fg='grey', font=('bold', 12), bg='white')  # if the user has not
        labelu.place(x=940, y=387)  # entered something, it displays
        v = labelu  # an error messsage ( label )
    else:
        if len(str(w)) < 1:
            if not entry2.get() == 'Result will be shown here':  # this checks if the length of the user input
                entry2.delete(0, 'end')  # is zero or not
                entry2.insert(0, 'Result will be shown here')
            labelv = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',  # if the length is zero, an
                           fg='grey', font=('bold', 12), bg='white')  # error message is displayed
            labelv.place(x=940, y=387)
            x = labelv
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):  # This checks so that the lenght don't exceeds
            try:
                if float.is_integer(float(w)):
                    result = str(oct(int(w))).lstrip('0o')
                    entry2.delete(0, 'end')
                    entry2.insert(0, result)
                if not float.is_integer(float(w)):
                    whole, decimal = str(w).split('.')
                    whole = str(oct(int(whole))).lstrip('0o') + '.'
                    decimal = str(oct(int(decimal))).lstrip('0o')
                    resultant = whole + decimal
                    entry2.delete(0, 'end')
                    entry2.insert(0, resultant)
            except ValueError:
                if not entry2.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2.delete(0, 'end')  # message will be displayed
                    entry2.insert(0, 'Result will be shown here')
                labely = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely.place(x=940, y=387)
                y = labely
        else:
            labelz = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                           fg='grey', bg='white', font=('bold', 12))
            labelz.place(x=940, y=387)
            z = labelz


def dec_to_dec():
    value = entry1.get()
    return dec_to_dec_1(value)


def dec_to_dec_1(w):
    destroy()
    global v  # here the global function is defined so that the assigned variables can be
    global x  # used in different functions ( i.e. out of the scope of this function )
    global y
    global z
    global g
    if str(w) == 'Enter a Decimal Value':
        if not entry2.get() == 'Result will be shown here':  # This checks if the user has entered
            entry2.delete(0, 'end')  # something or not
            entry2.insert(0, 'Result will be shown here')
        labelu = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                       fg='grey', font=('bold', 12), bg='white')  # if the user has not
        labelu.place(x=940, y=387)  # entered something, it displays
        v = labelu  # an error messsage ( label )
    else:
        if len(str(w)) < 1:
            if not entry2.get() == 'Result will be shown here':  # this checks if the length of the user input
                entry2.delete(0, 'end')  # is zero or not
                entry2.insert(0, 'Result will be shown here')
            labelv = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',  # if the length is zero, an
                           fg='grey', font=('bold', 12), bg='white')  # error message is displayed
            labelv.place(x=940, y=387)
            x = labelv
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):  # This checks so that the lenght don't exceeds
            try:
                if float.is_integer(float(w)):
                    result = int(w)
                    entry2.delete(0, 'end')
                    entry2.insert(0, result)
                if not float.is_integer(float(w)):
                    resultant = float(w)
                    entry2.delete(0, 'end')
                    entry2.insert(0, resultant)
            except ValueError:
                if not entry2.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2.delete(0, 'end')  # message will be displayed
                    entry2.insert(0, 'Result will be shown here')
                labely = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely.place(x=940, y=387)
                y = labely
        else:
            labelz = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                           fg='grey', bg='white', font=('bold', 12))
            labelz.place(x=940, y=387)  # If the user input exceeds the range,
            z = labelz


def dec_to_hex():
    value = entry1.get()
    return dec_to_hex_1(value)


def dec_to_hex_1(w):
    destroy()
    global v  # here the global function is defined so that the assigned variables can be
    global x  # used in different functions ( i.e. out of the scope of this function )
    global y
    global z
    global g
    if str(w) == 'Enter a Decimal Value':
        if not entry2.get() == 'Result will be shown here':  # This checks if the user has entered
            entry2.delete(0, 'end')  # something or not
            entry2.insert(0, 'Result will be shown here')
        labelu = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                       fg='grey', font=('bold', 12), bg='white')  # if the user has not
        labelu.place(x=940, y=387)  # entered something, it displays
        v = labelu  # an error messsage ( label )
    else:
        if len(str(w)) < 1:
            if not entry2.get() == 'Result will be shown here':  # this checks if the length of the user input
                entry2.delete(0, 'end')  # is zero or not
                entry2.insert(0, 'Result will be shown here')
            labelv = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',  # if the length is zero, an
                           fg='grey', font=('bold', 12), bg='white')  # error message is displayed
            labelv.place(x=940, y=387)
            x = labelv
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):  # This checks so that the lenght don't exceeds
            try:
                if float.is_integer(float(w)):
                    result = str(hex(int(w))).lstrip('0x')
                    entry2.delete(0, 'end')
                    entry2.insert(0, result)
                if not float.is_integer(float(w)):
                    whole, decimal = str(w).split('.')
                    whole = str(hex(int(whole))).lstrip('0x') + '.'
                    decimal = str(hex(int(decimal))).lstrip('0x')
                    resultant = whole + decimal
                    entry2.delete(0, 'end')
                    entry2.insert(0, resultant)
            except ValueError:
                if not entry2.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2.delete(0, 'end')  # message will be displayed
                    entry2.insert(0, 'Result will be shown here')
                labely = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely.place(x=940, y=387)
                y = labely
        else:
            labelz = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                           fg='grey', bg='white', font=('bold', 12))
            labelz.place(x=940, y=387)
            z = labelz


def caps(event):
    text.set(text.get().upper())


def hexa_decimal():
    global label6
    destroy_label()
    label6 = Label(root2, text='Hex Value----->', font=('Comic Sans MS', 18), fg='#0198E1', bg='white')
    label6.place(x=180, y=378)

    global entry1___
    global text
    text = StringVar()
    entry1___ = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff', textvariable=text)
    entry1___.configure(font=('-family', 'Comic Sans MS'))
    entry1___.insert(0, 'Enter a Decimal Value')
    entry1___.bind('<FocusIn>', on_entry_click4)
    entry1___.bind('<FocusOut>', on_focusout4)
    entry1___.bind('<KeyRelease>', caps)
    entry1___.place(x=420, y=380, height=40)

    global entry2___
    entry2___ = Entry(root2, width=50, justify='center', font='normal', fg='white', borderwidth=2, bg='#009dff')
    entry2___.configure(font=('-family', 'Comic Sans MS'))
    entry2___.insert(0, 'Result will be shown here')  # This is the second entry where the results are displayed
    entry2___.place(x=420, y=600, height=40)

    try:
        canvas2.create_text(145, 523, text="Binary", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(470, 523, text="Octal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(812, 523, text="Decimal", font=("Comic Sans MS", 15), fill='black')
        canvas2.create_text(1154, 523, text="Hexa-Decimal", font=("Comic Sans MS", 15), fill='black')
        button6 = Button(root2, padx=9, bg="#009dff", command=hex_to_bin)
        button6.place(x=80, y=511)
        button7 = Button(root2, padx=9, bg="#009dff", command=hex_to_oct)
        button7.place(x=410, y=511)
        button8 = Button(root2, padx=9, bg="#009dff", command=hex_to_dec)
        button8.place(x=740, y=511)
        button9 = Button(root2, padx=9, bg="#009dff", command=hex_to_hex)
        button9.place(x=1050, y=511)
        button10 = Button(root2, text='Reset Value', padx=16, pady=2, bg='#009dff', fg='white', relief='raised',
                          font=('Comic Sans MS', 10), command=reset4)
        button10.place(x=140, y=600)
    except TypeError:
        pass


def hex_to_bin():
    value = entry1___.get()
    return hex_to_bin_1(value)


def hex_to_bin_1(w):
    destroy___()
    global v___  # here the global function is defined so that the assigned variables can be
    global x___  # used in different functions ( i.e. out of the scope of this function )
    global y___
    global z___
    global g___
    if str(w) == 'Enter a Decimal Value':
        if not entry2___.get() == 'Result will be shown here':
            entry2___.delete(0, 'end')
            entry2___.insert(0, 'Result will be shown here')
        labelu___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                         fg='grey', font=('bold', 12), bg='white')
        labelu___.place(x=940, y=387)
        v___ = labelu___
    else:
        if len(str(w)) < 1:
            if not entry2___.get() == 'Result will be shown here':
                entry2___.delete(0, 'end')
                entry2___.insert(0, 'Result will be shown here')
            labelv___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                             fg='grey', font=('bold', 12), bg='white')
            labelv___.place(x=940, y=387)
            x___ = labelv___
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if not '.' in str(w):
                    result = bin(int(w, 16)).lstrip('0b')
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, result)
                if '.' in str(w):
                    whole, decimal = str(w).split('.')
                    whole = int(whole, 16)
                    decimal = int(decimal, 16)
                    res = bin(int(str(whole))).lstrip('0b') + '.'
                    ult = bin(int(str(decimal))).lstrip('0b')
                    bina = res + ult
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, bina)
            except ValueError:
                if not entry2___.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, 'Result will be shown here')
                labely___ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely___.place(x=940, y=387)
                y___ = labely___
        else:
            labelz___ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                             fg='grey', bg='white', font=('bold', 12))
            labelz___.place(x=940, y=387)
            z___ = labelz___


def hex_to_oct():
    value = entry1___.get()
    return hex_to_oct_1(value)


def hex_to_oct_1(w):
    destroy___()
    global v___  # here the global function is defined so that the assigned variables can be
    global x___  # used in different functions ( i.e. out of the scope of this function )
    global y___
    global z___
    global g___
    if str(w) == 'Enter a Decimal Value':
        if not entry2___.get() == 'Result will be shown here':
            entry2___.delete(0, 'end')
            entry2___.insert(0, 'Result will be shown here')
        labelu___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                          fg='grey', font=('bold', 12), bg='white')
        labelu___.place(x=940, y=387)
        v___ = labelu___
    else:
        if len(str(w)) < 1:
            if not entry2___.get() == 'Result will be shown here':
                entry2___.delete(0, 'end')
                entry2___.insert(0, 'Result will be shown here')
            labelv___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                              fg='grey', font=('bold', 12), bg='white')
            labelv___.place(x=940, y=387)
            x___ = labelv___
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if not '.' in str(w):
                    result = oct(int(w, 16)).lstrip('0o')
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, result)
                if '.' in str(w):
                    whole, decimal = str(w).split('.')
                    whole = int(whole, 16)
                    decimal = int(decimal, 16)
                    res = oct(int(str(whole))).lstrip('0o') + '.'
                    ult = oct(int(str(decimal))).lstrip('0o')
                    bina = res + ult
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, bina)
            except ValueError:
                if not entry2___.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, 'Result will be shown here')
                labely___ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely___.place(x=940, y=387)
                y___ = labely___
        else:
            labelz___ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                              fg='grey', bg='white', font=('bold', 12))
            labelz___.place(x=940, y=387)
            z___ = labelz___


def hex_to_dec():
    value = entry1___.get()
    return hex_to_dec_1(value)


def hex_to_dec_1(w):
    destroy___()
    global v___  # here the global function is defined so that the assigned variables can be
    global x___  # used in different functions ( i.e. out of the scope of this function )
    global y___
    global z___
    global g___
    if str(w) == 'Enter a Decimal Value':
        if not entry2___.get() == 'Result will be shown here':
            entry2___.delete(0, 'end')
            entry2___.insert(0, 'Result will be shown here')
        labelu___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                          fg='grey', font=('bold', 12), bg='white')
        labelu___.place(x=940, y=387)
        v___ = labelu___
    else:
        if len(str(w)) < 1:
            if not entry2___.get() == 'Result will be shown here':
                entry2___.delete(0, 'end')
                entry2___.insert(0, 'Result will be shown here')
            labelv___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                              fg='grey', font=('bold', 12), bg='white')
            labelv___.place(x=940, y=387)
            x___ = labelv___
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if not '.' in str(w):
                    result = str(int(w, 16))
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, result)
                if '.' in str(w):
                    whole, decimal = str(w).split('.')
                    whole = int(whole, 16)
                    decimal = int(decimal, 16)
                    res = str(whole) + '.'
                    ult = str(decimal)
                    bina = res + ult
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, bina)
            except ValueError:
                if not entry2___.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, 'Result will be shown here')
                labely___ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely___.place(x=940, y=387)
                y___ = labely___
        else:
            labelz___ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                              fg='grey', bg='white', font=('bold', 12))
            labelz___.place(x=940, y=387)
            z___ = labelz___


def hex_to_hex():
    value = entry1___.get()
    return hex_to_hex_1(value)


def hex_to_hex_1(w):
    destroy___()
    global v___  # here the global function is defined so that the assigned variables can be
    global x___  # used in different functions ( i.e. out of the scope of this function )
    global y___
    global z___
    global g___
    if str(w) == 'Enter a Decimal Value':
        if not entry2___.get() == 'Result will be shown here':
            entry2___.delete(0, 'end')
            entry2___.insert(0, 'Result will be shown here')
        labelu___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                          fg='grey', font=('bold', 12), bg='white')
        labelu___.place(x=940, y=387)
        v___ = labelu___
    else:
        if len(str(w)) < 1:
            if not entry2___.get() == 'Result will be shown here':
                entry2___.delete(0, 'end')
                entry2___.insert(0, 'Result will be shown here')
            labelv___ = Label(root2, text='#Don\'t keep the entry blank. Enter something ! ',
                              fg='grey', font=('bold', 12), bg='white')
            labelv___.place(x=940, y=387)
            x___ = labelv___
        elif (len(str(w)) >= 1) and (len(str(w)) <= 15):
            try:
                if not '.' in str(w):
                    result = hex(int(w, 16)).lstrip('0x')
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, result.upper())
                if '.' in str(w):
                    whole, decimal = str(w).split('.')
                    whole = int(whole, 16)
                    decimal = int(decimal, 16)
                    res = hex(int(str(whole))).lstrip('0x') + '.'
                    ult = hex(int(str(decimal))).lstrip('0x')
                    bina = res + ult
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, bina.upper())
            except ValueError:
                if not entry2___.get() == 'Result will be shown here':  # If the user enters an invalid value, an error
                    entry2___.delete(0, 'end')
                    entry2___.insert(0, 'Result will be shown here')
                labely___ = Label(root2, text='#Invalid Input', fg='grey', bg='white', font=('bold', 12))
                labely___.place(x=940, y=387)
                y___ = labely___
        else:
            labelz___ = Label(root2, text='#Invalid Range ! You can enter a maximum of 15 digits',
                              fg='grey', bg='white', font=('bold', 12))
            labelz___.place(x=940, y=387)
            z___ = labelz___


def main_window():
    global root2
    global canvas2
    root2 = Tk()
    root2.state('zoomed')
    root2.title('Number System Converter')
    canvas2 = Canvas(root2, bg='white')
    canvas2.pack(fill='both', expand=True)

    canvas2.create_text(330, 140, text='Select The Number System For The User Input : - ', fill='black',
                        font=('Comic Sans MS', 20))

    canvas2.create_text(145, 263, text="Binary", font=("Comic Sans MS", 15), fill='black')
    canvas2.create_text(470, 263, text="Octal", font=("Comic Sans MS", 15), fill='black')
    canvas2.create_text(812, 263, text="Decimal", font=("Comic Sans MS", 15), fill='black')
    canvas2.create_text(1154, 263, text="Hexa-Decimal", font=("Comic Sans MS", 15), fill='black')

    button2 = Button(root2, padx=9, bg="#009dff", command=binary)
    button2.place(x=80, y=251)
    button3 = Button(root2, padx=9, bg="#009dff", command=octal)
    button3.place(x=410, y=251)
    button4 = Button(root2, padx=9, bg="#009dff", command=decimal)
    button4.place(x=740, y=251)
    button5 = Button(root2, padx=9, bg="#009dff", command=hexa_decimal)
    button5.place(x=1050, y=251)
    button6 = Button(root2, padx=10, pady=2, text='Quit', bg="#009dff", fg='white', relief='raised', font=('Comic Sans MS', 10), command=root2.destroy)
    button6.place(x=1100, y=600)

    frame1 = Frame(root2, width=root2.winfo_screenwidth(), height=80, bg='#00688B', relief='ridge')
    frame1.place(y=0)

    label2 = Label(frame1, text='Number System Converter', bg='#00688B', fg='#67C8FF')
    label2.configure(font=('-family', 'Riona Sans', '-slant', 'italic', '-weight', 'bold', '-size', 32))
    label2.place(x=410, y=13)


root1.mainloop()
