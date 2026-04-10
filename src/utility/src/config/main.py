from utility.src.config.config import ValidateFileConfig
from utility.src.config.validates import ConfigOptionValidate

from utility.src.language.text_loader import TextLoader

import yaml

class Config(ValidateFileConfig, ConfigOptionValidate):
    def __init__(self, language, custom_config=None):
        self.language = language
        lang = TextLoader(language)
        self.printf = lang.printf
        self.inputf = lang.inputf

        self.custom_config = custom_config
        self.setup_paths(custom_config)

    def main(self):
        catalogs = {}
        settings = {}
        with open(self.configuration, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

            self.contains_values(config)
            settings = self.validate_settings(config, settings)
            catalogs = self.validate_directories(config, catalogs)
            self.validate_catalogs(catalogs)

        language = 'en-US' if not self.language in settings else self.language
        return catalogs, settings, language
                
    def run(self):
        if not self.custom_config is None:
            self.validate_config()
        catalogs, settings, language = self.main()
        return catalogs, settings, language