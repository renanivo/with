import os
from shutil import rmtree

import pytest
from appdirs import AppDirs

from withtool.config import get_config


class DescribeGetConfig(object):

    @pytest.fixture
    def app_dirs(self):
        return AppDirs(appname='with', appauthor='Renan Ivo')

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

    def it_puts_the_history_in_users_cache_dir(self, app_dirs):
        config = get_config()
        assert app_dirs.user_cache_dir in config['history_dir']
