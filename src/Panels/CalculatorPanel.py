import customtkinter

class CalculatorPanel(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=180,
            height=160,
            corner_radius=20,
            fg_color="#2b2b2b"
        )

        label = customtkinter.CTkLabel(self, text="Calculator Panel")
        label.place(relx=0.5, rely=0.5, anchor="center")