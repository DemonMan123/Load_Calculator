import customtkinter


class PreStartupPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=430, height=300)

        title = customtkinter.CTkLabel(self, text="Pre Start Checklist", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

        checklist = [
            "Condenser Coolant Pump . A1 [ENABLE]",
            "Condenser Coolant Pump . A2 [ENABLE]",
            "Condenser Coolant Pump . A1 [SPEED 2]",
            "Condenser Coolant Pump . A1 [SPEED 3]",
            "Turbine A-B Bleed Valve [OPEN]",
            "Turbine A Bypass Valve [ENABLE]",
            "Turbine A Bypass Valve [100%] (adjust by holding the knob)",
            "Deaerator A-B Bleed Valve [CLOSE]",
            "Deaerator A Relief Valve [50%]",
            "Deaerator A Steam Inlet Valve [25%]",
            "Recirculation pump A2 [SPEED 2]",
            "Recirculation pump A1 [SPEED 2]",
            "Reactor Isolation Valve Inlet 1, 2 [OPEN]",
            "Reactor Isolation Valve Outlet 1, 2 [OPEN]",
            "Set ECCS Injection Tank1500PSI (toggling Nitrogen valve will fill tank)",
            "SET Automatic Hotwell level [35] (set on numpad and press the grey button)",
            "Automatic Hotwell Limiter Valve [ENABLE]",
            "Breaker 18M-G1",
            "Breaker 64B-M (Key Required)",
            "Automatic G1 Offload [DISABLE]",
            "G1 -64A OFFLOAD SYSTEM [PRIMED]",
            "FEED limiter valve [ENABLE] (located next to feed water pumps)",
            "Pre Start Complete"
        ]

        self.check_states = []

        for i, step in enumerate(checklist, start=1):
            self.check_states.append(False)

            btn = customtkinter.CTkButton(
                self,
                width=25,
                height=25,
                text="",
                corner_radius=2,
                command=lambda idx=i - 1: self.toggle_check(idx)
            )
            btn.grid(row=i, column=0, padx=(10, 5), pady=5, sticky="w")

            label = customtkinter.CTkLabel(self, text=step, anchor="w")
            label.grid(row=i, column=1, padx=5, pady=5, sticky="w")

            self.check_states[i - 1] = {"state": False, "button": btn}

        self.grid_columnconfigure(1, weight=1)

    def toggle_check(self, idx):
        item = self.check_states[idx]
        btn = item["button"]

        if item["state"]:
            btn.configure(text="", fg_color="gray20")
            item["state"] = False
        else:
            btn.configure(text="✔", fg_color="green")
            item["state"] = True
