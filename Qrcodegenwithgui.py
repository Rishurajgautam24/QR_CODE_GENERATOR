import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import Tk, Label, Entry, Button, StringVar
from PIL import Image, ImageTk

# Create the main window
root = Tk()
root.geometry('1280x720')

# Create input fields for the URL and file name
url_label = Label(root, text="Enter the URL:")
url_label.pack()

url_entry = Entry(root)
url_entry.pack()

name_label = Label(root, text="Enter the file name:")
name_label.pack()

name_entry = Entry(root)
name_entry.pack()

# Create a button to generate the QR code
def generate_qr_code():
    # Get the URL and file name from the input fields
    s = url_entry.get()
    name = name_entry.get()

    # Generate the QR code
    url = pyqrcode.create(s)
    url.png(name+".png", scale = 6)

    # Load the QR code image
    image = Image.open(name+".png")
    image = ImageTk.PhotoImage(image)

    # Add the image to the main window
    label = Label(root, image=image)
    label.image = image  # Keep a reference to the image to prevent it from being garbage collected
    label.pack()

generate_button = Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a button to reset the input fields
def reset():
    # Clear the input fields
    url_entry.delete(0, "end")
    name_entry.delete(0, "end")
  

reset_button = Button(root, text="Reset", command=reset)
reset_button.pack()

# Run the application
root.mainloop()
