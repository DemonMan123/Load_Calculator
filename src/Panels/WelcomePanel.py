import customtkinter
import webbrowser

class WelcomePanel(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=450)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_propagate(False)

        self.title = customtkinter.CTkLabel(self, text="Welcome to the OakRidge Utility Program!", font=("Arial", 18, "bold"))
        self.title.grid(row=0, column=0, pady=(10, 20), sticky="n")

        # Yes, I did this again.
        self.Separator = customtkinter.CTkFrame(self, height=2, fg_color="gray")
        self.Separator.grid(row=1, column=0, padx=20, pady=0, sticky="ew")

        self.GithubTitle = customtkinter.CTkLabel(self, text="Follow my project on GitHub:", font=("Arial", 12, "bold"), anchor="center")
        self.GithubTitle.grid(row=2, column=0, pady=(10, 0), sticky="n", padx=20)

        self.GithubLink = customtkinter.CTkLabel(self, text="https://github.com/DemonMan123/Oakridge-Utility-Program", font=("Arial", 11), text_color="blue", cursor="hand2", anchor="center")
        self.GithubLink.grid(row=3, column=0, sticky="n", padx=20)
        self.GithubLink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/DemonMan123/Oakridge-Utility-Program"))

        self.DiscordTitle = customtkinter.CTkLabel(self, text="Add me on Discord for help or suggestions:", font=("Arial", 12, "bold"), anchor="center")
        self.DiscordTitle.grid(row=4, column=0, pady=(10, 0), sticky="n", padx=20)

        self.DiscordInfo = customtkinter.CTkLabel(self, text="Demin_Denim", font=("Arial", 11), anchor="center")
        self.DiscordInfo.grid(row=5, column=0, sticky="n", padx=20)
