def read_file(file_name, setting_names, setting_types):
    setting_type = dict(zip(setting_names, setting_types))
    settings = {}
    try:
        with open(file_name, "r") as settings_file:
            lines = settings_file.readlines()
    except FileNotFoundError:
        return settings

    for line in lines:
        setting_name, value = line.split(" ", 1)
        settings[setting_name] = convert(value, setting_type[setting_name])

    return settings


def convert(setting_value, setting_type):
    if setting_type == "int":
        try:
            setting_value = int(setting_value)
        except ValueError:
            print("The value was not a whole number")
            setting_value = None
    if setting_type == "float":
        try:
            setting_value = float(setting_value)
        except ValueError:
            print("The value was not a number")
            setting_value = None

    return setting_value


class Settings:

    def __init__(self, file_name="settings.txt"):
        self.file_name = file_name
        self.settings = []

    def read_settings(self, setting_names, setting_types=[]):
        if not setting_types:
            setting_types = [""] * len(setting_types)

        self.settings = read_file(self.file_name, setting_names, setting_types)

        for setting_name, setting_type in zip(setting_names, setting_types):
            if setting_name not in self.settings.keys():
                setting_value = None
                while not setting_value:
                    question = "Please provide a value for {} ({}): ".format(setting_name, setting_type)
                    setting_value = convert(input(question), setting_type)
                self.settings[setting_name] = setting_value

        self.write_settings()

        return self.settings

    def write_settings(self):
        with open(self.file_name, "w+") as settings_file:
            for setting_name, setting_value in self.settings.items():
                settings_file.write("{} {}\n".format(setting_name, setting_value))

    def get(self, setting_name, alternative=""):
        return self.settings.get(setting_name, alternative)