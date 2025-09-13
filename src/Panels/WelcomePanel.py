import customtkinter
from tkinter import ttk

class WelcomePanel(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master,width=453)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_propagate(False)

        self.WelcomeText = customtkinter.CTkLabel(self, text="Welcome to the OakRidge Utility Program!")
        self.WelcomeText.grid(row=0, column=0, padx=110, pady=10, sticky="nsew")
        self.Separator = ttk.Separator(self)
        self.Separator.grid(row=1,column=0,padx=110,pady=0,sticky='nsew')
        self.GithubText = customtkinter.CTkLabel(self, text="\nFollow my project on Github! Link below:\n" \
        "https://github.com/DemonMan123/Oakridge-Utility-Program")
        self.GithubText.grid(row=2, column=0, padx=0, pady=5, sticky="nsew")
        self.DiscordText = customtkinter.CTkLabel(self, text="Add me on Discord if you have any problems: Demin_Denim")
        self.DiscordText.grid(row=3, column=0, padx=0, pady=5, sticky="nsew")