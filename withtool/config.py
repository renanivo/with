import os


def get_config():
    config = {
        'history_dir': '/tmp/history',
    }

    if not os.path.isdir(config['history_dir']):
        os.mkdir(config['history_dir'])

    return config
