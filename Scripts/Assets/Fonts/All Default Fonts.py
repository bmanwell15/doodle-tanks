import tkinter as tk
from tkinter import font

# Create the main application window
root = tk.Tk()
root.geometry("1000x700")

# Create a label and apply the custom font
for index in range(len(font.families())):
    label = tk.Label(root, text=f"{index}. Doodle Tanks", font=(font.families()[index], 8))
    label.grid(row=index // 9, column=index % 9)

# Run the application
root.mainloop()
