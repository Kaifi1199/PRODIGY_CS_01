import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_value = ord(char.upper())
            num = ascii_value - 65
            if mode == 'encrypt':
                shifted = (num + shift) % 26
            else:
                shifted = (num - shift) % 26
            result = result + chr(shifted + 65)
        else:
            result = result + char
    return result

def process_text():
    mode = mode_var.get()
    message = message_entry.get()
    try:
        shift = int(shift_entry.get())
        if 0 <= shift <= 25:
            result = caesar_cipher(message, shift, mode)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, result)
        else:
            messagebox.showerror("Error!", "Shift value must be between 0 and 25!")
    except ValueError:
        messagebox.showerror("Error!", "Please enter a valid integer for the shift value!")

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Message:").grid(column=0, row=0, sticky=tk.W)
message_entry = ttk.Entry(frame, width=40)
message_entry.grid(column=1, row=0, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Shift (0-25):").grid(column=0, row=1, sticky=tk.W)
shift_entry = ttk.Entry(frame, width=5)
shift_entry.grid(column=1, row=1, sticky=tk.W)

ttk.Label(frame, text="Mode:").grid(column=0, row=2, sticky=tk.W)
mode_var = tk.StringVar(value="encrypt")
ttk.Radiobutton(frame, text="Encrypt", variable=mode_var, value="encrypt").grid(column=1, row=2, sticky=tk.W)
ttk.Radiobutton(frame, text="Decrypt", variable=mode_var, value="decrypt").grid(column=2, row=2, sticky=tk.W)

ttk.Button(frame, text="Process", command=process_text).grid(column=1, row=3)

ttk.Label(frame, text="Result:").grid(column=0, row=4, sticky=tk.W)
result_text = tk.Text(frame, width=40, height=5)
result_text.grid(column=0, row=5, columnspan=3)

for child in frame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()