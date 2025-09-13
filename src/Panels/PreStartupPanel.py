import customtkinter


class PreStartupPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=430, height=300)

        title = customtkinter.CTkLabel(self, text="Pre Start Checklist", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

        checklist = [
            "1. Grab Key",
            "2. Condenser Coolant Pump A1 [ENABLE]",
            "3. Condenser Coolant Pump A2 [ENABLE]",
            "4. Condenser Coolant Pump A1 [SPEED 2]",
            "5. Condenser Coolant Pump A1 [SPEED 3]",
            "6. Turbine A-B Bleed Valve [OPEN]",
            "7. Turbine A Bypass Valve [ENABLE]",
            "8. Turbine A Bypass Valve [100%] (adjust by holding the knob)",
            "9. Deaerator A-B Bleed Valve [CLOSE]",
            "10. Deaerator A Relief Valve [50%]",
            "11. Deaerator A Steam Inlet Valve [25%]",
            "12. Recirculation Pump A2 [SPEED 2]",
            "13. Recirculation Pump A1 [SPEED 2]",
            "14. Reactor Isolation Valve Inlet 1,2 [OPEN]",
            "15. Reactor Isolation Valve Outlet 1,2 [OPEN]",
            "16. Set ECCS Injection Tank 1500PSI (toggling Nitrogen valve will fill tank)",
            "17. SET Automatic Hotwell level [35] (set on numpad and press grey button)",
            "18. Automatic Hotwell Limiter Valve [ENABLE]",
            "19. Breaker 18M-G1",
            "20. Breaker 64B-M (Key Required)",
            "21. Automatic G1 Offload [DISABLE]",
            "22. G1-64A OFFLOAD SYSTEM [PRIMED]",
            "23. FEED limiter valve [ENABLE] (located next to feed water pumps)",
            "24. Pre Start Complete"
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
            label.grid(row=i, column=1, padx=5, pady=10, sticky="w")

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
