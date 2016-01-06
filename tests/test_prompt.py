import os
from shutil import rmtree

import pytest
from withtool import prompt
from prompt_toolkit.history import History


class DescribeGetHistory(object):

    @pytest.fixture
    def history_dir(self):
        return '/tmp/history'

    @pytest.fixture
    def command(self):
        return 'cat'

    def setup(self):
        os.mkdir(self.history_dir())

    def teardown(self):
        rmtree(self.history_dir())

    def it_creates_the_history_file_when_not_found(
        self,
        history_dir,
        command
    ):
        history = prompt.get_history(history_dir, command)
        os.path.isfile(history.filename)

    def it_returns_a_prompt_toolkit_history(
        self,
        history_dir,
        command
    ):
        history = prompt.get_history(history_dir, command)
        assert isinstance(history, History)
