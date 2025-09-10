#Oakridge Utility Program created by Demin

import customtkinter
from src.Panels.CalculatorPanel import CalculatorPanel
from src.Panels.NavPanel import NavPanel
from src.Panels.InfoPanel import InfoPanel
from src.Panels.ButtonFunctions import ButtonActions
'''
from Panels.CalculatorPanel import CalculatorPanel
from Panels.NavPanel import NavPanel
from Panels.InfoPanel import InfoPanel
'''
iconPhoto = r"src\Images\kyotdigital.ico"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Oakridge Utility Program")
        self.iconbitmap(iconPhoto)
        self.geometry(f"{650}x{400}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        customtkinter.set_appearance_mode("dark")
        self.resizable(False,False)

        self.actions = ButtonActions(self)

        self.Calculatorpan = CalculatorPanel(self)
        self.NavPan = NavPanel(self,
                               on_calculator_click=self.actions.on_calculate_click,
                               on_error_click=self.actions.on_error_events_click,
                               on_startup_click=self.actions.on_startup_click,
                               on_postStart_click=self.actions.on_postStart_click,
                               on_settings_click=self.actions.on_settings_click,
                               on_shutdown_click=self.actions.on_shutdown_click
                               )
        self.NavPan.grid(row=0, column=0, padx=(10,2), pady=10, sticky="nsw")
        self.MainPanel = InfoPanel(self)
        self.MainPanel.grid(row=0, column=1,padx=10,pady=10, sticky="nsw")
        self.MainPanel.grid_propagate(False)


if __name__ == "__main__":
    app = App()
    app.mainloop()