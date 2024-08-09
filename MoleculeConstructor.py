import tkinter as tk
from tkinter import ttk
import tkinter.font as font  # Import the font module


# Dictionary of elements with their most common valencies
elements = {
    'H': [1], 'He': [0], 'Li': [1], 'Be': [2], 'B': [3], 'C': [2, 4], 'N': [3, 5], 'O': [2], 'F': [1], 'Ne': [0],
    'Na': [1], 'Mg': [2], 'Al': [3], 'Si': [4], 'P': [3, 5], 'S': [2, 4, 6], 'Cl': [1, 3, 5, 7], 'Ar': [0],
    'K': [1], 'Ca': [2], 'Sc': [3], 'Ti': [4], 'V': [5], 'Cr': [2, 3, 6], 'Mn': [2, 4, 7], 'Fe': [2, 3],
    'Co': [2, 3], 'Ni': [2], 'Cu': [1, 2], 'Zn': [2], 'Ga': [3], 'Ge': [4], 'As': [3, 5], 'Se': [2, 4, 6],
    'Br': [1, 3, 5, 7], 'Kr': [0], 'Rb': [1], 'Sr': [2], 'Y': [3], 'Zr': [4], 'Nb': [5], 'Mo': [6],
    'Tc': [7], 'Ru': [8], 'Rh': [3, 4], 'Pd': [2, 4], 'Ag': [1], 'Cd': [2], 'In': [3], 'Sn': [4],
    'Sb': [3, 5], 'Te': [2, 4, 6], 'I': [1, 3, 5, 7], 'Xe': [0], 'Cs': [1], 'Ba': [2], 'La': [3],
    'Ce': [3, 4], 'Pr': [3, 4], 'Nd': [3], 'Pm': [3], 'Sm': [2, 3], 'Eu': [2, 3], 'Gd': [3],
    'Tb': [3, 4], 'Dy': [3], 'Ho': [3], 'Er': [3], 'Tm': [2, 3], 'Yb': [2, 3], 'Lu': [3],
    'Hf': [4], 'Ta': [5], 'W': [6], 'Re': [7], 'Os': [4, 6, 8], 'Ir': [3, 4], 'Pt': [2, 4],
    'Au': [1, 3], 'Hg': [1, 2], 'Tl': [1, 3], 'Pb': [2, 4], 'Bi': [3, 5], 'Th': [4], 'Pa': [5],
    'U': [3, 4, 5, 6], 'Np': [3, 4, 5, 6, 7], 'Pu': [3, 4, 5, 6, 7, 8], 'Am': [2, 3, 4, 5, 6, 7],
    'Cm': [3, 4], 'Bk': [3, 4], 'Cf': [2, 3, 4], 'Es': [2, 3], 'Fm': [2, 3], 'Md': [2, 3], 'No': [2, 3],
    'Lr': [3], 'Rf': [4], 'Db': [5], 'Sg': [6], 'Bh': [7], 'Hs': [8], 'Mt': [9], 'Ds': [9], 'Rg': [9],
    'Cn': [2], 'Nh': [3], 'Fl': [4], 'Mc': [5], 'Lv': [6], 'Ts': [7], 'Og': [8]
}

def calculate_molecule():
    element1 = combobox1.get()
    element2 = combobox2.get()
    valency1 = int(combobox_valency1.get())
    valency2 = int(combobox_valency2.get())
    # Omit the number 1 and 0 in the molecular formula
    molecule.set(f"{element1}{'' if valency2 in [0, 1] else valency2}{element2}{'' if valency1 in [0, 1] else valency1}")

def update_valency1(*args):
    element = combobox1.get()
    combobox_valency1['values'] = elements[element]
    combobox_valency1.current(0)  # Automatically select the first valency

def update_valency2(*args):
    element = combobox2.get()
    combobox_valency2['values'] = elements[element]
    combobox_valency2.current(0)  # Automatically select the first valency

root = tk.Tk()
root.title("Molecular Formula Maker")

# Increase the window size
root.geometry('345x150')  # Width x Height

# Increase the font size
default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(size=13)

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

combobox1 = ttk.Combobox(frame, values=list(elements.keys()))
combobox1.grid(row=0, column=0, padx=(0, 10))
combobox1.bind('<<ComboboxSelected>>', update_valency1)

combobox2 = ttk.Combobox(frame, values=list(elements.keys()))
combobox2.grid(row=0, column=1)
combobox2.bind('<<ComboboxSelected>>', update_valency2)

combobox_valency1 = ttk.Combobox(frame)
combobox_valency1.grid(row=1, column=0)

combobox_valency2 = ttk.Combobox(frame)
combobox_valency2.grid(row=1, column=1)

button = ttk.Button(frame, text="Calculate Molecule", command=calculate_molecule)
button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

molecule = tk.StringVar()
molecule_label = ttk.Label(frame, textvariable=molecule)
molecule_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
