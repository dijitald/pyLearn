import tkinter as tk

def submit():
    pass
    # Function to handle form submission
    # Add your code here

window = tk.Tk()
window.title("My Form")
window.minsize(500, 300)

# Create form elements
label = tk.Label(window, text="Enter your name:", font=("Arial", 16, "bold"))
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=submit)
button.pack()

# Start the main event loop
window.mainloop()