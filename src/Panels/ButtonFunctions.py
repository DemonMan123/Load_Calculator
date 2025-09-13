class ButtonActions:
    def __init__(self, app):
        self.app = app  

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

    def on_startup_click(self):
        self.app.ShowActivePanels("Startup")

    def on_shutdown_click(self):
        self.app.ShowActivePanels("Shutdown")

    def on_postStart_click(self):
        self.app.ShowActivePanels("PostStart")

    def on_error_events_click(self):
        print("Error events button clicked!")

    def on_settings_click(self):
        print("Settings button clicked!")
