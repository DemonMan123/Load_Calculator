import customtkinter

class InfoPanel(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master,corner_radius=0)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        self.WelcomeText = customtkinter.CTkLabel(self, text="3333333333333333333333Welcome to the OakRidge Utility Program!")
        self.WelcomeText.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")