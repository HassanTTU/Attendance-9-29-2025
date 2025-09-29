import tkinter as tk

def greet():
    name = entry.get().strip()
    if name:
        output_label.config(text=f"Hello, {name}!")
    else:
        output_label.config(text="Please enter your name.")

# 1. Main window setup
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x120")

# 2. Prompt and input field
tk.Label(root, text="Enter your name:").pack(pady=(10, 0))
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# 3. Button to trigger greeting
tk.Button(root, text="Greet Me", command=greet).pack(pady=5)

# 4. Label to display the result
output_label = tk.Label(root, text="")
output_label.pack(pady=(5, 0))

# 5. Start the GUI event loop
root.mainloop()


'''

Comments explaining each line:
- import tkinter as tk
Imports the Tkinter library so you can create windows and widgets; aliases it to tk for shorter references.

- def greet():
Defines the greet function, which is called when the button is clicked.

- name = entry.get().strip()
Reads the text typed into the entry widget and removes any extra spaces at the start or end.

- if name:
Checks whether the user actually entered something (non-empty string).

- output_label.config(text=f"Hello, {name}!")
If there’s input, updates the label’s text to greet the user by name.

- else:
Starts the branch for when the entry is empty.

- output_label.config(text="Please enter your name.")
If no name was entered, updates the label to prompt the user to type something.

- root = tk.Tk()
Creates the main application window object where all widgets live.

- root.title("Greeting App")
Sets the text shown in the window’s title bar.

- root.geometry("300x120")
Fixes the window’s size to 300 pixels wide by 120 pixels tall.

- tk.Label(root, text="Enter your name:").pack(pady=(10, 0))
Creates a label prompting the user, then places it with 10px top padding so it’s not jammed against the window edge.

- entry = tk.Entry(root, width=30)
Creates a single-line text box 30 characters wide for user input.

- entry.pack(pady=5)
Places the entry widget with 5 pixels of vertical space around it.

- tk.Button(root, text="Greet Me", command=greet).pack(pady=5)
Creates a button labeled “Greet Me” that calls greet() when clicked, then packs it with padding.

- output_label = tk.Label(root, text="")
Defines an initially blank label where the greeting or error message will appear.

- output_label.pack(pady=(5, 0))
Places the output label with 5px of top padding to separate it from the button.

- root.mainloop()
Starts Tkinter’s event loop, which keeps the window open and listens for clicks and key presses until the user closes it.

'''