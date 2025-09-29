import tkinter as tk                                      # import the tkinter library

def say_hello(lang):
    greetings = {                                        # map each language to its greeting
        "English": "Hello",
        "Spanish": "Hola",
        "French":  "Bonjour",
        "Dutch":   "Hallo"
    }
    
    output_label.config(text=greetings.get(lang, "Hello"))  # update the label with the right greeting

root = tk.Tk()                                           # create the main application window
root.title("Greeting Translator")                               # set the window’s title
root.geometry("550x240")                                # size: 400px wide by 120px tall

button_frame = tk.Frame(root)                           # a container to hold all four buttons
button_frame.pack(pady=10)                              # pack it with 10px vertical padding

# create one button per language and pack them side by side
for lang in ["English", "Spanish", "French", "Dutch"]:
    btn = tk.Button(
        button_frame,
        text=lang,                                       # button text shows the language
        width=8,                                         # fixed button width
        command=lambda l=lang: say_hello(l)              # call say_hello(lang) when clicked
    )
    #btn.pack(side="left", padx=5)                        # pack left-to-right with 5px spacing
    #this line was making them side by side

    btn.pack(padx=4, pady=4)   
    #this is just the "padding" x,y axis

output_label = tk.Label(root, text="", font=("Arial", 14))  # label to display the greeting
output_label.pack()                                       # pack it below the buttons

root.mainloop()                                          # start the GUI event loop