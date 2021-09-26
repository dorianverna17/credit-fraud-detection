import tkinter as tk
from tkinter import BOTH, TOP, END
import tkinter.messagebox

import numpy as np
import pandas as pd
from PIL import ImageTk, Image

import fraud_prediction as fp

types = {'PAYMENT', 'DEBIT', 'CASH_OUT', 'TRANSFER', 'CASH_IN'}


def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("backgrounds/abstract-background-resized.gif")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
    canvas.pack(fill=BOTH, expand=True)


def add_transaction():
    flag = 0
    time_str = time_text.get('0.0', 'end')
    time_str = time_str[0:len(time_str) - 1]
    type_str = type_text.get('0.0', 'end')
    type_str = type_str[0:len(type_str) - 1]
    amount_str = amount_text.get('0.0', 'end')
    amount_str = amount_str[0:len(amount_str) - 1]
    name_orig_str = nameOrig_text.get('0.0', 'end')
    name_orig_str = name_orig_str[0:len(name_orig_str) - 1]
    old_balance_org_str = oldbalanceOrg_text.get('0.0', 'end')
    old_balance_org_str = old_balance_org_str[0:len(old_balance_org_str) - 1]
    new_balance_orig_str = newbalanceOrig_text.get('0.0', 'end')
    new_balance_orig_str = new_balance_orig_str[0:len(new_balance_orig_str) - 1]
    name_dest_str = nameDest_text.get('0.0', 'end')
    name_dest_str = name_dest_str[0:len(name_dest_str) - 1]
    old_balance_dest_str = oldbalanceDest_text.get('0.0', 'end')
    old_balance_dest_str = old_balance_dest_str[0:len(old_balance_dest_str) - 1]
    new_balance_dest_str = newbalanceDest_text.get('0.0', 'end')
    new_balance_dest_str = new_balance_dest_str[0:len(new_balance_dest_str) - 1]
    if time_text.get('0.0', 'end') == "\n":
        flag = 1
    if type_text.get('0.0', 'end') == "\n":
        flag = 1
    if amount_text.get('0.0', 'end') == "\n":
        flag = 1
    if nameOrig_text.get('0.0', 'end') == "\n":
        flag = 1
    if oldbalanceOrg_text.get('0.0', 'end') == "\n":
        flag = 1
    if newbalanceOrig_text.get('0.0', 'end') == "\n":
        flag = 1
    if nameDest_text.get('0.0', 'end') == "\n":
        flag = 1
    if oldbalanceDest_text.get('0.0', 'end') == "\n":
        flag = 1
    if newbalanceDest_text.get('0.0', 'end') == "\n":
        flag = 1
    s = ""
    try:
        t_time = int(time_str)
        t_amount = float(amount_str)
        t_old_balance_orig = float(old_balance_org_str)
        t_new_balance_orig = float(new_balance_orig_str)
        t_old_balance_dest = float(old_balance_dest_str)
        t_new_balance_dest = float(new_balance_dest_str)
        s = s + str(t_time) + "  -  " + str(t_amount) + "  -  " + \
            name_orig_str + "  -  " + str(t_old_balance_orig) + "  -  " + \
            str(t_new_balance_orig) + "  -  " + name_dest_str + "  -  " + \
            str(t_old_balance_dest) + "  -  " + str(t_new_balance_dest)
    except ValueError as e:
        flag = 1
    if type_str not in types:
        flag = 1
    if flag == 1:
        tk.messagebox.showinfo('Error', 'The transaction data have not been added')
    else:
        s = type_str + "  -  " + s
        box.insert("end", s)


def predict_transactions():
    df_lst = []
    for data in enumerate(box.get(0, END)):
        lst = str(data).split("  -  ")
        df_line = np.array(lst)
        df_lst.append(df_line)
    y = fp.final_model.predict(df_lst)


window = tk.Tk()
window.title("Credit Fraud Detector")
window.geometry("800x520")

# background for the main window
image = Image.open("backgrounds/abstract-background-resized.gif")
img = ImageTk.PhotoImage(image)
canvas = tk.Canvas(window, width=600, height=500)
canvas.create_image(0, 0, image=img, anchor='nw')
canvas.pack(fill=BOTH, expand=True)

# adding the desired labels
time_label = tk.Label(canvas, text="Time:", fg='white', bg='grey')
type_label = tk.Label(canvas, text="Type:", fg='white', bg='grey')
amount_label = tk.Label(canvas, text="Amount:", fg='white', bg='grey')
nameOrig_label = tk.Label(canvas, text="Origin Name:", fg='white', bg='grey')
oldbalanceOrg_label = tk.Label(canvas, text="Origin Old Balance:", fg='white', bg='grey')
newbalanceOrig_label = tk.Label(canvas, text="Origin New Balance:", fg='white', bg='grey')
nameDest_label = tk.Label(canvas, text="Destination Name:", fg='white', bg='grey')
oldbalanceDest_label = tk.Label(canvas, text="Destination Old Balance:", fg='white', bg='grey')
newbalanceDest_label = tk.Label(canvas, text="Destination New Balance:", fg='white', bg='grey')

canvas.create_window(time_label.winfo_reqwidth(), 30, window=time_label)
canvas.create_window(time_label.winfo_reqwidth(), 60, window=type_label)
canvas.create_window(time_label.winfo_reqwidth() + 9, 90, window=amount_label)
canvas.create_window(time_label.winfo_reqwidth() + 21, 120, window=nameOrig_label)
canvas.create_window(time_label.winfo_reqwidth() + 37, 150, window=oldbalanceOrg_label)
canvas.create_window(time_label.winfo_reqwidth() + 39, 180, window=newbalanceOrig_label)
canvas.create_window(time_label.winfo_reqwidth() + 35, 210, window=nameDest_label)
canvas.create_window(time_label.winfo_reqwidth() + 50, 240, window=oldbalanceDest_label)
canvas.create_window(time_label.winfo_reqwidth() + 53, 270, window=newbalanceDest_label)

time_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
type_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
amount_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
nameOrig_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
oldbalanceOrg_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
newbalanceOrig_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
nameDest_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
oldbalanceDest_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)
newbalanceDest_text = tk.Text(canvas, fg='white', bg='grey', height=1, width=70)

canvas.create_window(500, 30, window=time_text)
canvas.create_window(500, 60, window=type_text)
canvas.create_window(500, 90, window=amount_text)
canvas.create_window(500, 120, window=nameOrig_text)
canvas.create_window(500, 150, window=oldbalanceOrg_text)
canvas.create_window(500, 180, window=newbalanceOrig_text)
canvas.create_window(500, 210, window=nameDest_text)
canvas.create_window(500, 240, window=oldbalanceDest_text)
canvas.create_window(500, 270, window=newbalanceDest_text)

box = tk.Listbox(canvas, fg='white', bg='grey', height=10, width=120)
canvas.create_window(400, 380, window=box)

add_transaction_button = tk.Button(canvas, text="Add Transaction",
                                   height=1, width=20, command=add_transaction)
predict_button = tk.Button(canvas, text="Predict", height=1, width=20,
                           command=predict_transactions)
canvas.create_window(250, 490, window=add_transaction_button)
canvas.create_window(550, 490, window=predict_button)

window.resizable(0, 0)
print('ok')
window.mainloop()
