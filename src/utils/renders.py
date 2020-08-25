import os
from .helpers import get_file_size


def render_default(path: str) -> dict:
    _file_params = {
        'name': os.path.basename(path),
        'type': 'unknown',
    }

    return _file_params


def render_txt(path: str) -> dict:
    _file_params = {
        'name': os.path.basename(path),
        'type': 'text',
        'size': f'{get_file_size(path)} lines',
    }

    return _file_params


def render_bin(path: str) -> dict:
    _file_params = {
        'name': os.path.basename(path),
        'type': 'binary',
        'size': f'{os.path.getsize(path)} bytes',
    }

    return _file_params
