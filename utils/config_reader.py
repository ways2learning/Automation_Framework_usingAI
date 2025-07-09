import yaml
import os

class ConfigReader:
    def __init__(self, env=None):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)

        self.env = env or config_data.get("env", "qa")
        self.env_config = config_data["environments"][self.env]

    def get_base_url(self):
        return self.env_config.get("base_url")

    def get_api_url(self):
        return self.env_config.get("api_url")

    def get_db_config(self):
        return self.env_config.get("db", {})