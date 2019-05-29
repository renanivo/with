import os
import types
from shutil import rmtree
from unittest import mock

import pytest
from prompt_toolkit.history import History

from withtool import prompt


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
    def it_exits_on_EOF_error(self):
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

    @pytest.fixture(autouse=True)
    def setup_history_dir(self, history_dir):
        os.mkdir(history_dir)
        yield
        rmtree(history_dir)

    def it_creates_the_history_file_when_not_found(
        self,
        history_dir,
        command
    ):
        history = prompt.get_history(history_dir, command)
        assert os.path.isfile(history.filename)

    def it_returns_a_prompt_toolkit_history(
        self,
        history_dir,
        command
    ):
        history = prompt.get_history(history_dir, command)
        assert isinstance(history, History)

    def it_removes_invalid_filename_characters_from_command(
        self,
        history_dir
    ):
        history = prompt.get_history(history_dir, '*/ -s ^^')
        assert os.path.isfile(history.filename)
