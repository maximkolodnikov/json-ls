import sys

from src.dir_builder.model import DirBuilder
from src.utils.helpers import safe_list_get

import logging

logging.basicConfig(format='%(asctime)s - %(message)s')

logger = logging.getLogger()

def run():
    root_path = safe_list_get(sys.argv, 1, '.')
    dir_builder = DirBuilder(root_path)
    print(dir_builder.build_json())


if __name__ == '__main__':
    try:
        run()
    except:
        logger.exception('Error while running program')