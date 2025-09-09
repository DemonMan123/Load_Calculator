import customtkinter

class NavPanel(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.CalculatorButton = customtkinter.CTkButton(self, text="Calculator")
        self.CalculatorButton.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.StartupChklstButton = customtkinter.CTkButton(self, text="Startup checklist")
        self.StartupChklstButton.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.PostStartChklstButton = customtkinter.CTkButton(self, text="Post Start Checklist")
        self.PostStartChklstButton.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.ShutdownChecklist = customtkinter.CTkButton(self, text="Shutdown Checklist")
        self.ShutdownChecklist.grid(row=3, column=0, padx=10, pady=10, sticky="W")
        self.ErrorEvents = customtkinter.CTkButton(self, text="Error Events")
        self.ErrorEvents.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.settingsButton = customtkinter.CTkButton(self, text="Settings")
        self.settingsButton.grid(row=5, column=0, padx=10, pady=10, sticky="w")