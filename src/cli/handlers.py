from src.sorter.main import Sorter
from src.config.main import Config

from pathlib import Path

class CliHandlers:
    def sort(self, args):
        conf = Config('en-US', custom_config=args.config) if args.config else Config('en-US')
        catalogs, settings, language = conf.run()
        
        sort = Sorter(catalogs, settings, language)
        sort.main('nt')

        self.lang.save_log(Path('C:\\Users') / 'sophrosha\\Documents\\Projects\\RoSorter-1')

    def gui(self, args):
        print('Under Construction')

    def create(self, args):
        print('Under Construction')