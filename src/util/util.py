def get_files(_format, _files):
    return filter(lambda f: f.split('.')[-1] in _format, _files)
