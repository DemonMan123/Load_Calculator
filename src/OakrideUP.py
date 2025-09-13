#Oakridge Utility Program created by Demin

import customtkinter
from src.Panels.CalculatorPanel import CalculatorPanel
from src.Panels.NavPanel import NavPanel
from src.Panels.WelcomePanel import WelcomePanel
from src.Panels.ButtonFunctions import ButtonActions
from src.Panels.PostStartPanel import PostStartPanel
from src.Panels.PreStartupPanel import PreStartupPanel
from src.Panels.ShutdownPanel import ShutdownPanel
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

        #self.Calculatorpan = CalculatorPanel(self)
        self.NavPan = NavPanel(self,
                               on_calculator_click=self.actions.on_calculate_click,
                               on_error_click=self.actions.on_error_events_click,
                               on_startup_click=self.actions.on_startup_click,
                               on_postStart_click=self.actions.on_postStart_click,
                               on_settings_click=self.actions.on_settings_click,
                               on_shutdown_click=self.actions.on_shutdown_click
                               )
        self.NavPan.grid(row=0, column=0, padx=(10,2), pady=10, sticky="nsw")
        #self.welcomePanel = WelcomePanel(self)
        #self.welcomePanel.grid(row=0, column=1,padx=10,pady=10, sticky="nsw")
        #self.welcomePanel.grid_propagate(False)

        self.frames = {}
        self.frames["Welcome"] = WelcomePanel(self)
        self.frames["PostStart"] = PostStartPanel(self)
        self.frames["Startup"] = PreStartupPanel(self)
        self.frames["Shutdown"]= ShutdownPanel(self)
        # Gonna add more to this list as I add more frames

        self.active_frame = ""
        self.ShowActivePanels("Welcome")
    
    def ShowActivePanels(self, name: str):
        if self.active_frame == name:
            # This is to hide the panel and bring the Welcome panel back
            self.frames[name].grid_forget()
            self.frames["Welcome"].grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
            self.frames["Welcome"].grid_propagate(False)
            self.active_frame = None
        else:
            # This hides the welcome frame when any other frame is clicked, I'm sure there's a better way to do this.
            for frame in self.frames.values():
                frame.grid_forget()

            shownFrame = self.frames[name]
            shownFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")
            self.active_frame = name

if __name__ == "__main__":
    app = App()
    app.mainloop()