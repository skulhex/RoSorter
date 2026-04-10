from utility.src.language.text_loader import TextLoader

from utility.src.cli.commands import CliCommands
from utility.src.cli.handlers import CliHandlers

import argparse

class Cli(CliCommands, CliHandlers):
    def __init__(self):
        self.parser = None
        self.lang = TextLoader('commands', logging=True)
        self.code_return = self.lang.code_return

    def main(self):
        self.parser = argparse.ArgumentParser(
            description=self.code_return('help')
        )
        self.commands()