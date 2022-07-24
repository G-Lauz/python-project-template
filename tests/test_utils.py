"""
TODO: Module docstring
"""

import os

from amodule.utils import temp_dir


class TestTempDir:
    def test_directory_creation(self):
        with temp_dir.TempDir(remove_on_exit=True) as tmp:
            assert os.path.exists(tmp.path)
