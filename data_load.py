class ConfigFile:
    def __init__(self):
        self.system_theme = "blue"  # blue / green / dark-blue
        self.system_scale = "100%"
        self.system_appearance = "System"
        self.start_up_x = 200
        self.start_up_y = 150

    def load_default(self):
        config_file = open("config_data/config.txt", "r")
        config_file_data = config_file.read()
        config_file.close()
        config_file_data = config_file_data.split("\n")
        data = []
        for i in range(0, len(config_file_data)):
            data.append(config_file_data[i].split(":"))
        self.system_theme = data[0][1]
        self.system_scale = data[1][1]
        self.system_appearance = data[2][1]
        self.start_up_x = data[3][1]
        self.start_up_y = data[4][1]
