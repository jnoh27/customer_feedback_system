import tkinter as tk
import customtkinter as ctk

# from tkinter import ttk

# window
window = ctk.CTk()
window.title("Customer Feedback Form")
window.geometry("500x500")

ctk.set_appearance_mode("dark")

def convert():
    print(entry_int.get())
    output_string.set("test")


# title
title_font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")
title_label = ctk.CTkLabel(master=window, text="Customer Feedback", font=title_font, text_color="#FFFFFF")
title_label.pack(pady=10)

# create account



# login

# run
window.mainloop()
