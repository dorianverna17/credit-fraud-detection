import tkinter as tk
from tkinter import BOTH
from PIL import ImageTk, Image

def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("backgrounds/abstract-background-resized.gif")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

window = tk.Tk()
window.title("Credit Fraud Detector")
window.geometry("600x500")

# background for the main window
image = ImageTk.PhotoImage(file="backgrounds/abstract-background-resized.gif")
canvas = tk.Canvas(window, width=600, height=500)
canvas.pack(fill=BOTH, expand=True)
canvas.background = image
bg = canvas.create_image(0, 0, anchor=tk.NW, image=image)

window.bind("<Configure>", resize_image)
window.mainloop()
