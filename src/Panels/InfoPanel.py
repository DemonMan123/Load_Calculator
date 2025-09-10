import customtkinter
from tkinter import ttk

class InfoPanel(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master,width=450)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        self.WelcomeText = customtkinter.CTkLabel(self, text="Welcome to the OakRidge Utility Program!")
        self.WelcomeText.grid(row=0, column=0, padx=110, pady=10, sticky="nsew")
        self.Separator = ttk.Separator(self)
        self.Separator.grid(row=1,column=0,padx=110,pady=0,sticky='nsew')