def read_file(file_name):
    settings = {}

    try:
        with open(file_name) as settings_file:
            lines = settings_file.readline()
    except FileNotFoundError:
        return settings

    for line in lines:
        setting_name, setting_value = line.split("", 1)
        settings[setting_name] = setting_value

    return settings

def write_file(settings, file_name):
    with open(file_name, "w+") as settings_file:
        for setting_name, setting_value in settings.items():
            settings_file.write("{} {} \n".format(setting_name,setting_value))


class Settings:
    def __init__(self, file_name="setting.txt"):
        self.file_name = file_name
        self.settings = read_file(file_name)

    def read_settings(self, setting_names):
        for setting_name in setting_names:
            if setting_name not in self.settings.keys():
                setting_value = input("Please give a value for " + setting_name + ": ")
                self.settings[setting_name] = setting_value
        write_file(self.settings, self.file_name)

    def get_value(self, setting):
        return self.settings[setting]