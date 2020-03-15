from configparser import ConfigParser


def init():
    config = ConfigParser(allow_no_value=True)
    config.read("socli/cli_setup/socless.ini")

    socless_config_data = {"repos": {}}
    for section in config.sections():
        for key in config[section]:
            socless_config_data["repos"][key] = f"https://{section}/{key}"

    return socless_config_data
