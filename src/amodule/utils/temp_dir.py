"""
Utility Class that feature a context manager for temporary directory
"""

import os
import shutil
import tempfile

class TempDir:
    """
    Utility Class that feature a context manager for temporary directory
    """
    def __init__(self, remove_on_exit:bool=True) -> None:
        """
        @param remove_on_exit: If the directory will be remove when getting out
            of the context manager
        """
        self._path = None
        self._remove = remove_on_exit

    def __enter__(self):
        self._path = os.path.abspath(tempfile.mkdtemp())
        if not os.path.exists(self._path):
            raise FileExistsError()
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        if self._remove and os.path.exists(self._path):
            shutil.rmtree(self._path)

        if self._remove and os.path.exists(self._path):
            raise FileExistsError(
                f"The tempory file: \"{self._path}\" was not properly remove"
            )

        if not os.path.exists(os.getcwd()):
            raise FileExistsError()

    @property
    def path(self):
        return self._path

    def join(self, *path:str):
        """
        Join to the temporary directory path.
        @param path: The paths to join

        @return : The joint directory path
        """
        return os.path.join(self._path, *path)
