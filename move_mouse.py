import pyautogui as pag
import tkinter as tk
from tkinter import ttk
import random
import time
import threading

exit_flag = False
def function_one():
    print("Function One is triggered!")
    # Start a separate thread for the time-consuming operation
    threading.Thread(target=automove).start()


def automove(t=5):
    while not exit_flag:
        x=random.randint(500,800)
        y=random.randint(300,700)
        pag.moveTo(x,y,0.7)
        time.sleep(t)


# Function to minimize the window
def minimize_window():
    root.iconify()

def exit_program():
    
    global exit_flag
    exit_flag = True
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Auto Mover")
root.geometry("400x200")
# Use the 'clam' theme for a more modern look (you can try other themes like 'alt', 'default', etc.)
style = ttk.Style()
style.theme_use('clam')

# Create two buttons with some styling
button1 = ttk.Button(root, text="Start the Bot", command=function_one, padding=10)


# Add an Exit button
exit_button = ttk.Button(root, text="Exit", command=exit_program, padding=10, style="Danger.TButton")

# Pack the buttons to display them in the window
button1.pack(pady=5)

exit_button.pack(pady=10)
minimize_button = ttk.Button(root, text="Minimize", command=minimize_window, padding=10)
minimize_button.pack(pady=5)
# Define a custom style for the Exit button (red background and white text)
style.configure("Danger.TButton", background="#FF5733", foreground="white")

# Start the GUI event loop
root.mainloop()


