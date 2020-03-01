#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


# ------------------ Create a table ------------------
DEFAULT_ICON = 'D:\CSP\Homeworks\Python Project\lock.ico'
def make_table(num_rows, num_cols):
    row_a = ["5","19 Minutes","1 Day","8 Days"]
    row_b = ["6","8 Hours","65 Days","2 Years"]
    row_c = ["7", "9 Days", "11 Years", "200 Years"]
    row_d = ["8", "241 Days", "692 Years", "19,000 Years"]
    row_e = ["9", "17 Years", "42,000 Years", "1.8M Years"]
    return row_a,row_b,row_c,row_d,row_e
Table = make_table(num_rows=5, num_cols=4)
headings = ['Length Characters', 'Lowercase', 'Uppercase, Lowercase&Digits', 'Uppercase, Lowercase, Digits&Puctutaion']

sg.ChangeLookAndFeel('Dark')

# ------------------ GenerateScreen------------------
Generatelayout = [
    [sg.Text('                                                                          Time to bruteforce password space, assuming 10k attempts per second:',)],
    [sg.Table(values=Table, headings=headings, max_col_width=25,background_color='lightblue',auto_size_columns=True, display_row_numbers=False, justification='center', num_rows=5, alternating_row_color='blue', key='_table_', tooltip='Time to bruteforce password space, assuming 10k attempts per second')],
    [sg.T(' ')],
    [sg.ReadButton('Generate New Password'),sg.ReadButton('Your Passwords')]]

GenerateWindow = sg.Window('RamosGenerator', grab_anywhere=True, resizable=False,icon=DEFAULT_ICON).Layout(Generatelayout)

# ------------------ MainScreen------------------
mainLayout = [
    [sg.T("Hello and welcome to RamosGenerator software\nBefore the program will create your unique password\nIt will check "
          "against HackersDictionaries to make sure\nyou won't get hacked again! ", justification='center',tooltip='This program created by Ramos')],
    [sg.CloseButton('Generate New Password', tooltip = 'Want generate new password? Click here!'),sg.CloseButton('Your Passwords', key = '_Passwords_', tooltip = 'Your saved passwords')],
    [sg.T('\nRG - Watch On You ©')]
]

mainWindow = sg.Window('RamosGenerator', grab_anywhere=True, resizable=False,element_justification='center',icon=DEFAULT_ICON).Layout(mainLayout)
while True:
    mainScreenEvent, mainScreenValue = mainWindow.Read()
    print (mainScreenEvent, mainScreenValue)
    if mainScreenEvent is None:
        print("error1")
        break
    if mainScreenEvent == 'Generate New Password':
        GenerateScreenEvent, GenerateScreenValue = GenerateWindow.Read()
        break



GenerateScreen = GenerateWindow.Close()
mainScreen = mainWindow.Close()

sys.exit(69)
