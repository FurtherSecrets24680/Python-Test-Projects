import tkinter as tk
import random

# Function to generate chemical formula
def generate_formula():
    x, y, z = random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)
    formula = f"C{x if x != 1 else ''}H{y if y != 1 else ''}O{z if z != 1 else ''}"
    return formula

# Function to update the label text
def update_label():
    formula = generate_formula()
    label.config(text=f"Formula: {formula}")

# Create the main window
root = tk.Tk()
root.title("Chemical Formula Generator")

# Create a label to display the formula
label = tk.Label(root, text="")
label.pack()

# Create a button to generate a new formula
button = tk.Button(root, text="Generate new formula", command=update_label)
button.pack()

# Run the application
root.mainloop()
