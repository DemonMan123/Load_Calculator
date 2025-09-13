import customtkinter


class PostStartPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=430, height=300)

        title = customtkinter.CTkLabel(self, text="Post Startup Checklist", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

        startup_checklist = [
            "1. Retrieve bypass key from Control Room cabinet",
            "2. Insert key into Autoscram panel and disable Autoscram",
            "3. Enable Reactor Mode 1",
            "4. Close Heat Exchanger A & B",
            "5. Disable OCC Circulation Pumps 1 & 2",
            "6. Acknowledge Mode Conflict alarm on Reactor Console",
            "7. Enable Shutdown Control Rods",
            "8. Press Reset next to acknowledge button on Reactor Console",
            "9. Wait for Out of Zone panel flash and bell (Shutdown Rods removed)",
            "10. Enable Auto Control Rods",
            "11. Set Auto Control Rods to 1500 MW via keypad",
            "12. Enable Reactor Mode 2 and monitor Core Heat Distribution",
            "13. Enable Feedwater Pump 1 (speed 2)",
            "14. Enable Condensate Pump 1 (speed 2)",
            "15. Call Engineering, disengage Turbine A Turning Gear",
            "16. Enable Synchronoscope for Turbine A",
            "17. Reduce Turbine A bypass valve to 20-30%",
            "18. Increase Turbine Valve to 60-70%",
            "19. Monitor RPM (+30 per update)",
            "20. Open Grid Sync cap",
            "21. Wait for RPM ~1775, stabilize at 1800, click Grid Sync",
            "22. If sync fails: acknowledge alarm, reset, retry",
            "23. If sync succeeds: acknowledge Reverse Power, adjust Turbine A valves, reset, enable Breaker 64 A-M, reset breakers",
            "24. Set Deaerator A & B Relief Valves to 25%",
            "25. Set Deaerator A & B Inlet Valves to 45%",
            "26. Enable Condensate Pump 2",
            "27. Enable Feedwater Pump 2",
            "28. Open Deaerator A-B Bleed Valve",
            "29. Set Main Circulation Pumps A1 & A2 to speed 3",
            "30. Enable Main Circulation Pumps B1 & B2",
            "31. Set Condenser Coolant Pumps A1 & A2 to speed 3",
            "32. Set Auto Control Rods to 3000 MW, monitor Core Heat Distribution",
            "33. Enable Condenser Coolant Pumps B1 & B2 to speed 3",
            "34. Disengage Turbine B Turning Gear",
            "35. Enable Synchronoscope for Turbine B",
            "36. Reduce Turbine B bypass valve to 20-30%",
            "37. Increase Turbine Valve to 60-70%",
            "38. Monitor RPM and open Grid Sync cap",
            "39. Wait for RPM ~1775, stabilize at 1800, click Grid Sync",
            "40. If sync fails: acknowledge alarm, reset, retry",
            "41. If sync succeeds: acknowledge Reverse Power, adjust Turbine B valves, reset, enable Feedwater & Condensate Pump 2 speed 2",
            "42. Set Auto Control Rods to 4000 MW via keypad",
            "43. Set Main Circulation Pumps B1 & B2 to speed 3",
            "44. Enable Condenser Coolant Pumps A3 & B3",
            "45. Call Grid Controller and click Go Online",
            "46. Enable Bypass valves A & B",
            "47. Enable Auto Bypass Valves A & B"
        ]



        self.check_states = []

        for i, step in enumerate(startup_checklist, start=1):
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

            label = customtkinter.CTkLabel(self, text=step, anchor="w", wraplength=380)
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
