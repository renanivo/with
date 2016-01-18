import os
import types
from unittest import mock
from shutil import rmtree

import pytest
from withtool import prompt
from prompt_toolkit.history import History


class DescribeGetPrompt(object):

    def it_returns_a_generator(self):
        result = prompt.get_prompt('cmd')
        assert isinstance(result, types.GeneratorType)

    @pytest.mark.asyncio
    def it_calls_an_async_prompt(self):
        with mock.patch('withtool.prompt.prompt_async') as mock_prompt_async:
            yield from prompt.get_prompt('cmd')

        assert mock_prompt_async.called

    @pytest.mark.asyncio
    def it_exits_on_EOFError(self):
        with mock.patch('withtool.prompt.prompt_async') as mock_prompt_async:
            mock_prompt_async.side_effect = EOFError

            with pytest.raises(SystemExit):
                yield from prompt.get_prompt('cmd')


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
