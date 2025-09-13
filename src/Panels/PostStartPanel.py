import customtkinter


class PostStartPanel(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=430, height=300)

        title = customtkinter.CTkLabel(self, text="Post Startup Checklist", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

        checklist = [
            "Placeholder 1",
            "Placeholder 2",
            "Placeholder 3",
            "Placeholder 4",
            "Placeholder 5",
            "Placeholder 6",
            "Placeholder 7",
            "Placeholder 8",
            "Placeholder 9",
            "Placeholder 10"
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
