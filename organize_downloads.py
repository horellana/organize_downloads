#!/usr/bin/env python

import sys
from pathlib import Path

class UnknownSuffix(Exception):
    pass

config = {
    'powerpoint': ['.ppt', '.pptx'],
    'images': ['png', 'jpg', 'jpeg'],
    'archives': ['.zip', '.rar', '.tar.gz'],
    'documents': ['.pdf', '.djvu' , '.doc', '.docx']
}

def get_folder(ext, config):
    for folder, extension in config.items():
        if ext in extension:
            return folder
    raise UnknownSuffix('Unkown suffix: {}\n'.format(ext))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.stderr.write('Usage: organize_downloads.py path\n')
        sys.exit(1)

    root = Path(sys.argv[1])
    files = (Path(path) for path in root.iterdir() if path.is_file())
    
    for file in files:
        try:
            suffix = file.suffix
            root = file.parents[0]
            folder = get_folder(suffix, config)
            
            sys.stdout.write('{file} => Moving: {root}/{folder}/{name}\n'
                             .format(file=file,
                                     root=file.parents[0],
                                     folder=folder,
                                     name=file.name))
        
            file.rename('{root}/{folder}/{file}'.format(root=file.parents[0],
                                                        folder=folder,
                                                        file=file.name))
        except UnknownSuffix as err:
            sys.stderr.write('{} => '.format(file.as_posix()))
            sys.stderr.write('Error: {}'.format(err))
