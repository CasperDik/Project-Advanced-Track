from chapter_12.Settings.Settings import Settings

settings = Settings("test_settings.txt")
settings.read_settings(["1","2","3"])
settings.get_value()
