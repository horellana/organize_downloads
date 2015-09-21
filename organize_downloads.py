#!/usr/bin/env python

import sys
from pathlib import Path

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
    raise Exception('Unkown suffix: {}'.format(ext))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.stderr.write('Usage: organize_downloads.py path\n')
        sys.exit(1)

    root = Path(sys.argv[1])
    files = (Path(path) for path in root.iterdir() if path.is_file())
    
    for file in files:
        suffix = file.suffix
        folder = get_folder(suffix, config)
        file.rename('{root}/{folder}/{file}'.format(root=file.parents[0],
                                                    folder=folder,
                                                    file=file.name))
