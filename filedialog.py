import tkinter as tk
from tkinter import filedialog

root= tk.Tk()
root.withdraw()  # Hide the main window
# --- This basically tell to create a file dialog box to select a file and the title of the dialog box is "Select a file" and the file types that can be selected are text files and all files.----

file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
save_path = filedialog.asksaveasfilename(title="Save file as", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

folder_path = filedialog.askdirectory(title="Select a folder") # creates a dialog box to select a folder and the title of the dialog box is "Select a folder".

# Runs the whole code 
root.mainloop()