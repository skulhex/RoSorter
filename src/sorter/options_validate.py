import sys

class optionsValidate:
    def validate_options(self, catalog):
        options = {'path': True, 'files': True, 'names': False, 'ignore': False}
        added_opts = []
        for option, needed in options.items():
            if option not in self.catalogs[catalog]:
                if needed == False:
                    continue
                else:
                    self.printf('missing_option', option)
                    sys.exit()
            elif needed == False:
                added_opts.append(option)
        path_file = self.catalogs[catalog]['path']
        files = self.catalogs[catalog]['files']
        names = self.catalogs[catalog]['names'] if 'names' in added_opts else None
        ignore = self.catalogs[catalog]['ignore'] if 'ignore' in added_opts else None

        names1 = []
        for el in names:
            for key, value in el.items():
                names1.append([key, value])
        
        return path_file, files, ignore, names1