import os

from appdirs import AppDirs


def get_config():
    app_dirs = AppDirs(appname='with', appauthor='Renan Ivo')

    config = {
        'history_dir': os.path.join(app_dirs.user_cache_dir, 'history'),
    }

    if not os.path.isdir(config['history_dir']):
        os.makedirs(config['history_dir'])

    return config
