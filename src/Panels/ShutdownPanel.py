import customtkinter

class ShutdownPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=430)

        Label = customtkinter.CTkLabel(self, text="Shutdown Panel Placeholder")
        Label.grid(row=0, column=0, padx=150, pady=10, sticky="nsew")