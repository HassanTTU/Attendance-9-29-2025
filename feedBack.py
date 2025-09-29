import tkinter as tk

def submit_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    message = message_text.get("1.0", tk.END).strip()
    print("Feedback received:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x300")

tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=(10, 0))
name_entry = tk.Entry(root, width=50)
name_entry.pack(padx=10, pady=5)

tk.Label(root, text="Email:").pack(anchor="w", padx=10, pady=(10, 0))
email_entry = tk.Entry(root, width=50)
email_entry.pack(padx=10, pady=5)

tk.Label(root, text="Message:").pack(anchor="w", padx=10, pady=(10, 0))
message_text = tk.Text(root, width=50, height=5)
message_text.pack(padx=10, pady=5)

tk.Button(root, text="Submit", command=submit_feedback).pack(pady=10)

root.mainloop()
