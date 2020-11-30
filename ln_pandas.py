import PySimpleGUI as sg
from openpyxl import workbook
import pandas as pd


def draw_window():
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [[sg.Text('Filename')],
              [sg.Input(), sg.FileBrowse()],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Get filename example', layout)
    event, values = window.read()
    window.close()
    return values['Browse']


# df_excel = pd.read_excel(draw_window())

df_csv = pd.read_csv(draw_window())

embark = df_csv[df_csv['Embarked']=='Q']
survived = df_csv[df_csv['Survived']=='Yes']

print(df_csv[df_csv['Embarked'] == 'Q'])

print(df_csv[(df_csv['Embarked'] == 'Q') & (df_csv['Survived'] == 'Yes')])


