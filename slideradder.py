import tkinter as tk
from tkinter import messagebox

# Define a function to change the background color of a widget
def change_color(widget, color):
    widget.configure(bg=color)

# Define a function to show the message box with the total value
def show_message():
    # Get the values of the sliders
    slider1_value = int(slider1.get())
    slider2_value = int(slider2.get())

    # Calculate the total value
    total_value = slider1_value + slider2_value

    # Display the message box with the total value
    messagebox.showinfo("Total Value", f"The total value is {total_value}")

# Create the main window
root = tk.Tk()
root.title("Slider Adder")
root.configure(bg="#f2f2f2")

# Create the sliders
slider1 = tk.Scale(root, from_=-999, to=999, orient=tk.HORIZONTAL, label="1st Number", bg="#f2f2f2", fg="#333333", font=("Arial", 12))
slider1.pack(pady=20)

slider2 = tk.Scale(root, from_=-999, to=999, orient=tk.HORIZONTAL, label="2nd Number", bg="#f2f2f2", fg="#333333", font=("Arial", 12))
slider2.pack(pady=20)

# Create the button to show the message box
button = tk.Button(root, text="Show the Sum", bg="#4CAF50", fg="#ffffff", font=("Arial", 12), command=show_message)
button.pack(pady=20)

# Change the background color of the slider and button when hovered
def on_enter(event):
    change_color(event.widget, "#e6e6e6")

def on_leave(event):
    change_color(event.widget, "#f2f2f2")

slider1.bind("<Enter>", on_enter)
slider1.bind("<Leave>", on_leave)

slider2.bind("<Enter>", on_enter)
slider2.bind("<Leave>", on_leave)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Start the main loop
root.mainloop()