import logging
from logging import FileHandler, StreamHandler, Formatter
import pytest
from typing import List
from _pytest.config import Config
import os

logger = logging.getLogger(__name__)


def pytest_configure(config: Config):
    root_path = config.rootpath
    log_path = os.path.join(root_path, 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    file_handler = FileHandler(filename=f"{log_path}/report.log", mode='w')
    stream_handler = StreamHandler()
    formatter = Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                          datefmt='%a, %d %b %Y %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


def pytest_collection_modifyitems(session, config, items):
    '''
    修改用例使用参数化时中文的名称问题
    :param session:
    :param config:
    :param items:
    :return:
    '''
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # 用例名字
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # 用例路径
