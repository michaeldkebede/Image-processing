# A multipurpose image processing program with Tkinter GUI.

import tkinter as tk

window = tk.Tk()
txt = tk.Label(text="Python rocks!")
txt.pack()

image = tk.PhotoImage(file='download.png')
txt['image'] = image
window.mainloop()