import customtkinter
#from src.Panels.CalculatorPanel import CalculatorPanel
from Panels.CalculatorPanel import CalculatorPanel
from Panels.NavPanel import NavPanel
from Panels.InfoPanel import InfoPanel
#Oakridge Utility Program

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Oakridge Utility Program")
        self.geometry(f"{650}x{400}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        customtkinter.set_appearance_mode("dark")
        self.resizable(False,False)

        self.Calculatorpan = CalculatorPanel(self)
        self.NavPan = NavPanel(self)
        self.NavPan.grid(row=0, column=0, padx=(10,2), pady=10, sticky="nsw")
        self.MainPanel = InfoPanel(self)
        self.MainPanel.grid(row=0, column=1, padx=(0,10), pady=10, sticky="nsew")

    def on_calculate_click(self):
        demand = 2000
        result = self.CalculateFunction(demand)
        print(f"Input {result} for each turbine.")

    def CalculateFunction(self, demand: float):
        try:
            PowerPerTurbine = (demand / 2) + 12
            return PowerPerTurbine
        except TypeError:
            print("Works")

if __name__ == "__main__":
    app = App()
    app.mainloop()