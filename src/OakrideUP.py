import customtkinter
from src.Panels.CalculatorPanel import CalculatorPanel
#Oakridge Utility Program

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Oakridge Utility Program")
        self.geometry(f"{300}x{200}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        customtkinter.set_appearance_mode("dark")
        self.resizable(False,False)

        self.Calculatorpan = CalculatorPanel(self)

        self.Calculate = customtkinter.CTkButton(master=self, text="Calculate", command=self.on_calculate_click)
        self.Calculate.grid(row=1, column=1)

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
