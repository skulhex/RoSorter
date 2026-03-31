from src.language.text_loader import TextLoader

from cli.commands import CliCommands
from cli.handlers import CliHandlers

import argparse

class Cli(CliCommands, CliHandlers):
    def __init__(self):
        self.lang = TextLoader('commands', logging=True)
        self.code_return = self.lang.code_return

    def main(self):
        self.parser = argparse.ArgumentParser(
            description=self.code_return('help')
        )
        self.commands()