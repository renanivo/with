import re
import sys
from unittest import mock

import pytest

from withtool.main import main


class DescribeMain(object):

    @pytest.mark.asyncio
    def it_prints_the_current_version_and_exits(self):
        with mock.patch.object(sys, 'argv', ['/tmp/with', '--version']), \
                mock.patch('builtins.print') as mock_print:

            with pytest.raises(SystemExit):
                yield from main()

        version_pattern = re.compile(r'with \d+\.\d+\.\d+')

        assert mock_print.called
        assert version_pattern.match(mock_print.call_args[0][0])
