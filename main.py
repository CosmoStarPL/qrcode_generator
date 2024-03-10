from tkinter import Tk, ttk

root = Tk()

root.title("QR-code Generator")
root.iconbitmap("assets/app_icon.ico")
root.geometry("350x500")
root.configure(bg='#253547')

label = ttk.Label(root, text="Enter text or link", font=("Manrope", 20), padding=8, foreground="#62A7F4",
                  background="#253547")
label.pack()

root.mainloop()
