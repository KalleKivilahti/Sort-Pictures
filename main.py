import cv2
import numpy as np
import os
from shutil import move
import customtkinter as ctk
from tkinter import Toplevel, Label, Button
from tkinter import filedialog

def sharp(image_path, threshold=20):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
    return laplacian_var >= threshold

def sort(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff')):
            image_path = os.path.join(source_folder, filename)
            if not sharp(image_path):
                os.rename(image_path, os.path.join(destination_folder, filename))

def select(label_var):
    folder_selected = filedialog.askdirectory()
    label_var.set(folder_selected)

def show_message_box(title, message):
    dialog = Toplevel()
    dialog.title(title)
    dialog.geometry("300x150")
    Label(dialog, text=message).pack(pady=10)
    Button(dialog, text="OK", command=dialog.destroy).pack(pady=5)

def start_sorting(source_var, dest_var):
    source_folder = source_var.get()
    destination_folder = dest_var.get()
    if source_folder and destination_folder:
        sort(source_folder, destination_folder)
        show_message_box("Sorting Complete", "Unsharpened images have been sorted.")

root = ctk.CTk()
root.geometry("700x300")
root.title("Unsharpened Image Sorter")

source_folder_var = ctk.StringVar()
dest_folder_var = ctk.StringVar()

ctk.CTkLabel(root, text="Source Folder:").grid(row=0, column=0, padx=5, pady=5)
ctk.CTkLabel(root, textvariable=source_folder_var, width=50).grid(row=1, column=0, padx=5, pady=5)
ctk.CTkLabel(root, text="Destination Folder:").grid(row=2, column=0, padx=5, pady=5)
ctk.CTkLabel(root, textvariable=dest_folder_var, width=50).grid(row=3, column=0, padx=5, pady=5)

ctk.CTkButton(root, text="Select Source Folder", command=lambda: select(source_folder_var)).grid(row=0, column=2, padx=5, pady=5)
ctk.CTkButton(root, text="Select Destination Folder", command=lambda: select(dest_folder_var)).grid(row=2, column=2, padx=5, pady=5)

ctk.CTkButton(root, text="Start Sorting", command=lambda: start_sorting(source_folder_var, dest_folder_var)).grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
