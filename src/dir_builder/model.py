import os
import json
import logging

from ..utils.helpers import (
    get_file_size,
    get_file_extension
)
from ..utils.renders import (
    render_default,
    render_bin,
    render_txt,
)

from .classes import AbstractDirBuilder

logger = logging.getLogger()


class DirBuilder(AbstractDirBuilder):
    def __init__(self, root: str = '.'):
        self.root = root
        self.render_handlers = {
            '.txt': render_txt,
            '.bin': render_bin,
        }

    def _build(self, path: str) -> dict:
        dir_element = dict()

        if os.path.isdir(path) and os.access(path, os.X_OK):
            dir_element[os.path.basename(path)] = [
                self._build(os.path.join(path, dir_el))
                for dir_el in os.listdir(path)
            ]
        else:
            try:
                _exists = os.path.exists(path)
                if not _exists: raise IOError
                
                file_extension = get_file_extension(path)
                dir_element = {
                    **dir_element,
                    **self.render_handlers.get(file_extension, render_default)(path)
                }
            except IOError as e:
                logger.exception(f'File does not exists {path}')
            except Exception as e:
                logger.exception(f'Error while rendering file {path}')
        return dir_element

    def build(self) -> dict:
        return self._build(self.root)

    def build_json(self, indent: int = 2) -> str:
        return json.dumps(self._build(self.root), indent=indent)
