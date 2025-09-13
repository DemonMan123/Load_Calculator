import customtkinter

class ShutdownPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=430, height=300)

        title = customtkinter.CTkLabel(self, text="Shutdown Checklist", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

        # Full shutdown checklist with sub-steps indicated by '*'
        checklist = [
            "1. Call Grid Controller and click Go Offline.",
            "2. Reduce Reactor Power:\n   * Enter 3400 into Auto Control Rods keypad\n   * Insert control rods symmetrically\n   * Avoid rapid power reduction",
            "3. Deaerator Configuration:\n   * Disable Deaerator Auto Control\n   * Set Deaerator Inlets A & B to 0%\n   * Set Deaerator Outlets A & B to 50%",
            "4. Condenser & Pumps:\n   * Stop Condenser Coolant Pumps A1 & A2\n   * Stop Main Circulation Pumps A1 & A2",
            "5. Turbines:\n   * Shut down Turbine A and Turbine B\n   * Verify Turning Gear is engaged",
            "6. Feedwater & Recirculation:\n   * Disable Feedwater Pump 1 & 2\n   * Disable Recirculation Pumps A1 & A2",
            "7. Cooling Systems:\n   * Stop Condensate Pump 1 & 2\n   * Verify Heat Exchangers are closed",
            "8. Control Rods:\n   * Enable Shutdown Control Rods\n   * Press Reset button on Middle Reactor Console\n   * Wait for Out-of-Zone panel to flash and bell to ring",
            "9. Auto Control Rods:\n   * Disable Auto Control Rods",
            "10. Breakers & Alarms:\n   * Acknowledge any active alarms\n   * Reset any active Breakers (18M-G1, 64B-M, etc.)",
            "11. Bypass Valves:\n   * Close Bypass valves A & B\n   * Disable Auto Bypass valves",
            "12. Final Steps:\n   * Verify reactor is at safe shutdown state\n   * Ensure all systems are in proper shutdown configuration\n   * Document completion in Control Room log"
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
            label = customtkinter.CTkLabel(
                self,
                text=step,
                anchor="w",
                wraplength=380
            )
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
