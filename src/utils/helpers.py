import os
import logging

logger = logging.getLogger()


def get_file_size(path: str):
    num = 0
    try:
        with open(path) as f:
            for num, _ in enumerate(f, 1):
                pass

    except IOError as e:
        logger.exception(f'Can not read file {path}')

    except Exception as e:
        logger.exception(f'Unexpected error getting file size {path}')

    return num


def get_file_extension(path: str):
    _, file_extension = os.path.splitext(path)
    return file_extension


def safe_list_get(l: list, idx: int, default):
    try:
        return l[idx]
    except IndexError:
        return default
