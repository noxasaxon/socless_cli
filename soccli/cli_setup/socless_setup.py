from configparser import ConfigParser
from pprint import pprint

def init():
    config = ConfigParser(allow_no_value=True)
    config.read("cli_setup/socless.ini")
    
    socless_config_data = {
        "repos" : {}
    }
    for section in config.sections():
        for key in config[section]:
            socless_config_data["repos"][key] = f"https://{section}/{key}"
    
    pprint(socless_config_data["repos"])
    return socless_config_data
