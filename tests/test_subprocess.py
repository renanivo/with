from unittest import mock

import pytest

from withtool import subprocess


class DescribeExcecute(object):

    def it_executes_the_given_command(self):
        with mock.patch('subprocess.check_call') as mock_check_call:
            subprocess.run('ls')

        assert mock_check_call.called

    def it_catches_every_exception(self):
        with mock.patch('subprocess.check_call') as mock_check_call:
            mock_check_call.side_effect = Exception

            try:
                subprocess.run('ls')
            except Exception as e:
                pytest.fail('It should not have raised: {}'.format(e))
