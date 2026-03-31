class Applyes:
    def apply_ignore(self, ignore, content_folder, catalog):
        if ignore != None:
            self.printf('found_ignore', catalog)
            for name, file_extension in content_folder:
                if name + file_extension in ignore:
                    self.printf('delete_ignore', name + file_extension)
                    content_folder.remove((name, file_extension))
                    self.printf('deleted_ignore', name + file_extension)
        return content_folder

    def apply_names(self, names, content_folder):
        if names != None:
            for filename, fil in content_folder:
                if any(filename in n for n in names):
                    content_folder.remove((filename, fil))
        return content_folder