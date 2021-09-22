import tkinter as tk
from tkinter import BOTH, TOP
from PIL import ImageTk, Image


def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("backgrounds/abstract-background-resized.gif")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
    canvas.pack(fill=BOTH, expand=True)


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

add_transaction_button = tk.Button(canvas, text="Add Transaction", height=1, width=20)
predict_button = tk.Button(canvas, text="Predict", height=1, width=20)
canvas.create_window(250, 490, window=add_transaction_button)
canvas.create_window(550, 490, window=predict_button)

window.resizable(0, 0)
window.mainloop()
