import os
from shutil import rmtree

from withtool.config import get_config


class DescribeGetConfig(object):

    def teardown(self):
        config = get_config()
        rmtree(config['history_dir'])

    def it_returns_a_dict(self):
        config = get_config()
        assert isinstance(config, dict)

    def it_returns_a_dict_with_the_history_dir(self):
        config = get_config()
        assert 'history_dir' in config

    def it_creates_the_history_dir_when_does_not_exists(self):
        config = get_config()
        assert os.path.isdir(
            config['history_dir']
        )
