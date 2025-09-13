import customtkinter


class NavPanel(customtkinter.CTkFrame):
    def __init__(self, master,
                 on_calculator_click=None,
                 on_startup_click=None,
                 on_postStart_click=None,
                 on_shutdown_click=None,
                 on_error_click=None,
                 on_settings_click=None
                 ):
        super().__init__(master)

        # Without using the ttk library, this was my solution to make a line.
        self.separator = customtkinter.CTkFrame(self, width=5, height=2, fg_color="gray")
        #separator.grid(row=0,column=0,padx=(10,10),pady=10,sticky='nsew')

        self.VersionText = customtkinter.CTkLabel(self, text="Oakridge Utility Program\n\nCreated by Demin")
        self.VersionText.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.separator.grid(row=1,column=0,padx=(10,10),pady=5,sticky='nsew')
        self.PreStartupChklstButton = customtkinter.CTkButton(self, text="Pre Start checklist",command=on_startup_click)
        self.PreStartupChklstButton.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.PostStartChklstButton = customtkinter.CTkButton(self, text="Post Start Checklist", command=on_postStart_click)
        self.PostStartChklstButton.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.ShutdownChecklist = customtkinter.CTkButton(self, text="Shutdown Checklist", command=on_shutdown_click)
        self.ShutdownChecklist.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.ErrorEvents = customtkinter.CTkButton(self, text="Error Events", command=on_error_click)
        self.ErrorEvents.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.CalculatorButton = customtkinter.CTkButton(self, text="Calculator", command=on_calculator_click)
        self.CalculatorButton.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.settingsButton = customtkinter.CTkButton(self, text="Settings", command=on_settings_click)
        self.settingsButton.grid(row=7, column=0, padx=10, pady=10, sticky="w")