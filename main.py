import customtkinter as ctk
from data_load import ConfigFile

system_data = ConfigFile()
system_data.load_default()

ctk.set_appearance_mode(system_data.system_appearance)    # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme(system_data.system_theme)  # Themes: "blue" (standard), "green", "dark-blue"
project_center = ctk.CTk()
project_center.geometry(f"{system_data.start_up_x}x{system_data.start_up_y}")
project_center.title("Project Center")

FONT_TITLE_BIG = ctk.CTkFont(size=25, weight="bold")
FONT_TITLE_NORMAL = ctk.CTkFont(size=20, weight="bold")
FONT_LABEL = ctk.CTkFont(size=10, weight="bold")
FONT_BUTTON = ctk.CTkFont(size=15, weight="bold")

# ----------------------------------------------------------------------------------------------------------------------
# Side Bar
side_bar = ctk.CTkFrame(master=project_center, width=120, height=400)
side_bar.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

side_bar_new_project_button = ctk.CTkButton(master=side_bar,
                                            text="New Project",
                                            font=FONT_BUTTON)
side_bar_new_project_button.pack(padx=5, pady=10)

side_bar_settings_button = ctk.CTkButton(master=side_bar,
                                         text="Settings",
                                         font=FONT_BUTTON)
side_bar_settings_button.pack(padx=5, pady=10)


# Main Body
main_body = ctk.CTkFrame(master=project_center, width=(120-int(system_data.start_up_x)))
main_body.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
main_body_title = ctk.CTkLabel(master=main_body,
                               text="Projects",
                               font=FONT_TITLE_BIG)
main_body_title.pack(padx=5, pady=5)

main_projects_frame = ctk.CTkFrame(master=main_body)
main_projects_frame.pack(padx=0, pady=5)





# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    project_center.mainloop()
