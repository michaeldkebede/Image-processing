# A multipurpose image processing program with Tkinter GUI.

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image


global_image = 0


# Open image file for editing(image processing)
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("png", "*.png"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    image = ImageTk.PhotoImage(file=filepath)
    display_lbl.configure(image=image)
    display_lbl.image = image
    global global_image
    global_image = image


# Save file
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="jpeg",
        filetypes=[("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("png", "*.png"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    global global_image
    save_image = Image.fromarray(global_image)
    save_image.save(filepath)

# main logic of program
root = tk.Tk()
# display the name of the application on the title bar
root.title("KMAM Image Processor")

# configure minimum size of the root
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

# create widgets
fr_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
display_lbl = tk.Label(root)

# place the two buttons on the root
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# place widget on windows
fr_buttons.grid(row=0, column=0, sticky="ns")
display_lbl.grid(row=0, column=1, sticky="nsew")

root.mainloop()
